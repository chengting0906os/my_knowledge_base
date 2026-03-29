# Chapter 3：Index Scan 與 Index Only Scan

## 目標
理解 Index Scan 如何找到資料、為什麼需要再讀 heap、以及 Index Only Scan 為何更快。

---

## 3-1 B-tree Index 的結構（概念）

PostgreSQL 預設的 index 是 B-tree。想像成一本書的「索引頁」：

```
B-tree index（在 email 欄位上）：

          [M]
         /   \
      [A-L]  [N-Z]
      /   \
   [A-F] [G-L]
     |
  "user_1@..." → page 2341, offset 15   ← 記錄在 heap 的位置
  "user_10@..." → page 1023, offset 3
  "user_100@..." → page 5678, offset 7
```

Index 只存**鍵值（email）**和**指向 heap 的位置（ctid）**，不存其他欄位。

---

## 3-2 Index Scan：兩段式讀取

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'user_500000@example.com';
```

```
Index Scan using idx_users_email on users  (cost=0.42..8.44 rows=1 width=58)
                                           (actual time=0.031..0.033 rows=1 loops=1)
  Index Cond: (email = 'user_500000@example.com')
```

**執行流程**：
```
Step 1：走 B-tree index，找到 'user_500000@example.com'
        → 取得 ctid（例如：page 2341, offset 15）

Step 2：用 ctid 去 heap 讀取那一個 page
        → 拿到整列資料（id, name, email, age, city, score, created_at）
        → 這一步叫做 "heap fetch"
```

**為什麼要讀兩次？**
因為 SELECT * 需要 `age`、`city` 等欄位，但 index 只存 `email`，所以必須回到 heap 取完整資料。

---

## 3-3 Index Scan vs Seq Scan 的速度比較

```sql
-- 精準查詢：1 筆
\timing on

-- Index Scan（email 有 index）
SELECT * FROM users WHERE email = 'user_500000@example.com';

-- Seq Scan（city 沒有 index）
SELECT * FROM users WHERE city = 'Taipei' LIMIT 1;

\timing off
```

Index Scan 通常在 1ms 以內，Seq Scan 即使只要 1 筆也要掃整張表。

---

## 3-4 Index Only Scan：完全不用讀 heap

當 SELECT 的欄位**全部都在 index 裡**，PostgreSQL 可以跳過 heap 讀取：

```sql
-- 只 SELECT email（正好是 index 的 key）
EXPLAIN ANALYZE SELECT email FROM users WHERE email = 'user_500000@example.com';
```

```
Index Only Scan using idx_users_email on users  (cost=0.42..4.44 rows=1 width=32)
                                                (actual time=0.021..0.023 rows=1 loops=1)
  Index Cond: (email = 'user_500000@example.com')
  Heap Fetches: 0
```

**關鍵**：`Heap Fetches: 0`，完全不用讀 heap。

對比剛才的 Index Scan：
```
Index Scan:      width=58（整列資料）
Index Only Scan: width=32（只有 email）
```

---

## 3-5 Heap Fetches 不為 0 的情況

```sql
-- 第一次跑（資料剛插入，visibility map 可能未更新）
EXPLAIN ANALYZE SELECT email FROM users WHERE email LIKE 'user_1@%';
```

可能看到：
```
Index Only Scan ...
  Heap Fetches: 3
```

`Heap Fetches > 0` 代表 visibility map（VM）上那個 page 尚未被標記為 all-visible，
PostgreSQL 需要去 heap 確認資料是否對目前 transaction 可見（MVCC 機制）。

解法：
```sql
VACUUM users;
-- 再執行一次，Heap Fetches 應該變成 0
EXPLAIN ANALYZE SELECT email FROM users WHERE email LIKE 'user_1@%';
```

---

## 3-6 建立 Covering Index，把更多欄位加進 index

如果常常查詢 `email` + `name`，但 `name` 不在 index 裡，會走 Index Scan（需要 heap fetch）。
可以建 covering index，把 `name` include 進去：

```sql
-- 建立 covering index（INCLUDE 不影響 B-tree 結構，只是附帶儲存）
CREATE INDEX idx_users_email_covering ON users(email) INCLUDE (name, age);

-- 現在 SELECT email, name, age 可以走 Index Only Scan
EXPLAIN ANALYZE SELECT email, name, age FROM users WHERE email = 'user_500000@example.com';
```

```
Index Only Scan using idx_users_email_covering on users
  Heap Fetches: 0
```

---

## 3-7 range 查詢的 Index Scan

```sql
-- 用 PK 查範圍（id 有 index）
EXPLAIN ANALYZE SELECT * FROM users WHERE id BETWEEN 1 AND 100;
```

```
Index Scan using users_pkey on users  (cost=0.42..12.94 rows=100 width=58)
                                      (actual time=0.023..0.245 rows=100 loops=1)
  Index Cond: ((id >= 1) AND (id <= 100))
```

100 筆，用 Index Scan。

```sql
-- 同樣是 range，但範圍很大（50萬筆）
EXPLAIN ANALYZE SELECT * FROM users WHERE id BETWEEN 1 AND 500000;
```

```
Seq Scan on users  (cost=0.00..24846.00 rows=500000 width=58)
```

範圍變大（50% 的資料），Planner 改用 Seq Scan，因為大量 random I/O 比 sequential 慢。

---

## 3-8 EXPLAIN 看 Index 使用細節

```sql
-- 加上 VERBOSE 可以看到更多資訊
EXPLAIN (ANALYZE, VERBOSE)
SELECT * FROM users WHERE email = 'user_500000@example.com';
```

輸出中會有：
```
Output: id, name, email, age, city, score, created_at
```
告訴你這個節點輸出哪些欄位。

---

## 本章練習

1. 建立 `score` 欄位的 index，然後查詢 `WHERE score = 999.99`，確認走 Index Scan
2. 查詢 `SELECT score FROM users WHERE score = 999.99`，確認走 Index Only Scan，並觀察 `Heap Fetches`
3. 執行 `VACUUM users;` 後，再次觀察 `Heap Fetches` 是否變 0
4. 試試 `SELECT * FROM users WHERE id IN (1, 2, 3, 1000, 50000, 999999)`，是哪種 scan？

---

## 本章小結

| Scan 類型 | 觸發條件 | 特點 |
|----------|---------|------|
| Index Scan | 有 index，回傳少量列 | 查 index → heap fetch（兩段） |
| Index Only Scan | SELECT 欄位全在 index 裡 | 不用讀 heap，最快 |

| 指標 | 意義 |
|------|------|
| `Heap Fetches: 0` | 理想狀態，完全走 index |
| `Heap Fetches > 0` | VM 未更新，需要 VACUUM |

下一章：[Chapter 4：Bitmap Scan](04_bitmap_scan.md)
