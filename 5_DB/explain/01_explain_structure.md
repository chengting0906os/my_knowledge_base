# Chapter 1：認識 EXPLAIN 輸出結構

## 目標
能夠看懂 EXPLAIN 輸出的每一個欄位，知道 cost、rows、width 各代表什麼。

---

## 1-1 最基本的用法

先執行一個最簡單的查詢，只讀一筆資料：

```sql
EXPLAIN SELECT * FROM users WHERE id = 1;
```

你會看到：
```
Index Scan using users_pkey on users  (cost=0.42..8.44 rows=1 width=58)
  Index Cond: (id = 1)
```

現在先不管 Index Scan 是什麼（後面章節會詳細說），我們專注在**括號裡的數字**。

---

## 1-2 cost 是什麼

```
cost=0.42..8.44
      ↑      ↑
  startup  total
```

- **startup cost（0.42）**：回傳「第一筆」資料之前，需要花費多少代價
- **total cost（8.44）**：回傳「所有」資料的總代價
- 單位是**抽象的代價單位**，不是毫秒，但數字越小越好

**startup cost 什麼時候會很大？**
排序（Sort）需要把所有資料讀完才能輸出第一筆，所以 startup cost 會接近 total cost：

```sql
EXPLAIN SELECT * FROM users ORDER BY age;
```

```
Sort  (cost=137014.84..139514.84 rows=1000000 width=58)
  Sort Key: age
  ->  Seq Scan on users  (cost=0.00..18334.00 rows=1000000 width=58)
```

注意 Sort 節點：`137014.84..139514.84`，startup 幾乎等於 total，代表排完才輸出。

---

## 1-3 rows 與 width

```
rows=1 width=58
```

- **rows**：Planner **預估**會回傳幾列（不是實際值！）
- **width**：每列平均佔幾個 bytes

width 可以幫你估計查詢傳回的資料量：
```
rows=1000000 × width=58 bytes ≈ 58 MB
```

---

## 1-4 樹狀結構與執行順序

EXPLAIN 的輸出是一棵樹，**縮排越深的節點越先執行**。

```sql
EXPLAIN
SELECT u.name, o.amount
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE u.id = 1;
```

輸出（大致如下）：
```
Nested Loop  (cost=0.98..25.08 rows=5 width=46)          ← 3. 最後執行
  ->  Index Scan on users  (cost=0.42..8.44 rows=1 ...)   ← 1. 先執行
        Index Cond: (id = 1)
  ->  Index Scan on orders (cost=0.56..16.58 rows=5 ...)  ← 2. 每次外層回一筆就執行一次
        Index Cond: (user_id = 1)
```

**閱讀技巧**：
1. 找最深縮排的節點 → 從那裡開始讀
2. 往上走就是資料流向（子節點的輸出傳給父節點）

---

## 1-5 EXPLAIN 不執行 vs EXPLAIN ANALYZE 真的執行

```sql
-- 只產生計畫，不執行
EXPLAIN SELECT * FROM users WHERE age = 30;

-- 真的執行，顯示實際時間與筆數
EXPLAIN ANALYZE SELECT * FROM users WHERE age = 30;
```

加了 ANALYZE 之後，每個節點多出一行：
```
Seq Scan on users  (cost=0.00..24846.00 rows=16529 width=58)
                   (actual time=0.023..189.451 rows=16642 loops=1)
  Filter: (age = 30)
  Rows Removed by Filter: 983358

Planning Time: 0.123 ms
Execution Time: 193.456 ms
```

新出現的欄位：

| 欄位 | 意義 |
|------|------|
| `actual time=0.023..189.451` | 實際 startup time .. total time（**毫秒**） |
| `rows=16642` | 這個節點實際回傳幾列 |
| `loops=1` | 這個節點被執行幾次 |
| `Rows Removed by Filter` | 被 WHERE 條件過濾掉的列數 |
| `Planning Time` | Planner 思考查詢計畫花費的時間 |
| `Execution Time` | 查詢真正執行的時間 |

---

## 1-6 預估 vs 實際的差距

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE age = 30;
```

對比：
```
rows=16529   ← Planner 預估
rows=16642   ← 實際
```

這次差距很小，代表統計資訊準確。
如果差距很大（預估 100，實際 50000），代表統計過期，需要執行：

```sql
ANALYZE users;
```

---

## 1-7 各種 EXPLAIN 選項

```sql
-- 加上 BUFFERS（看 cache 命中率，需配合 ANALYZE）
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE age = 30;

-- 輸出 JSON 格式（適合程式解析）
EXPLAIN (ANALYZE, FORMAT JSON) SELECT * FROM users WHERE age = 30;

-- 最完整
EXPLAIN (ANALYZE, BUFFERS, VERBOSE) SELECT * FROM users WHERE age = 30;
```

> ⚠️ **重要**：`EXPLAIN ANALYZE` 會真的執行查詢，包含 INSERT/UPDATE/DELETE。
> 寫入操作請用 transaction 包住：
> ```sql
> BEGIN;
> EXPLAIN ANALYZE DELETE FROM orders WHERE status = 'cancelled';
> ROLLBACK;  -- 不要真的刪掉
> ```

---

## 本章練習

1. 執行 `EXPLAIN SELECT * FROM users WHERE city = 'Taipei';`，說出 cost、rows、width 各是多少
2. 執行 `EXPLAIN ANALYZE SELECT * FROM users WHERE city = 'Taipei';`，比較預估 rows 和實際 rows
3. 從 `Rows Removed by Filter` 反推：如果有 20 萬筆被過濾掉，代表它讀了多少筆？

---

## 本章小結

| 概念 | 重點 |
|------|------|
| cost | 抽象代價，不是毫秒，startup..total |
| rows | Planner 預估，可能不準 |
| actual rows | 真實值，需要 ANALYZE 才看到 |
| loops | 節點被執行幾次（Nested Loop 內層常 > 1） |
| 執行順序 | 縮排最深的先執行 |

下一章：[Chapter 2：Sequential Scan](02_seq_scan.md)
