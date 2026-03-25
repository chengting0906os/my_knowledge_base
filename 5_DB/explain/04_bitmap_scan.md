# Chapter 4：Bitmap Scan

## 目標
理解 Bitmap Scan 解決了什麼問題、兩個階段分別做什麼，以及 lossy 是什麼警訊。

---

## 4-1 為什麼需要 Bitmap Scan？

先來理解問題所在：

- **Seq Scan**：讀整張表，random access 少，效率高，但讀太多不必要的資料
- **Index Scan**：精準找到目標，但每一筆都是一次 random I/O（去不同 heap page）

當符合條件的資料**不少但也不多**（例如 5%～30%），Index Scan 會有大量 random I/O：

```
Index Scan（100 筆隨機散落在 100 個不同 page）：
  read page_3241 → 取 1 筆
  read page_8823 → 取 1 筆
  read page_1023 → 取 1 筆
  ...（100 次 random I/O）
```

Bitmap Scan 的解法：**先收集所有目標位置，再依 page 順序批次讀取，把 random I/O 變成 sequential I/O**。

---

## 4-2 觀察 Bitmap Scan

先確認 `age` 欄位有 index（Chapter 2 結尾有建，若沒有先建）：

```sql
CREATE INDEX IF NOT EXISTS idx_users_age ON users(age);
ANALYZE users;
```

查詢一個中等範圍的條件：

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE age BETWEEN 20 AND 25;
```

預期輸出：
```
Bitmap Heap Scan on users  (cost=1823.45..19234.67 rows=98234 width=58)
                           (actual time=18.234..312.456 rows=99012 loops=1)
  Recheck Cond: ((age >= 20) AND (age <= 25))
  Heap Blocks: exact=14823
  ->  Bitmap Index Scan on idx_users_age  (cost=0.00..1799.00 rows=98234 width=0)
                                          (actual time=14.123..14.123 rows=99012 loops=1)
        Index Cond: ((age >= 20) AND (age <= 25))

Planning Time: 0.134 ms
Execution Time: 318.678 ms
```

---

## 4-3 兩個階段逐步解析

### Phase 1：Bitmap Index Scan（子節點，先執行）

```
Bitmap Index Scan on idx_users_age
  Index Cond: ((age >= 20) AND (age <= 25))
  actual rows=99012  ← 找到 99012 筆符合的資料
```

這個階段：
1. 走 B-tree index 找到所有 age 在 20～25 的 entry
2. **不去讀 heap**，只建立一個 bitmap（記憶體中的位元圖）
3. Bitmap 記錄：「heap 的第 X 個 page 有我要的資料」

```
Bitmap（概念示意）：
page 0:   0
page 1:   1  ← 這個 page 有符合的資料
page 2:   0
page 3:   1  ← 這個 page 有符合的資料
...
```

注意：`width=0`！Bitmap Index Scan 完全不回傳資料列，只回傳位置資訊。

### Phase 2：Bitmap Heap Scan（父節點，後執行）

```
Bitmap Heap Scan on users
  Recheck Cond: ((age >= 20) AND (age <= 25))
  Heap Blocks: exact=14823
```

這個階段：
1. 依照 bitmap，**按 page 順序**讀取 heap（sequential I/O！）
2. 讀到該 page 後，用 `Recheck Cond` 再過濾一次
3. `Heap Blocks: exact=14823` → 讀了 14823 個 heap page

**為什麼需要 Recheck？**
Bitmap 是 page-level 的（記錄「這個 page 有符合的資料」），不是 row-level 的。
讀到 page 後，該 page 上可能有多筆資料，需要 Recheck 確認每一筆是否真的符合條件。

---

## 4-4 Exact vs Lossy

### Exact（正常狀態）

```
Heap Blocks: exact=14823
```

每個 bit 對應一**列**（row），Bitmap 精確記錄哪幾列符合。

### Lossy（記憶體不足時）

```
Heap Blocks: lossy=14823
```

記憶體不夠放下所有 row-level 的位置，改成每個 bit 對應一個 **page**。
影響：Recheck 要做更多工作（整個 page 的每一列都要重新檢查）。

**如何解決 Lossy？**

```sql
-- 查看目前的 work_mem
SHOW work_mem;
-- 預設通常是 4MB

-- 在 session 中調高（不影響全局）
SET work_mem = '64MB';

-- 再執行同樣查詢，觀察是否從 lossy 變 exact
EXPLAIN ANALYZE SELECT * FROM users WHERE age BETWEEN 20 AND 25;
```

---

## 4-5 BitmapAnd：兩個 index 的交集

當 WHERE 條件有兩個欄位，兩個欄位都有 index 時：

```sql
-- 確認 city 也有 index
CREATE INDEX IF NOT EXISTS idx_users_city ON users(city);
ANALYZE users;

-- 兩個條件都有 index
EXPLAIN SELECT * FROM users WHERE age = 30 AND city = 'Taipei';
```

```
Bitmap Heap Scan on users
  Recheck Cond: ((age = 30) AND (city = 'Taipei'))
  ->  BitmapAnd
        ->  Bitmap Index Scan on idx_users_age
              Index Cond: (age = 30)
        ->  Bitmap Index Scan on idx_users_city
              Index Cond: (city = 'Taipei')
```

**BitmapAnd 流程**：
```
Bitmap A（age = 30）：  0 1 0 1 0 0 1 ...
Bitmap B（city = 'Taipei'）：  0 1 1 0 0 1 1 ...

AND 運算結果：           0 1 0 0 0 0 1 ...
                              ↑           ↑
                         只有這兩個 page 同時符合兩個條件
```

---

## 4-6 BitmapOr：兩個 index 的聯集

```sql
EXPLAIN SELECT * FROM users WHERE age = 20 OR city = 'Taipei';
```

```
Bitmap Heap Scan on users
  Recheck Cond: ((age = 20) OR (city = 'Taipei'))
  ->  BitmapOr
        ->  Bitmap Index Scan on idx_users_age
        ->  Bitmap Index Scan on idx_users_city
```

OR 條件自動合併兩個 index 的結果，避免 Seq Scan。

---

## 4-7 Bitmap Scan vs Index Scan 的邊界

調整查詢範圍，觀察 Planner 在什麼時候切換：

```sql
-- 很小的範圍（1 歲）→ Index Scan
EXPLAIN SELECT * FROM users WHERE age = 18;

-- 中等範圍（幾歲）→ Bitmap Scan
EXPLAIN SELECT * FROM users WHERE age BETWEEN 20 AND 25;

-- 大範圍（一半）→ Seq Scan
EXPLAIN SELECT * FROM users WHERE age >= 18 AND age <= 48;
```

---

## 本章練習

1. 建立 `status` 欄位 index 在 orders 表：`CREATE INDEX idx_orders_status ON orders(status);`
2. 查詢 `WHERE status = 'paid'`，觀察是哪種 scan（約 25% 的資料）
3. 把 `work_mem` 設成 `'1MB'`，再跑 `WHERE age BETWEEN 20 AND 30`，看看是否出現 `lossy`
4. 查詢 `WHERE status = 'paid' OR status = 'shipped'`，觀察是否出現 BitmapOr

---

## 本章小結

| 概念 | 重點 |
|------|------|
| Bitmap Index Scan | 建 bitmap（記位置），不讀 heap |
| Bitmap Heap Scan | 依 page 順序讀 heap，做 Recheck |
| exact | 記憶體夠，bit 對應 row |
| lossy | 記憶體不足，bit 對應 page，Recheck 更多 |
| BitmapAnd/Or | 多個 index 合併，AND/OR 條件 |

| 回傳比例 | 通常用的 scan |
|---------|-------------|
| < 1% | Index Scan |
| 1% ～ 20% | Bitmap Scan |
| > 20% | Seq Scan |

下一章：[Chapter 5：Join 類型](05_join_types.md)
