# What is an Index in PostgreSQL?

## Overview

An index is like a **book's table of contents**. Without one, the database must scan every row (Sequential Scan) to find matching data. With one, it jumps directly — drastically reducing I/O.

- Without index → **Sequential Scan** (every row checked)
- With index → **Index Scan** (jump directly to matching rows)

```sql
CREATE INDEX index_name ON table_name (column_name);
```

**Benefits:**
- Speeds up SELECT, JOIN, WHERE, ORDER BY
- Reduces disk I/O on large tables
- UNIQUE INDEX enforces data uniqueness

**Costs:**
- Writes must maintain indexes (INSERT / UPDATE / DELETE become slower)
- Extra disk space
- Too many indexes can confuse the Optimizer (or cause it to pick the wrong one)

---

## B+ Tree Index (Most Common)

PostgreSQL's default index type is **B+ Tree**, suitable for the vast majority of use cases.

```
B+ Tree structure:
                    [30 | 70]
                   /    |    \
              [10|20] [40|60] [80|90]
              /  |  \    ...
           [10] [20] [30] ...  ← Leaf Nodes (contain row pointers)
```

- Leaf nodes are **doubly linked** → efficient ORDER BY
- Supports: `=`, `<`, `>`, `BETWEEN`, `LIKE 'abc%'`
- Not suitable for: `LIKE '%abc'`, regex

```sql
-- Create B-Tree index (default)
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_user_id
ON orders (user_id) USING BTREE;

-- Index Range Scan
SELECT * FROM orders WHERE order_id > 7 AND order_id < 12;

-- Index Only Scan (reads index only, never touches the table)
SELECT order_id FROM orders WHERE order_id > 7 AND order_id < 12;
```

---

## CONCURRENTLY — Critical for Production

```sql
-- Without CONCURRENTLY: locks the entire table during build (never do this in prod!)
CREATE INDEX idx_bad ON orders (create_time);

-- With CONCURRENTLY: no table lock, reads/writes continue (takes longer but safe)
CREATE INDEX CONCURRENTLY idx_good ON orders (create_time);
```

---

## Types of Indexes

| Type | Best For | Operators |
|---|---|---|
| **B-Tree** | Range queries, equality checks (default) | `<` `<=` `=` `>=` `>` |
| **Hash** | Exact match only | `=` |
| **GiST** | Spatial, geometric, range data | `<<` `&<` `@>` `<@` `~=` |
| **GIN** | Arrays, full-text search | `<@` `@>` `=` `&&` |
| **BRIN** | Large tables with naturally ordered data | `<` `<=` `=` `>=` `>` |

---

## B-Tree (Default)

```sql
CREATE INDEX idx_btree ON books (author);
```

- Default type when no `USING` clause specified
- Balanced tree structure → O(log n) lookup
- Handles range queries and sorting well

---

## Hash

```sql
CREATE INDEX idx_hash ON books USING HASH (author);
```

- Maps values to buckets via hash function
- Only useful for `=` — cannot do range queries
- Slightly faster than B-Tree for pure equality checks

---

## GiST (Generalized Search Tree)

```sql
CREATE INDEX idx_gist ON locations USING GIST (coordinates);
```

- Flexible framework supporting many data types
- Used for: geometric shapes, geographic data (PostGIS), range types
- Supports overlap, containment, nearest-neighbor queries

---

## GIN (Generalized Inverted Index)

```sql
CREATE INDEX idx_gin ON books USING GIN (title);
```

- Inverted index — maps each element to its containing rows
- Used for: `tsvector` (full-text search), arrays, JSONB
- Fast search, but larger storage and slower writes than B-Tree

---

## BRIN (Block Range Index)

```sql
CREATE INDEX idx_brin ON books USING BRIN (publication_year);
```

- Stores min/max summary per block range (not per row)
- Extremely small index size
- Effective only when data is **physically ordered** on disk (e.g., append-only timestamp columns)
- Useless if data is randomly distributed

---

## Verifying Index Usage with EXPLAIN

```sql
EXPLAIN SELECT * FROM books WHERE author = 'Harper Lee';
```

Look for:
- `Index Scan using idx_author` → index is being used
- `Seq Scan` → index is NOT used (or doesn't exist)

```sql
EXPLAIN ANALYZE SELECT * FROM books WHERE author = 'Harper Lee';
```

`ANALYZE` actually runs the query and shows real execution time vs estimated.

---

## When Index Becomes Ineffective

- Column has **low cardinality** (e.g., boolean, gender) — too many matching rows
- Query uses `LIKE '%keyword'` — leading wildcard bypasses B-Tree
- **Table is small** — sequential scan is faster than index lookup overhead
- Statistics are stale → Optimizer misjudges selectivity
- Function applied to indexed column: `WHERE LOWER(name) = 'foo'` (use functional index instead)

---

## Index Maintenance

```sql
-- Rebuild bloated index
REINDEX INDEX idx_author;

-- Update table statistics for Optimizer
ANALYZE books;

-- Check index usage stats
SELECT * FROM pg_stat_user_indexes WHERE relname = 'books';
```

---

## Interview Points

- What is the default index type in PostgreSQL? → B-Tree
- When would you use GIN over B-Tree? → Full-text search, array containment queries
- Why can BRIN be dangerous? → Only works if data is physically ordered; randomly inserted data makes it useless
- What does `EXPLAIN` show? → The query execution plan — whether index is used, estimated rows, cost
- Can indexes slow things down? → Yes — on writes (INSERT/UPDATE/DELETE), every index must be updated; too many indexes hurt write performance

---
---

# PostgreSQL 索引（Index）

## 概述

索引就像書本的「目錄」。沒有索引時，資料庫必須掃描整張表（Sequential Scan）才能找到符合條件的資料。有了索引，可以直接定位，大幅減少 I/O。

- 沒有 index → **Sequential Scan**（逐行掃描）
- 有 index → **Index Scan**（直接跳到對應資料）

```sql
CREATE INDEX index_name ON table_name (column_name);
```

**索引的好處：**
- 加速查詢（SELECT、JOIN、WHERE、ORDER BY）
- 減少磁碟 I/O，提升大表查詢效率
- UNIQUE INDEX 可確保資料唯一性

**索引的代價：**
- 寫入時需要同步維護索引（INSERT / UPDATE / DELETE 變慢）
- 佔用額外磁碟空間
- 索引過多會讓 Optimizer 選擇困難（甚至選錯）

---

## B+ Tree Index（最常用）

PostgreSQL 預設索引類型為 **B+ Tree**，適合絕大多數場景。

```
B+ Tree 結構示意：
                    [30 | 70]
                   /    |    \
              [10|20] [40|60] [80|90]
              /  |  \    ...
           [10] [20] [30] ...  ← Leaf Nodes（包含 row pointer）
```

- Leaf Node 之間有**雙向連結** → ORDER BY 效率高
- 支援：`=`、`<`、`>`、`BETWEEN`、`LIKE 'abc%'`
- 不適合：`LIKE '%abc'`、正則表達式

```sql
-- 建立 B-tree Index（預設）
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_user_id
ON orders (user_id) USING BTREE;

-- Index Range Scan
SELECT * FROM orders WHERE order_id > 7 AND order_id < 12;

-- Index Only Scan（只讀 Index，完全不碰 Table）
SELECT order_id FROM orders WHERE order_id > 7 AND order_id < 12;
```

---

## CONCURRENTLY — 生產環境必用

```sql
-- 不加 CONCURRENTLY：建索引時整張表被鎖住（生產環境禁止！）
CREATE INDEX idx_bad ON orders (create_time);

-- 加 CONCURRENTLY：不鎖表，建索引過程中仍可讀寫（需要更長時間但安全）
CREATE INDEX CONCURRENTLY idx_good ON orders (create_time);
```

---

## 索引類型

| 類型 | 最適用於 | 支援運算子 |
|---|---|---|
| **B-Tree** | 範圍查詢、等值查詢（預設） | `<` `<=` `=` `>=` `>` |
| **Hash** | 純等值查詢 | `=` |
| **GiST** | 空間資料、幾何、範圍型別 | `<<` `&<` `@>` `<@` `~=` |
| **GIN** | 陣列、全文搜尋 | `<@` `@>` `=` `&&` |
| **BRIN** | 大型有序資料集的範圍查詢 | `<` `<=` `=` `>=` `>` |

---

## B-Tree（預設）

```sql
CREATE INDEX idx_btree ON books (author);
```

- 不指定 `USING` 時的預設類型
- 平衡樹結構 → O(log n) 查找
- 範圍查詢和排序都適用

---

## Hash

```sql
CREATE INDEX idx_hash ON books USING HASH (author);
```

- 透過 hash function 將值映射到 bucket
- 只支援 `=`，無法做範圍查詢
- 純等值查詢略快於 B-Tree

---

## GiST（通用搜尋樹）

```sql
CREATE INDEX idx_gist ON locations USING GIST (coordinates);
```

- 彈性框架，支援多種資料型別
- 用於：幾何形狀、地理資料（PostGIS）、範圍型別
- 支援重疊、包含、最近鄰查詢

---

## GIN（通用倒排索引）

```sql
CREATE INDEX idx_gin ON books USING GIN (title);
```

- 倒排索引：將每個元素映射到包含它的所有列
- 用於：`tsvector`（全文搜尋）、陣列、JSONB
- 搜尋快，但儲存空間大、寫入比 B-Tree 慢

---

## BRIN（區塊範圍索引）

```sql
CREATE INDEX idx_brin ON books USING BRIN (publication_year);
```

- 每個 block range 只存 min/max 摘要，不是逐行存
- 索引體積極小
- 只在資料**實體上有序**時有效（例如 append-only 的時間戳欄位）
- 資料隨機分布時幾乎無效

---

## 用 EXPLAIN 驗證是否走索引

```sql
EXPLAIN SELECT * FROM books WHERE author = 'Harper Lee';
```

看輸出結果：
- `Index Scan using idx_author` → 有走索引
- `Seq Scan` → 沒走索引（索引不存在或 Optimizer 判斷不划算）

```sql
EXPLAIN ANALYZE SELECT * FROM books WHERE author = 'Harper Lee';
```

`ANALYZE` 會實際執行 query，顯示真實執行時間 vs 估算時間。

---

## 索引失效的情況

- 欄位**基數低**（如 boolean、性別）— 符合條件的列太多，走索引反而更慢
- `LIKE '%keyword'` — 前綴萬用字元讓 B-Tree 無法使用
- **資料表太小** — Sequential Scan 比 index 查找的 overhead 還快
- 統計資料過時 → Optimizer 誤判選擇性
- 對索引欄位套函數：`WHERE LOWER(name) = 'foo'`（改用 functional index）

---

## 索引維護

```sql
-- 重建膨脹的索引
REINDEX INDEX idx_author;

-- 更新表統計資料，讓 Optimizer 做出正確決策
ANALYZE books;

-- 查看索引使用狀況
SELECT * FROM pg_stat_user_indexes WHERE relname = 'books';
```

---

## 面試重點

- PostgreSQL 預設索引類型？→ B-Tree
- 什麼情況用 GIN 而不用 B-Tree？→ 全文搜尋、陣列包含查詢
- BRIN 的風險？→ 只在資料實體有序時有效；隨機插入的資料讓它幾乎無用
- `EXPLAIN` 顯示什麼？→ 查詢執行計畫：是否走索引、估算行數、成本
- 索引會讓寫入變慢嗎？→ 會，每次 INSERT/UPDATE/DELETE 都要同步更新所有相關索引；索引過多會拖慢寫入
