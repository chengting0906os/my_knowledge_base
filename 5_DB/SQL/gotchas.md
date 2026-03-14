# SQL Gotchas

## NULL 比較必須獨立寫

`NULL` 無法用 `!=`、`=` 比較，必須用 `IS NULL` / `IS NOT NULL`。

```sql
-- ❌ 錯誤：NULL != 2 不會 match NULL，結果會漏掉 referee_id 為 NULL 的列
WHERE referee_id != 2

-- ✅ 正確：要明確加上 IS NULL
WHERE referee_id != 2 OR referee_id IS NULL
```

> 原因：在 SQL 中，任何與 NULL 的比較（`NULL = 2`、`NULL != 2`）結果都是 `UNKNOWN`，不是 `TRUE`，所以不會被 WHERE 選到。

## DISTINCT

去除重複列，作用在 SELECT 的所有欄位組合。

```sql
-- 單欄：去除重複的 city
SELECT DISTINCT city FROM Customer

-- 多欄：去除 (city, country) 組合重複，不是單獨去重
SELECT DISTINCT city, country FROM Customer
```

**常見用法：**

```sql
-- 搭配 COUNT
SELECT COUNT(DISTINCT customer_id) FROM Orders

-- ❌ 這樣不對，DISTINCT 只能放在最前面
SELECT customer_id, COUNT(DISTINCT) FROM Orders
```

> DISTINCT 對 NULL 的處理：多個 NULL 視為相同，只保留一個。

## SELECT 語法順序

```sql
-- ❌ 錯誤
SELECT name WHERE age > 18 FROM Users

-- ✅ 正確
SELECT name FROM Users WHERE age > 18
```

> 固定順序：`SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY`

## 比較運算子

```sql
-- ❌ 錯誤：SQL 不用 ==，也不用雙引號
WHERE low_fats == "Y"

-- ✅ 正確
WHERE low_fats = 'Y'
```

## ORDER BY 必須指定欄位

```sql
-- ❌ 錯誤
ORDER BY ASC

-- ✅ 正確
ORDER BY id ASC
```

## JOIN 條件用 ON，不是 WHERE

```sql
-- ❌ 錯誤
FROM Employees AS a
LEFT JOIN EmployeeUNI AS b WHERE a.id = b.id

-- ✅ 正確
FROM Employees AS a
LEFT JOIN EmployeeUNI AS b ON a.id = b.id
```

## MySQL 不支援 FULL JOIN / OUTER JOIN

```sql
-- ❌ MySQL 不支援
FULL JOIN ...
OUTER JOIN ...

-- ✅ 改用 LEFT JOIN 或 RIGHT JOIN
LEFT JOIN ...
```

## Ambiguous Column：兩表同名欄位要加前綴

```sql
-- ❌ 錯誤：visit_id 在兩張表都有
COUNT(visit_id)

-- ✅ 正確：指定來自哪張表
COUNT(v.visit_id)
```

## 使用聚合函數必須搭配 GROUP BY

```sql
-- ❌ 錯誤：COUNT 沒有 GROUP BY，會把所有人合併成一列
SELECT customer_id, COUNT(visit_id)
FROM Visits

-- ✅ 正確
SELECT customer_id, COUNT(visit_id) AS count_no_trans
FROM Visits
GROUP BY customer_id
```

> 規則：SELECT 裡有 `COUNT / SUM / AVG / MAX / MIN`，其他非聚合欄位都要放進 `GROUP BY`。
