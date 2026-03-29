# Chapter 2：Sequential Scan（全表掃描）

## 目標
理解 Seq Scan 什麼時候出現、為什麼有時候用 Seq Scan 比 index 更快，以及如何判斷它是否是瓶頸。

---

## 2-1 Seq Scan 是什麼

Seq Scan = Sequential Scan，**從頭到尾讀完整張表**，再用 Filter 過濾掉不符合條件的列。

```
磁碟上的 heap：[ page1 ][ page2 ][ page3 ]...[ pageN ]
                  ↓         ↓         ↓             ↓
                全部讀取，遇到不符合條件的就丟掉
```

---

## 2-2 觀察 Seq Scan

`city` 欄位目前沒有 index，所以會走 Seq Scan：

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE city = 'Taipei';
```

預期輸出：
```
Seq Scan on users  (cost=0.00..24846.00 rows=200000 width=58)
                   (actual time=0.031..215.234 rows=199847 loops=1)
  Filter: (city = 'Taipei')
  Rows Removed by Filter: 800153
Planning Time: 0.089 ms
Execution Time: 221.456 ms
```

**逐行解讀**：

| 欄位 | 解讀 |
|------|------|
| `cost=0.00..24846.00` | startup=0（立刻開始讀），total=24846（讀完整張表的代價） |
| `rows=200000` | 預估回傳 20 萬筆 |
| `actual rows=199847` | 實際 199847 筆，預估準確 |
| `actual time=0.031..215.234` | 第一筆出現在 0.031ms，全部讀完花 215ms |
| `Rows Removed by Filter: 800153` | 80 萬筆被過濾掉（讀了但沒用） |

**注意**：`Rows Removed by Filter: 800153` 代表它讀了 **100 萬筆**，丟掉 80 萬，只回傳 20 萬。

---

## 2-3 Seq Scan 不一定是壞事

試試看回傳「大量資料」的情況：

```sql
-- 回傳全部資料（100%）
EXPLAIN SELECT * FROM users;
```

```
Seq Scan on users  (cost=0.00..18334.00 rows=1000000 width=58)
```

沒有 Filter，直接全掃，這是最有效率的方式。

```sql
-- 回傳 80% 的資料（age 不等於 18，約 98%）
EXPLAIN SELECT * FROM users WHERE age != 18;
```

```
Seq Scan on users  (cost=0.00..24846.00 rows=983471 width=58)
  Filter: (age <> 18)
```

**結論**：即使 `age` 有 index，Planner 也不會用它，因為回傳 98% 的資料用 Seq Scan 更快。

---

## 2-4 Planner 如何決定用 Seq Scan 還是 Index？

Planner 會估算兩種方式的 cost，選便宜的那個。

決策關鍵在於**選擇率（selectivity）**：這個查詢會回傳幾 % 的資料？

```
回傳比例低（< ~5%）  →  通常用 Index Scan
回傳比例高（> ~10%） →  通常用 Seq Scan
中間地帶              →  可能用 Bitmap Scan
```

實際驗證：

```sql
-- 只有 1 個城市 = 20%，還是 Seq Scan
EXPLAIN SELECT * FROM users WHERE city = 'Taipei';

-- 只有 1 筆（email 精準查詢）→ Index Scan
EXPLAIN SELECT * FROM users WHERE email = 'user_1@example.com';
```

---

## 2-5 強迫走 Seq Scan（測試用）

有時候你想比較 index vs no-index 的速度差異：

```sql
-- 關掉所有 index scan
SET enable_indexscan = off;
SET enable_bitmapscan = off;

EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'user_1@example.com';
-- 現在會走 Seq Scan

-- 記得還原
SET enable_indexscan = on;
SET enable_bitmapscan = on;
```

---

## 2-6 `Rows Removed by Filter` 是重要警訊

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE score > 999;
```

```
Seq Scan on users
  Filter: (score > 999::numeric)
  Rows Removed by Filter: 998989
```

`score > 999` 只有大約 1000 筆符合，卻掃了 100 萬筆丟掉 99.9 萬筆。
→ 這就是應該建 index 的信號。

**判斷標準**：
```
Rows Removed by Filter / total rows > 90%
且 actual rows 很少
→ 考慮建 index
```

---

## 2-7 動手建 index，觀察從 Seq Scan 變成 Index Scan

```sql
-- Step 1：記錄建 index 前的執行時間
EXPLAIN ANALYZE SELECT * FROM users WHERE score > 999;

-- Step 2：建 index
CREATE INDEX idx_users_score ON users(score);
ANALYZE users;

-- Step 3：同樣查詢，觀察計畫變化
EXPLAIN ANALYZE SELECT * FROM users WHERE score > 999;
```

建 index 後，你應該看到從 Seq Scan 變成 Index Scan 或 Bitmap Scan。
（下一章會詳細說明 Index Scan）

---

## 本章練習

1. 執行 `EXPLAIN ANALYZE SELECT * FROM users WHERE age BETWEEN 25 AND 35;`
   - 它用了什麼 scan？
   - `Rows Removed by Filter` 是多少？
   - 這個查詢值得建 index 嗎？為什麼？

2. 執行 `EXPLAIN SELECT * FROM users WHERE city = 'Taipei' AND city = 'Kaohsiung';`
   - 這個查詢邏輯上永遠不會有結果，Planner 知道嗎？rows 是多少？

---

## 本章小結

| 概念 | 重點 |
|------|------|
| Seq Scan | 從頭讀完整張表，遇到不符合的丟掉 |
| 不一定是壞事 | 回傳比例高時，比 index 更快 |
| 警訊 | `Rows Removed by Filter` 很大 + 回傳列數很少 |
| 決策依據 | 選擇率（回傳 % 越低，越傾向用 index） |

下一章：[Chapter 3：Index Scan 與 Index Only Scan](03_index_scan.md)
