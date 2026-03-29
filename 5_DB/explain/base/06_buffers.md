# Chapter 6：BUFFERS 與 Cache

## 目標
看懂 `EXPLAIN (ANALYZE, BUFFERS)` 輸出的 shared hit / read，理解 PostgreSQL 的 buffer cache，判斷查詢是否受 I/O 瓶頸影響。

---

## 6-1 PostgreSQL 的 I/O 架構

```
應用程式
    ↓
PostgreSQL Backend
    ↓
Shared Buffer Cache（記憶體，預設 128MB）
    ↓（cache miss 才讀）
OS Page Cache（記憶體）
    ↓（OS cache miss 才讀）
磁碟
```

PostgreSQL 自己管一層 cache 叫 **shared_buffers**，所有 backend process 共用。
資料先在 shared_buffers 找，找不到才去 OS cache，再找不到才讀磁碟。

---

## 6-2 開啟 BUFFERS 選項

```sql
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE age = 30;
```

輸出多了一行：
```
Seq Scan on users  (cost=0.00..24846.00 rows=16529 width=58)
                   (actual time=0.023..189.451 rows=16642 loops=1)
  Filter: (age = 30)
  Rows Removed by Filter: 983358
  Buffers: shared hit=14234 read=201
```

---

## 6-3 逐一解讀 Buffers 指標

| 指標 | 意義 |
|------|------|
| `shared hit` | 從 shared_buffers（記憶體）讀取的 page 數 |
| `shared read` | 從磁碟讀取的 page 數（cache miss） |
| `shared dirtied` | 在記憶體中被修改的 page 數 |
| `shared written` | 被寫回磁碟的 page 數 |
| `local hit/read` | temporary table 的 cache hit/miss |
| `temp read/written` | sort/hash spill 用的暫存空間 |

---

## 6-4 Cold Cache vs Warm Cache

**第一次執行（cold cache）**：

```sql
-- 清除 shared_buffers（需要 superuser，lab 用戶可能沒有）
-- 只是讓你理解概念，不一定要執行
-- pg_prewarm 或重啟 PostgreSQL 可以清 cache

EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE age = 30;
```

```
Buffers: shared hit=0 read=14435    ← 全部從磁碟讀
```

**第二次執行（warm cache）**：

```sql
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE age = 30;
```

```
Buffers: shared hit=14234 read=201  ← 大部分從 cache 讀，快多了
```

**實際驗證**：

```sql
-- 跑兩次，比較 Execution Time
\timing on
SELECT * FROM users WHERE age = 30;  -- 第一次：較慢
SELECT * FROM users WHERE age = 30;  -- 第二次：快很多
\timing off
```

---

## 6-5 read 很多是什麼意思？

```
Buffers: shared hit=100 read=50000   ← read 遠大於 hit
```

代表：
1. shared_buffers 不夠大（大部分資料進不了 cache）
2. 資料分散在很多 page（hot data 沒被 cache 住）
3. 這個查詢 I/O bound（受磁碟速度限制）

**調大 shared_buffers**（在 postgresql.conf）：
```
shared_buffers = 2GB   # 建議設為實體記憶體的 25%
```

---

## 6-6 temp read/written：Sort 和 Hash 的 Spill

```sql
-- 強制用少量記憶體
SET work_mem = '1MB';

EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM users ORDER BY score;
```

可能看到：
```
Sort  (cost=... rows=... width=...)
  Sort Method: external merge  Disk: 65432kB   ← spill to disk！
  Buffers: shared hit=14435, temp read=8192 written=8192
```

| 看到這個 | 代表 |
|---------|------|
| `Sort Method: quicksort` | 在記憶體排序（OK） |
| `Sort Method: external merge` | 記憶體不夠，spill to disk（慢） |
| `temp read/written > 0` | 有暫存 I/O |

```sql
-- 調回合理的 work_mem
SET work_mem = '64MB';
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users ORDER BY score;
-- 應該看到 Sort Method: quicksort
```

---

## 6-7 用 BUFFERS 找出 index 效果

```sql
-- 沒有 index 的查詢
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE score > 999;
```

```
Seq Scan on users
  Buffers: shared hit=14435
  -- 讀了全部的 page
```

```sql
-- 建 index
CREATE INDEX IF NOT EXISTS idx_users_score ON users(score);
ANALYZE users;

EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE score > 999;
```

```
Bitmap Heap Scan on users
  Heap Blocks: exact=15
  Buffers: shared hit=21   ← 只讀了 21 個 page！
```

從讀 14435 個 page 降到 21 個，差了將近 700 倍。

---

## 6-8 完整分析一個複雜查詢

```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT u.city, COUNT(*), AVG(o.amount)
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE o.status = 'paid'
GROUP BY u.city
ORDER BY COUNT(*) DESC;
```

閱讀清單：
- [ ] 哪個節點的 `actual time` 最大？
- [ ] `Buffers: read` 主要在哪個節點？
- [ ] Hash Join 的 `Batches` 是幾？
- [ ] 有沒有 `temp read/written`？

---

## 本章練習

1. 對 `users` 表執行兩次相同查詢，比較第一次和第二次的 `shared read` vs `hit`
2. 設 `work_mem = '512kB'`，執行 `ORDER BY score`，觀察是否 spill
3. 建立 `idx_users_score` 後，比較有無 index 的 `Buffers` 差異
4. 在 Hash Join 的查詢中觀察 `Batches` 和 `Memory Usage`

---

## 本章小結

| 指標 | 好 | 壞 |
|------|----|----|
| `shared hit` | 越多越好（cache 命中） | |
| `shared read` | | 越多代表越多磁碟 I/O |
| `temp read/written` | 0 | > 0 代表 spill to disk |
| Sort Method | `quicksort`（in memory） | `external merge`（spill） |
| Hash Batches | `1`（in memory） | `> 1`（spill） |

下一章：[Chapter 7：統計資訊與 Planner 決策](07_statistics.md)
