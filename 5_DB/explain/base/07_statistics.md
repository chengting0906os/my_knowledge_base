# Chapter 7：統計資訊與 Planner 決策

## 目標
理解 Planner 如何用統計資訊預估 rows，知道預估不準的原因，以及如何修正。

---

## 7-1 Planner 靠什麼決定計畫？

PostgreSQL 的 Query Planner 是個**成本估算模型**，它不執行查詢，而是靠**統計資訊**預測：
- 每種計畫的代價（cost）
- 每個節點會回傳幾列（rows）

統計資訊儲存在 `pg_statistic`（底層）和 `pg_stats`（可讀的 view）。

---

## 7-2 查看欄位的統計資訊

```sql
SELECT attname, n_distinct, correlation, most_common_vals, most_common_freqs
FROM pg_stats
WHERE tablename = 'users' AND attname = 'city';
```

輸出：
```
attname | n_distinct | correlation | most_common_vals                                                    | most_common_freqs
--------+------------+-------------+---------------------------------------------------------------------+------------------
city    |          5 |  0.00842    | {Taipei,Kaohsiung,Tainan,Taichung,Hsinchu}                          | {0.203,0.201,0.200,0.199,0.197}
```

| 欄位 | 意義 |
|------|------|
| `n_distinct` | 有幾種不同的值（正數 = 絕對數量，負數 = 比例） |
| `correlation` | 資料在磁碟上的排列順序與值的順序相關性（-1 到 1，接近 1 最理想） |
| `most_common_vals` | 出現最多次的值 |
| `most_common_freqs` | 對應每個值出現的頻率（加總不超過 1） |

---

## 7-3 Planner 如何預估 rows

以 `WHERE city = 'Taipei'` 為例：

```
total rows = 1,000,000
freq('Taipei') = 0.203

預估 rows = 1,000,000 × 0.203 = 203,000
```

```sql
EXPLAIN SELECT * FROM users WHERE city = 'Taipei';
-- rows=203000（Planner 的預估，應接近 200000）
```

對比 `WHERE age = 30`（age 沒有 most_common_vals，只有 histogram）：

```sql
SELECT histogram_bounds FROM pg_stats WHERE tablename = 'users' AND attname = 'age';
```

Planner 用 histogram 估算 `age = 30` 大概在哪個 bucket，算出頻率。

---

## 7-4 製造預估不準的情況

讓我們故意讓統計過期：

```sql
-- 插入大量偏斜資料（全部都是 age = 99）
INSERT INTO users (name, email, age, city, score)
SELECT 'extra_' || i, 'extra_' || i || '@test.com', 99, 'Taipei', 0
FROM generate_series(1, 200000) i;

-- 不執行 ANALYZE，讓統計資訊過期
-- 查詢 age = 99（現在有 200000 筆，但統計不知道）
EXPLAIN ANALYZE SELECT * FROM users WHERE age = 99;
```

你會看到預估 rows 和實際 rows 差距很大：
```
rows=16529   ← Planner 預估（舊統計）
rows=200000  ← 實際（新資料）
```

這種差距會造成 Planner 選錯計畫（例如應該用 Seq Scan 卻選了 Index Scan）。

---

## 7-5 ANALYZE 修正統計

```sql
ANALYZE users;

EXPLAIN ANALYZE SELECT * FROM users WHERE age = 99;
```

執行 ANALYZE 後，預估和實際應該接近很多。

**什麼時候需要 ANALYZE？**
- 大量 INSERT/UPDATE/DELETE 之後
- autovacuum 會自動執行，但大量寫入時可能跟不上

---

## 7-6 相關欄位的統計問題

```sql
-- city = 'Taipei' AND age = 30
-- Planner 假設兩個條件獨立計算
EXPLAIN SELECT * FROM users WHERE city = 'Taipei' AND age = 30;
```

Planner 計算：
```
P(city='Taipei') × P(age=30) = 0.203 × 0.0167 ≈ 0.0034
→ 預估 1,000,000 × 0.0034 ≈ 3400 筆
```

但實際上 city 和 age 完全獨立，所以：
```
實際 ≈ 200,000（Taipei）× 1/60（每個 age 各 1/60）≈ 3333 筆
```

這次剛好差不多。但如果欄位有**相關性**（例如 city='Taipei' 的人 age 分佈偏向年輕），
Planner 的獨立假設就會差很多。

**解法：Extended Statistics**

```sql
-- 告訴 Planner 這兩個欄位有相關性
CREATE STATISTICS stat_users_city_age ON city, age FROM users;
ANALYZE users;

EXPLAIN SELECT * FROM users WHERE city = 'Taipei' AND age = 30;
-- 預估應該更準
```

---

## 7-7 n_distinct 不準的問題

`n_distinct` 是 Planner 估算 GROUP BY、index 的依據。

```sql
SELECT attname, n_distinct FROM pg_stats
WHERE tablename = 'users' AND attname IN ('city', 'email', 'age');
```

```
attname | n_distinct
--------+----------
city    | 5            ← 正確（只有 5 個城市）
email   | -1           ← -1 代表 unique（每列都不同）
age     | 61           ← 61 種不同的 age 值
```

預設 `default_statistics_target = 100`（收集 100 個 most_common_vals）。
如果欄位的 distinct 值很多，可以提高：

```sql
-- 針對特定欄位提高統計精細度
ALTER TABLE users ALTER COLUMN score SET STATISTICS 500;
ANALYZE users;
```

---

## 7-8 用 pg_stats 診斷 Planner 預估偏差

```sql
-- 查詢：找出哪些欄位的統計可能不準
SELECT
    attname,
    n_distinct,
    correlation,
    array_length(most_common_vals::text::text[], 1) AS n_common_vals
FROM pg_stats
WHERE tablename = 'users'
ORDER BY attname;
```

如果 `correlation` 接近 0 但欄位常用於 range scan，表示資料很亂（需要更多 random I/O）。

---

## 本章練習

1. 查看 `orders` 表 `status` 欄位的 `most_common_vals` 和 `most_common_freqs`
2. 手動計算 `WHERE status = 'paid'` 的預估 rows，和 EXPLAIN 的結果對比
3. 插入 10 萬筆 `status = 'new'` 的 orders，不執行 ANALYZE，看預估是否偏差
4. 執行 `ANALYZE orders;`，再看預估是否修正

---

## 本章小結

| 概念 | 重點 |
|------|------|
| `pg_stats` | 查看欄位統計（most_common_vals、histogram、n_distinct） |
| Planner 預估 | 基於統計資訊估算 rows，不是精確值 |
| 預估偏差 | 大量寫入後統計過期 → `ANALYZE` |
| 欄位相關性 | Planner 假設獨立，有相關時用 Extended Statistics |
| `n_distinct` 不準 | 提高 `statistics_target` |

下一章：[Chapter 8：常見警訊與優化手法](08_optimization.md)
