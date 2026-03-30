# SQL 筆試練習題

> 題型參考：給資料表，手寫 SQL，考總和、最大值、排序、條件篩選

---

## 資料表

**stores**

| store_id | store_name | region |
|---|---|---|
| 1 | 台北信義店 | 北部 |
| 2 | 台北內湖店 | 北部 |
| 3 | 新北板橋店 | 北部 |
| 4 | 桃園中壢店 | 中部 |
| 5 | 台中西屯店 | 中部 |
| 6 | 台中北屯店 | 中部 |
| 7 | 台南東區店 | 南部 |
| 8 | 高雄左營店 | 南部 |
| 9 | 高雄鳳山店 | 南部 |
| 10 | 宜蘭羅東店 | 東部 |

**sales**

| sale_id | store_id | amount | sale_date |
|---|---|---|---|
| 1 | 1 | 120000.00 | 2024-01-15 |
| 2 | 1 | 85000.00 | 2024-03-20 |
| 3 | 1 | 95000.00 | 2023-11-05 |
| 4 | 2 | 210000.00 | 2024-02-10 |
| 5 | 2 | 73000.00 | 2024-07-30 |
| 6 | 3 | 150000.00 | 2024-04-01 |
| 7 | 3 | 60000.00 | 2023-12-25 |
| 8 | 4 | 45000.00 | 2024-05-18 |
| 9 | 4 | 38000.00 | 2024-08-09 |
| 10 | 5 | 320000.00 | 2024-01-22 |
| 11 | 5 | 99000.00 | 2024-06-14 |
| 12 | 5 | 115000.00 | 2023-09-30 |
| 13 | 6 | 88000.00 | 2024-03-03 |
| 14 | 6 | 72000.00 | 2024-10-11 |
| 15 | 7 | 195000.00 | 2024-02-28 |
| 16 | 7 | 55000.00 | 2023-08-17 |
| 17 | 8 | 270000.00 | 2024-01-08 |
| 18 | 8 | 130000.00 | 2024-09-25 |
| 19 | 9 | 91000.00 | 2024-04-30 |
| 20 | 9 | 67000.00 | 2023-07-12 |
| 21 | 8 | 134000.00 | 2024-11-01 |

> 門市 10（宜蘭羅東店）無任何銷售記錄
> 台中西屯店與高雄左營店總額皆為 534,000（並列第一），用於 Q2-進階

---

## 題目

### Q1. 計算每間門市的總銷售額，依總銷售額由高到低排序
```sql
SELECT st.store_name, SUM(sa.amount) as amount
FROM stores st
JOIN sales sa ON st.store_id = sa.store_id
GROUP BY st.store_name
ORDER BY amount DESC


```

---

### Q2. 找出銷售額最高的那間門市
```sql
SELECT st.store_name, SUM(sa.amount) as amount
FROM stores st
JOIN sales sa ON st.store_id = sa.store_id
GROUP BY st.store_name
ORDER BY amount DESC
LIMIT 1
```


### Q2-進階. 找出銷售額最高的門市（若有並列第一，全部顯示）
```sql
SELECT store_name, amount
FROM (
    SELECT
        st.store_name,
        SUM(sa.amount) AS amount,
        RANK() OVER (ORDER BY SUM(sa.amount) DESC) AS rk
    FROM stores st
    JOIN sales sa ON st.store_id = sa.store_id
    GROUP BY st.store_name
) t
WHERE rk = 1;
```

---

### Q3. 找出總銷售額大於 100,000 的門市有幾間
```sql
SELECT COUNT(*) AS store_count
FROM (
    SELECT st.store_name
    FROM stores st
    JOIN sales sa ON st.store_id = sa.store_id
    GROUP BY st.store_name
    HAVING SUM(sa.amount) > 100000
    ) t
```

---

### Q4. 列出每間門市的總銷售額，以及在所有門市中的排名
```sql
SELECT 
    st.store_name, 
    SUM(sa.amount) as amount,
    RANK() OVER (ORDER BY SUM(sa.amount) DESC) AS rank
FROM stores st
JOIN sales sa ON st.store_id = sa.store_id
GROUP BY st.store_name
ORDER BY rank DESC
```

---

### Q5. 找出每個地區（region）銷售額最高的門市
```sql
SELECT *
FROM
    ( SELECT 
    st.store_name, 
    st.region, 
    SUM(sa.amount) as amount,
    RANK() OVER (PARTITION BY st.region ORDER BY SUM(sa.amount) DESC) as rk
    FROM stores st
    JOIN sales sa ON st.store_id = sa.store_id
    GROUP BY st.store_name, st.region
    ORDER BY amount DESC) t
WHERE rk = 1
```

---

### Q6. 計算每間門市 2024 年的總銷售額，沒有銷售記錄的門市也要顯示（顯示 0）
```sql
SELECT st.store_name, COALESCE(SUM(sa.amount), 0) as amount
FROM stores st
LEFT JOIN sales sa ON st.store_id = sa.store_id
GROUP BY st.store_name
ORDER BY amount DESC

```

---

### Q7. 計算每間門市的平均單筆銷售額，依平均由高到低排序
```sql
SELECT st.store_name, COALESCE(AVG(sa.amount), 0) as amount
FROM stores st
LEFT JOIN sales sa ON st.store_id = sa.store_id
GROUP BY st.store_name
ORDER BY amount DESC


```

---

### Q8. 找出單筆銷售額最高的那筆（回傳門市名稱、金額、日期）
```sql
SELECT * FROM
    (
    SELECT 
        st.store_name, 
        sa.amount,
        sa.sale_date,
        RANK() OVER (ORDER BY sa.amount DESC) as rk
    FROM stores st
    JOIN sales sa ON st.store_id = sa.store_id
    ) t
WHERE rk = 1
```

---

### Q9. 找出 2024 年有銷售但 2023 年沒有銷售的門市
```sql
SELECT DISTINCT st.store_name
FROM stores st
JOIN sales sa ON st.store_id = sa.store_id
WHERE EXTRACT(YEAR FROM sa.sale_date) = 2024

EXCEPT

SELECT DISTINCT st.store_name
FROM stores st
JOIN sales sa ON st.store_id = sa.store_id
WHERE EXTRACT(YEAR FROM sa.sale_date) = 2023
```

---

### Q10. 找出銷售筆數超過 2 筆的門市
```sql
SELECT st.store_name, COUNT(*) AS cnt
FROM stores st
JOIN sales sa ON st.store_id = sa.store_id
GROUP BY st.store_name
HAVING COUNT(*) >= 3


```

---

### Q11. 列出所有門市以及最近一筆銷售的日期（沒有銷售記錄的門市顯示 NULL）
```sql
SELECT st.store_name, MAX(sa.sale_date)
FROM stores st
LEFT JOIN sales sa ON st.store_id = sa.store_id
GROUP BY st.store_name

```

---

### Q12. 計算所有銷售記錄的總筆數
```sql
SELECT COUNT(*) AS cnt FROM sales;


```

---

### Q12-進階. 列出每間門市的銷售筆數，沒有銷售記錄的門市顯示 0（不能顯示 1）
```sql
SELECT st.store_name, COUNT(sa.sale_id) AS cnt
FROM stores st
LEFT JOIN sales sa ON st.store_id = sa.store_id
GROUP BY st.store_name
ORDER BY cnt DESC;
```

> 提示：`COUNT(*)` 會把 NULL row 算進去，要改用 `COUNT(欄位)` 才會忽略 NULL

---

### Q13. 計算全部銷售的平均金額、最高金額、最低金額（一次查出來）
```sql
SELECT st.store_name, COALESCE(AVG(sa.amount), 0), COALESCE(MAX(sa.amount), 0), COALESCE(MIN(sa.amount), 0)
FROM stores st
LEFT JOIN sales sa ON st.store_id = sa.store_id
GROUP BY st.store_name
```

---

### Q14. 計算每個地區（region）的總銷售額與門市數量
```sql
SELECT st.region, COUNT(st.store_name), COALESCE(SUM(sa.amount), 0)
FROM stores st
LEFT JOIN sales sa ON st.store_id = sa.store_id
GROUP BY  st.region
```

---

### Q15. 找出銷售筆數最多的門市
```sql
SELECT store_name, cnt
FROM (
    SELECT  st.store_name, 
            COUNT(sa.sale_id) as cnt,
            RANK() OVER (ORDER BY COUNT(sa.sale_id) DESC) AS rk
    FROM stores st
    LEFT JOIN sales sa ON st.store_id = sa.store_id
    GROUP BY st.store_name ) t
WHERE rk = 1;
```

---

### Q16. 列出 2023 年和 2024 年都有銷售記錄的門市（用 INTERSECT）
```sql
SELECT DISTINCT st.store_name
FROM stores st
JOIN sales sa ON st.store_id = sa.store_id
WHERE EXTRACT(YEAR FROM sa.sale_date) = 2023

INTERSECT

SELECT DISTINCT st.store_name
FROM stores st
JOIN sales sa ON st.store_id = sa.store_id
WHERE EXTRACT(YEAR FROM sa.sale_date) = 2024;
```

---

---

## 新資料表

**customers**

| customer_id | name | email | city | vip |
|---|---|---|---|---|
| 1 | 陳小明 | chen@example.com | 台北 | true |
| 2 | 林美華 | lin@example.com | 台中 | false |
| 3 | 王大偉 | wang@example.com | 高雄 | true |
| 4 | 張雅婷 | chang@example.com | 台北 | false |
| 5 | 李俊宏 | lee@example.com | 台南 | true |
| 6 | 黃淑芬 | huang@example.com | 新北 | false |
| 7 | 吳建志 | wu@example.com | 桃園 | false |
| 8 | 劉怡君 | liu@example.com | 台中 | true |
| 9 | 蔡明哲 | tsai@example.com | 高雄 | false |
| 10 | 鄭佳慧 | NULL | 宜蘭 | false |

**products**

| product_id | product_name | category | price | stock |
|---|---|---|---|---|
| 1 | 無線滑鼠 | 電腦周邊 | 599.00 | 150 |
| 2 | 機械鍵盤 | 電腦周邊 | 2499.00 | 80 |
| 3 | 27吋螢幕 | 電腦周邊 | 8900.00 | 30 |
| 4 | 筆記型電腦 | 電腦 | 35000.00 | 20 |
| 5 | 平板電腦 | 電腦 | 18000.00 | 45 |
| 6 | 藍牙耳機 | 音響 | 3200.00 | 60 |
| 7 | 喇叭 | 音響 | 4500.00 | 25 |
| 8 | 手機殼 | 配件 | 299.00 | 200 |
| 9 | 充電線 | 配件 | 199.00 | 500 |
| 10 | 停產商品 | 配件 | 0.00 | 0 |

---

### Q17. 找出所有 email 為 NULL 的顧客（用 IS NULL）
```sql
SELECT name, email
FROM customers
WHERE email is NULL;
```

---

### Q18. 找出名字包含「明」的顧客（用 LIKE）
```sql
SELECT name
FROM customers
WHERE name LIKE '%明%';

```

---

### Q19. 找出城市在台北或高雄的顧客（用 IN）
```sql
SELECT name 
FROM customers
WHERE city in ('台北', '高雄')

```

---

### Q20. 找出價格在 1000 到 10000 之間的商品（用 BETWEEN）
```sql
SELECT product_name
FROM products
WHERE price BETWEEN 1000 and 10000;

```

---

### Q21. 列出所有商品，並用 CASE WHEN 標註價格等級（低於 500 為「低」、500~5000 為「中」、5000 以上為「高」）
```sql
SELECT
    product_name,
    price,
    CASE
        WHEN price < 500 THEN '低'
        WHEN price BETWEEN 500 AND 5000 THEN '中'
        WHEN price > 5000 THEN '高'
    END AS price_level
FROM products;

```

---

### Q22. 列出所有顧客，email 為 NULL 的顯示「未填寫」（用 COALESCE）
```sql
SELECT name, COALESCE(email, '未填寫')
FROM customers;

```

---

### Q23. 找出有庫存（stock > 0）且屬於「電腦周邊」或「電腦」類別的商品
```sql
SELECT product_name, category
FROM products
WHERE category in ('電腦周邊', '電腦');

```

---

### Q24. 列出所有顧客的 email 和所有供應商的 email，去除重複（用 UNION）
```sql
SELECT email FROM customers
UNION
SELECT email FROM suppliers;

```

---

### Q25. 列出所有顧客的 email 和所有供應商的 email，保留重複（用 UNION ALL）
```sql
SELECT email FROM customers
UNION ALL
SELECT email FROM suppliers;

```

---

### Q26. UNION 和 UNION ALL 的差異是什麼？
```
UNION     → 合併兩個查詢結果，自動去除重複列（會做 DISTINCT）
UNION ALL → 合併兩個查詢結果，保留所有列（含重複）

效能：UNION ALL 較快，因為不需要額外排序去重
使用時機：
  - 確定不會有重複，或重複是需要的 → UNION ALL
  - 需要去重 → UNION
```

---

### Q27. 找出既是顧客又是供應商的 email（兩表交集概念，用 UNION ALL + GROUP BY 模擬）
```sql
SELECT email
FROM (
    SELECT email FROM customers
    UNION ALL
    SELECT email FROM suppliers
) combined
GROUP BY email
HAVING COUNT(*) > 1;

```

---

### Q28. 列出顧客名單與供應商名單，並標註來源（用 UNION ALL + 常數欄位）
```sql
SELECT name, '顧客' AS source FROM customers
UNION ALL
SELECT name, '供應商' AS source FROM suppliers;

```




---

### Q29. 顯示每個部門名稱及員工人數，只顯示人數超過 5 人的部門，依人數由高到低排序（JOIN + COUNT + HAVING）

表結構：
- `employees(employee_id, name, department_id, salary)`
- `departments(department_id, department_name, location)`

```sql
SELECT d.department_name,
       COUNT(e.employee_id) AS employee_count
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING COUNT(e.employee_id) > 5
ORDER BY employee_count DESC;

```

---

### Q30. 找出薪資高於公司整體平均薪資的員工，顯示 NAME 和 SALARY，依薪資由高到低排序（子查詢 Subquery）

表結構：`employees(employee_id, name, salary, manager_id)`

```sql
SELECT NAME, SALARY
FROM EMPLOYEES
WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEES)
ORDER BY SALARY DESC;
```