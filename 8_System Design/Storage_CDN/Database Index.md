# Database Index

## 中文版

索引是一種輔助資料結構，讓資料庫不用全表掃描（Full Table Scan）就能快速找到資料。

### 底層結構

| 類型 | 結構 | 適合 |
|------|------|------|
| **B-Tree Index** | 平衡樹 | 範圍查詢、排序、等值查詢（最常用） |
| **Hash Index** | Hash Table | 僅限等值查詢，不支援範圍 |
| **Full-Text Index** | 倒排索引 | 全文搜尋 |

### 索引類型

| | 說明 |
|---|---|
| **Primary Index** | 主鍵自動建立，資料依主鍵排序（Clustered） |
| **Secondary Index** | 非主鍵欄位上的索引（Non-Clustered） |
| **Composite Index** | 多欄位聯合索引，遵守最左前綴原則 |
| **Covering Index** | 查詢所需欄位全在索引中，不需回表 |

### 最左前綴原則
複合索引 `(A, B, C)`：
- ✅ 查 `A`、`A+B`、`A+B+C`
- ❌ 查 `B`、`C`、`B+C`（跳過 A）

### 代價
- 加速讀取，**拖慢寫入**（每次 INSERT/UPDATE/DELETE 都要更新索引）
- 佔用額外磁碟空間
- 不是越多越好，常查詢且選擇性高的欄位才值得建

## English Version

An index is an auxiliary data structure that allows the database to find data quickly without a full table scan.

### Underlying Structures

| Type | Structure | Best for |
|------|-----------|---------|
| **B-Tree Index** | Balanced tree | Range queries, sorting, equality (most common) |
| **Hash Index** | Hash table | Equality only — no range support |
| **Full-Text Index** | Inverted index | Full-text search |

### Index Types

| | Description |
|---|---|
| **Primary Index** | Auto-created on primary key; data physically sorted by it (Clustered) |
| **Secondary Index** | Index on non-primary-key columns (Non-Clustered) |
| **Composite Index** | Multi-column index; follows leftmost prefix rule |
| **Covering Index** | All queried columns exist in the index — no need to access the base table |

### Leftmost Prefix Rule
Composite index `(A, B, C)`:
- ✅ Queries on `A`, `A+B`, `A+B+C`
- ❌ Queries on `B`, `C`, `B+C` (skip A — index not used)

### Trade-offs
- Speeds up reads, **slows down writes** (every INSERT/UPDATE/DELETE must update indexes)
- Consumes extra disk space
- More is not always better — only index frequently queried, high-cardinality columns
