-- 門市
CREATE TABLE stores (
    store_id   INT PRIMARY KEY,
    store_name VARCHAR(100),
    region     VARCHAR(50)
);

-- 銷售記錄
CREATE TABLE sales (
    sale_id    INT PRIMARY KEY,
    store_id   INT REFERENCES stores(store_id),
    amount     NUMERIC(10,2),
    sale_date  DATE
);

-- 假資料：門市
INSERT INTO stores VALUES
(1,  '台北信義店',   '北部'),
(2,  '台北內湖店',   '北部'),
(3,  '新北板橋店',   '北部'),
(4,  '桃園中壢店',   '中部'),
(5,  '台中西屯店',   '中部'),
(6,  '台中北屯店',   '中部'),
(7,  '台南東區店',   '南部'),
(8,  '高雄左營店',   '南部'),
(9,  '高雄鳳山店',   '南部'),
(10, '宜蘭羅東店',   '東部');

-- 假資料：銷售記錄（含 2023、2024 年，門市 10 無任何銷售）
INSERT INTO sales VALUES
(1,  1, 120000.00, '2024-01-15'),
(2,  1,  85000.00, '2024-03-20'),
(3,  1,  95000.00, '2023-11-05'),
(4,  2, 210000.00, '2024-02-10'),
(5,  2,  73000.00, '2024-07-30'),
(6,  3, 150000.00, '2024-04-01'),
(7,  3,  60000.00, '2023-12-25'),
(8,  4,  45000.00, '2024-05-18'),
(9,  4,  38000.00, '2024-08-09'),
(10, 5, 320000.00, '2024-01-22'),
(11, 5,  99000.00, '2024-06-14'),
(12, 5, 115000.00, '2023-09-30'),
(13, 6,  88000.00, '2024-03-03'),
(14, 6,  72000.00, '2024-10-11'),
(15, 7, 195000.00, '2024-02-28'),
(16, 7,  55000.00, '2023-08-17'),
(17, 8, 270000.00, '2024-01-08'),
(18, 8, 130000.00, '2024-09-25'),
(19, 9,  91000.00, '2024-04-30'),
(20, 9,  67000.00, '2023-07-12'),
(21, 8, 134000.00, '2024-11-01'); -- 讓高雄左營店與台中西屯店並列第一（皆為 534000），用於測試 Q2-進階
-- 門市 10（宜蘭羅東店）無任何銷售記錄，用於測試 LEFT JOIN

-- 顧客
CREATE TABLE customers (
    customer_id   INT PRIMARY KEY,
    name          VARCHAR(100),
    email         VARCHAR(100),
    city          VARCHAR(50),
    vip           BOOLEAN DEFAULT FALSE
);

-- 商品
CREATE TABLE products (
    product_id    INT PRIMARY KEY,
    product_name  VARCHAR(100),
    category      VARCHAR(50),
    price         NUMERIC(10,2),
    stock         INT
);

-- 假資料：顧客
INSERT INTO customers VALUES
(1,  '陳小明', 'chen@example.com',   '台北', TRUE),
(2,  '林美華', 'lin@example.com',    '台中', FALSE),
(3,  '王大偉', 'wang@example.com',   '高雄', TRUE),
(4,  '張雅婷', 'chang@example.com',  '台北', FALSE),
(5,  '李俊宏', 'lee@example.com',    '台南', TRUE),
(6,  '黃淑芬', 'huang@example.com',  '新北', FALSE),
(7,  '吳建志', 'wu@example.com',     '桃園', FALSE),
(8,  '劉怡君', 'liu@example.com',    '台中', TRUE),
(9,  '蔡明哲', 'tsai@example.com',   '高雄', FALSE),
(10, '鄭佳慧', NULL,                 '宜蘭', FALSE); -- email 為 NULL，用於測試 IS NULL

-- 假資料：商品
INSERT INTO products VALUES
(1,  '無線滑鼠',     '電腦周邊', 599.00,  150),
(2,  '機械鍵盤',     '電腦周邊', 2499.00,  80),
(3,  '27吋螢幕',     '電腦周邊', 8900.00,  30),
(4,  '筆記型電腦',   '電腦',     35000.00, 20),
(5,  '平板電腦',     '電腦',     18000.00, 45),
(6,  '藍牙耳機',     '音響',     3200.00,  60),
(7,  '喇叭',         '音響',     4500.00,  25),
(8,  '手機殼',       '配件',     299.00,  200),
(9,  '充電線',       '配件',     199.00,  500),
(10, '停產商品',     '配件',     0.00,      0); -- 庫存為 0，用於測試條件篩選

-- 供應商
CREATE TABLE suppliers (
    supplier_id  INT PRIMARY KEY,
    name         VARCHAR(100),
    email        VARCHAR(100),
    city         VARCHAR(50)
);

-- 假資料：供應商（email 刻意與顧客有兩筆重複，用於測試 UNION vs UNION ALL）
INSERT INTO suppliers VALUES
(1, '科技貿易有限公司',   'chen@example.com',      '台北'),  -- 與顧客 email 重複
(2, '台灣電子供應商',     'supplier2@biz.com',     '新竹'),
(3, '全球零件股份公司',   'global@parts.com',      '台中'),
(4, '精品配件行',         'lee@example.com',       '台南'),  -- 與顧客 email 重複
(5, '南台灣物流公司',     'southlogistic@biz.com', '高雄');

-- 部門
CREATE TABLE departments (
    department_id    INT PRIMARY KEY,
    department_name  VARCHAR(100),
    location         VARCHAR(50)
);

-- 員工
CREATE TABLE employees (
    employee_id    INT PRIMARY KEY,
    name           VARCHAR(100),
    department_id  INT REFERENCES departments(department_id),
    salary         DECIMAL(10,2)
);

-- 假資料：部門
INSERT INTO departments VALUES
(1, '工程部', '台北'),
(2, '業務部', '台中'),
(3, '行銷部', '台北'),
(4, '人資部', '高雄'),
(5, '財務部', '台北');

-- 假資料：員工（工程部 7 人、業務部 6 人、行銷部 4 人、人資部 3 人、財務部 2 人）
-- HAVING > 5 應只顯示工程部(7)與業務部(6)
INSERT INTO employees VALUES
( 1, '王小明',  1, 85000),
( 2, '陳大華',  1, 92000),
( 3, '林志偉',  1, 78000),
( 4, '張怡君',  1, 95000),
( 5, '吳建宏',  1, 88000),
( 6, '劉美玲',  1, 72000),
( 7, '蔡俊賢',  1, 80000),
( 8, '黃淑芬',  2, 65000),
( 9, '鄭佳慧',  2, 70000),
(10, '許明哲',  2, 68000),
(11, '謝雅婷',  2, 73000),
(12, '周建志',  2, 66000),
(13, '盧怡萍',  2, 71000),
(14, '江雨蓁',  3, 60000),
(15, '方柏翰',  3, 58000),
(16, '石宜臻',  3, 62000),
(17, '葉庭語',  3, 59000),
(18, '賴冠霖',  4, 55000),
(19, '邱品蓉',  4, 57000),
(20, '潘子晴',  4, 54000),
(21, '洪睿哲',  5, 90000),
(22, '簡宛如',  5, 88000);
