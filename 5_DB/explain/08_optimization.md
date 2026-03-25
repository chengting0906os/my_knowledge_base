# Chapter 8：常見警訊與優化手法

## 目標
能夠看到 EXPLAIN 輸出就找出問題，對應正確的解法。

---

## 8-1 警訊速查表

| EXPLAIN 看到 | 代表 | 解法 |
|-------------|------|------|
| `Seq Scan` 大表 + 大量 `Rows Removed` | 缺 index | 建 index |
| 預估 `rows=1` 但 `actual rows=50000` | 統計過期 | `ANALYZE` |
| Hash `Batches > 1` | Hash spill to disk | 調高 `work_mem` |
| Sort `external merge` | Sort spill to disk | 調高 `work_mem` |
| Nested Loop 內層 `loops=100000` + 無 index | N+1 查詢 | 建 index 或改 Hash Join |
| `Heap Fetches > 0`（Index Only Scan） | visibility map 未更新 | `VACUUM` |
| `Bitmap Heap Scan: lossy` | Bitmap spill | 調高 `work_mem` |
| 大量 `temp read/written` | work_mem 不足 | 調高 `work_mem` |

---

## 8-2 案例 1：Seq Scan 因缺 index

```sql
-- 現象
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 500000;
```

```
Seq Scan on orders  (cost=0.00..96346.00 rows=5 width=40)
                    (actual time=312.123..312.345 rows=5 loops=1)
  Filter: (user_id = 500000)
  Rows Removed by Filter: 4999995
Execution Time: 312.456 ms
```

500 萬筆掃到底，只找 5 筆。

**優化**：

```sql
CREATE INDEX idx_orders_user_id ON orders(user_id);
ANALYZE orders;

EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 500000;
```

```
Index Scan using idx_orders_user_id on orders
                    (actual time=0.023..0.067 rows=5 loops=1)
Execution Time: 0.089 ms    ← 從 312ms 降到 0.089ms
```

---

## 8-3 案例 2：統計過期導致 Planner 選錯計畫

```sql
-- 插入大量某特定值（製造偏斜）
INSERT INTO orders (user_id, amount, status)
SELECT 1, 100.00, 'vip'
FROM generate_series(1, 500000);

-- 不 ANALYZE，Planner 不知道有這麼多 'vip'
EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'vip';
```

Planner 預估 `rows=1250000`（預設每種 status 各佔 25%），但實際是 500000。
更嚴重的情況：Planner 可能因此選錯 join 順序或 scan 類型。

```sql
ANALYZE orders;
EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'vip';
-- 預估更準確，Planner 做出正確決策
```

---

## 8-4 案例 3：Composite Index 的欄位順序

```sql
-- 查詢模式：status 等值 + amount 範圍
EXPLAIN SELECT * FROM orders WHERE status = 'paid' AND amount > 4000;
```

**建 Composite Index 的正確順序**：把等值（=）條件的欄位放前面：

```sql
-- 正確順序
CREATE INDEX idx_orders_status_amount ON orders(status, amount);
ANALYZE orders;

EXPLAIN SELECT * FROM orders WHERE status = 'paid' AND amount > 4000;
-- 應該走 index
```

```sql
-- 測試只用 amount 的查詢（前置欄位不符）
EXPLAIN SELECT * FROM orders WHERE amount > 4000;
-- 不會走 idx_orders_status_amount（因為 status 前置欄位未指定）
```

**規則**：Composite index `(A, B)` 可用於：
- `WHERE A = ?` ✓
- `WHERE A = ? AND B = ?` ✓
- `WHERE A = ? AND B > ?` ✓
- `WHERE B = ?` ✗（跳過前置欄位）

---

## 8-5 案例 4：Partial Index（部分索引）

如果常查詢某個特定條件，可以只對那個子集建 index：

```sql
-- 只對 'pending' 的訂單建 index（因為通常只處理 pending 訂單）
CREATE INDEX idx_orders_pending ON orders(user_id) WHERE status = 'pending';
ANALYZE orders;

-- 這個查詢會走 partial index
EXPLAIN SELECT * FROM orders WHERE user_id = 1 AND status = 'pending';

-- 這個不會（因為 status 不是 'pending'）
EXPLAIN SELECT * FROM orders WHERE user_id = 1 AND status = 'paid';
```

Partial Index 的優點：
- index 更小（只包含部分資料）
- 更新 status 不是 'pending' 的資料不需要維護這個 index

---

## 8-6 案例 5：避免 Index 失效的寫法

Index 在以下情況**不會被使用**：

```sql
-- ❌ 函數包住欄位 → index 失效
EXPLAIN SELECT * FROM users WHERE LOWER(email) = 'user_1@example.com';
-- → Seq Scan（idx_users_email 不會被用）

-- ✅ 改用 expression index
CREATE INDEX idx_users_email_lower ON users(LOWER(email));
EXPLAIN SELECT * FROM users WHERE LOWER(email) = 'user_1@example.com';
-- → Index Scan
```

```sql
-- ❌ 隱式型別轉換
EXPLAIN SELECT * FROM users WHERE id = '1';
-- PostgreSQL 通常還是走 index，但某些情況下（型別不匹配）會失效

-- ✅ 保持型別一致
EXPLAIN SELECT * FROM users WHERE id = 1;
```

```sql
-- ❌ LIKE 以萬用字元開頭
EXPLAIN SELECT * FROM users WHERE email LIKE '%@example.com';
-- → Seq Scan（B-tree 只支援前置匹配）

-- ✅ 前置匹配可走 index
EXPLAIN SELECT * FROM users WHERE email LIKE 'user_1%';
-- → Index Scan（前置匹配）
```

---

## 8-7 案例 6：用 EXPLAIN 確認 Subquery 的執行方式

```sql
-- Subquery 方式
EXPLAIN ANALYZE
SELECT * FROM users WHERE id IN (
    SELECT user_id FROM orders WHERE amount > 4500
);
```

PostgreSQL 通常會把 IN (subquery) 轉換成 join 或 semi-join，用 EXPLAIN 確認：

```
Hash Semi Join  (...)
  ->  Seq Scan on users
  ->  Hash
        ->  Seq Scan on orders
              Filter: (amount > 4500)
```

或者：

```
Nested Loop Semi Join
  ->  Seq Scan on users
  ->  Index Scan on orders
        Index Cond: (user_id = users.id)
        Filter: (amount > 4500)
```

看到 Semi Join 就代表 PostgreSQL 正確優化了 IN 子查詢。

---

## 8-8 綜合診斷流程

拿到一個慢查詢，按這個流程：

```
1. 執行 EXPLAIN (ANALYZE, BUFFERS)

2. 找最慢的節點
   → actual time 最大的那行

3. 是 Seq Scan 嗎？
   → 有 "Rows Removed by Filter" 嗎？很多？
   → 考慮在過濾欄位建 index

4. 預估 rows 和實際差距大嗎？
   → 差 10 倍以上 → ANALYZE

5. Hash Batches > 1 或 Sort Method: external merge？
   → 調高 work_mem

6. Nested Loop 內層 loops 很大？
   → 內表有 index 嗎？沒有就建

7. Buffers: read 很多？
   → 調大 shared_buffers，或查詢本身需要大量磁碟讀取
```

---

## 8-9 實戰：一個複雜慢查詢的診斷

```sql
-- 模擬一個慢查詢
EXPLAIN (ANALYZE, BUFFERS)
SELECT u.city,
       COUNT(DISTINCT u.id) AS user_count,
       AVG(o.amount) AS avg_amount
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE o.created_at >= NOW() - INTERVAL '30 days'
  AND o.status != 'cancelled'
GROUP BY u.city
ORDER BY avg_amount DESC;
```

練習：
1. 找出最耗時的節點
2. 判斷是否需要建 `orders(created_at)` 的 index
3. 判斷 Hash Join 的記憶體使用是否合理
4. 預估 rows 是否準確

---

## 本章練習

1. 找出你的 EXPLAIN 輸出中 `actual time` 最大的節點，描述它的問題
2. 對 `orders(status, amount)` 建 composite index，用 3 種查詢測試哪些有效、哪些無效
3. 建一個 expression index：`CREATE INDEX ON users(LOWER(name))`，確認 `WHERE LOWER(name) = 'user_1'` 走 index
4. 嘗試用 `SET enable_seqscan = off` 強制走 index，比較和 Seq Scan 的速度差異

---

## 本章小結

優化的思路不是「一定要加 index」，而是：

1. **先看 EXPLAIN**，找出瓶頸在哪
2. **確認問題**：是 I/O？記憶體？統計不準？
3. **對症下藥**：index / ANALYZE / work_mem / shared_buffers
4. **用 EXPLAIN ANALYZE 驗證**效果

完成所有章節！回顧所有章節：[Chapter 0](00_setup.md) → [1](01_explain_structure.md) → [2](02_seq_scan.md) → [3](03_index_scan.md) → [4](04_bitmap_scan.md) → [5](05_join_types.md) → [6](06_buffers.md) → [7](07_statistics.md) → [8](08_optimization.md)
