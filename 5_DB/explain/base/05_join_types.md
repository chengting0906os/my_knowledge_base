# Chapter 5：Join 類型

## 目標
理解 Nested Loop、Hash Join、Merge Join 三種 Join 的運作原理，知道 EXPLAIN 裡哪些指標最重要。

---

## 準備

先確認 orders 上有 user_id 的 index：

```sql
CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id);
ANALYZE orders;
```

---

## 5-1 Nested Loop Join

### 原理

```python
for each row in outer_table:         # 外表（小表）
    for each matching row in inner_table:  # 內表（用 index 查）
        yield combined_row
```

外表的每一列，都去內表查一次（透過 index）。

### 觸發條件
- 外表很小（幾列到幾千列）
- 內表有 index

### 實際觀察

```sql
-- 取少量 users（10筆），join 到 orders
EXPLAIN ANALYZE
SELECT u.name, o.amount
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE u.id <= 10;
```

```
Nested Loop  (cost=0.98..258.42 rows=50 width=46)
             (actual time=0.054..0.987 rows=52 loops=1)
  ->  Index Scan on users  (cost=0.42..8.94 rows=10 width=14)
                           (actual time=0.021..0.045 rows=10 loops=1)
        Index Cond: (id <= 10)
  ->  Index Scan on orders  (cost=0.56..24.85 rows=5 width=36)
                            (actual time=0.023..0.085 rows=5 loops=10)  ← loops=10 ！
        Index Cond: (user_id = u.id)
```

**關鍵看 `loops=10`**：
- 外表（users）回傳 10 筆
- 內表（orders）的 Index Scan 被執行了 **10 次**（每次查一個 user_id）
- `actual time=0.023..0.085` 是**每一次**的時間
- 實際總時間 ≈ `0.085 ms × 10 = 0.85 ms`

### loops 陷阱

```sql
-- 外表變大（1000筆）
EXPLAIN ANALYZE
SELECT u.name, o.amount
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE u.id <= 1000;
```

```
->  Index Scan on orders
      actual time=0.023..0.087 rows=5 loops=1000   ← 1000 次！
```

**總時間 ≈ `0.087 ms × 1000 = 87 ms`**。
外表再大下去，Planner 就會改用 Hash Join。

---

## 5-2 Hash Join

### 原理

```python
# Step 1：Build phase（建 hash table）
hash_table = {}
for row in smaller_table:
    hash_table[row.join_key] = row

# Step 2：Probe phase（探查）
for row in larger_table:
    if row.join_key in hash_table:
        yield combined_row
```

### 觸發條件
- 兩張表都較大
- 或內表沒有合用的 index

### 實際觀察

```sql
-- 大量 join，預期走 Hash Join
EXPLAIN ANALYZE
SELECT u.city, COUNT(*), AVG(o.amount)
FROM users u
JOIN orders o ON o.user_id = u.id
GROUP BY u.city;
```

```
HashAggregate  (...)
  ->  Hash Join  (cost=32847.00..128456.78 rows=5000000 width=22)
                 (actual time=892.123..8234.567 rows=5000000 loops=1)
        Hash Cond: (o.user_id = u.id)
        ->  Seq Scan on orders  (actual time=0.031..1234.567 rows=5000000 loops=1)
        ->  Hash  (actual time=456.789..456.789 rows=1000000 loops=1)
              Buckets: 131072  Batches: 1  Memory Usage: 65536kB
              ->  Seq Scan on users  (rows=1000000 loops=1)
```

### Hash 節點的重要指標

```
Hash  (...)
  Buckets: 131072   ← hash table 的 bucket 數量
  Batches: 1        ← 分幾批處理（1 = 全在記憶體）
  Memory Usage: 65536kB  ← 用了多少記憶體
```

**`Batches > 1` 是警訊！**

```
Batches: 8   ← hash table 太大，分 8 批，spill to disk
```

記憶體不夠，PostgreSQL 把部分 hash table 寫到暫存檔，大幅降低效能。

```sql
-- 調高 work_mem 解決
SET work_mem = '256MB';
EXPLAIN ANALYZE ...;
-- 應該看到 Batches: 1
```

---

## 5-3 Merge Join

### 原理

兩邊都**按 join key 排好序**，像合併兩個已排序的 list：

```python
i, j = 0, 0
while i < len(table_a) and j < len(table_b):
    if table_a[i].key == table_b[j].key:
        yield combined_row
        j += 1
    elif table_a[i].key < table_b[j].key:
        i += 1
    else:
        j += 1
```

### 觸發條件
- join key 已有排序（例如已走過 index，或已經 sort）
- 通常在 merge join 的代價比其他 join 低時由 Planner 選擇

### 強制觀察

```sql
-- 關掉其他 join，強制走 Merge Join
SET enable_hashjoin = off;
SET enable_nestloop = off;

EXPLAIN ANALYZE
SELECT u.id, o.amount
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE u.id <= 10000;

SET enable_hashjoin = on;
SET enable_nestloop = on;
```

```
Merge Join  (cost=... rows=... width=...)
  Merge Cond: (u.id = o.user_id)
  ->  Index Scan on users  (already sorted by id)
  ->  Index Scan on orders (already sorted by user_id)
```

如果 join key 上沒有 index，Planner 可能在 Merge Join 前加一個 Sort 節點：

```
Merge Join
  ->  Sort (Sort Key: u.id)
        ->  Seq Scan on users
  ->  Sort (Sort Key: o.user_id)
        ->  Seq Scan on orders
```

---

## 5-4 三種 Join 比較

| | Nested Loop | Hash Join | Merge Join |
|--|------------|-----------|------------|
| **最適合** | 外表小 + 內表有 index | 大表 join，無 index | 兩表已排序 |
| **記憶體** | 低 | 高（build hash table） | 低（需排序則高） |
| **Disk spill** | 不會 | `Batches > 1` 時 | Sort 可能 spill |
| **警訊** | `loops` 很大 + 內表無 index | `Batches > 1` | Sort 節點成本高 |

---

## 5-5 找出 Join 的瓶頸

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT u.name, SUM(o.amount)
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE o.status = 'paid'
GROUP BY u.name
ORDER BY SUM(o.amount) DESC
LIMIT 10;
```

閱讀步驟：
1. 找最深縮排節點（最先執行）
2. 比較每個節點的 `actual time`，找最大的
3. 看 `loops`，注意 Nested Loop 內層的累計時間
4. 看 `Buffers: read` 是否很大（大量磁碟讀取）

---

## 本章練習

1. 執行一個只取 5 筆 users 的 join，確認是 Nested Loop，觀察 `loops`
2. 執行全量 join（不加 WHERE），觀察是 Hash Join，看 `Batches` 和 `Memory Usage`
3. 把 `work_mem` 設成 `'1MB'`，再執行全量 join，看 `Batches` 是否變大
4. 關掉 hashjoin 和 nestloop，強制 Merge Join，觀察有無額外 Sort 節點

---

## 本章小結

| Join 類型 | 觸發 | 最重要的指標 |
|---------|------|------------|
| Nested Loop | 外表小 + 內表有 index | 內表的 `loops` 數量 |
| Hash Join | 大表，無 index | `Batches`（> 1 代表 spill） |
| Merge Join | 已排序或有序 index | 是否有額外 Sort 節點 |

下一章：[Chapter 6：BUFFERS 與 Cache](06_buffers.md)
