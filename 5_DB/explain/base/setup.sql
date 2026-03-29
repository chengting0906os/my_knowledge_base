-- ============================================================
-- EXPLAIN/ANALYZE Lab - 資料建置
-- ============================================================

-- 1. users 表：100萬筆，模擬大表
CREATE TABLE users (
    id         SERIAL PRIMARY KEY,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL,
    age        INT,
    city       TEXT,
    score      NUMERIC(10, 2),
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO users (name, email, age, city, score)
SELECT
    'user_' || i,
    'user_' || i || '@example.com',
    (random() * 60 + 18)::INT,
    (ARRAY['Taipei', 'Taichung', 'Kaohsiung', 'Tainan', 'Hsinchu'])[ceil(random() * 5)],
    (random() * 1000)::NUMERIC(10, 2)
FROM generate_series(1, 1000000) AS i;

-- 2. orders 表：500萬筆，外鍵關聯 users
CREATE TABLE orders (
    id         SERIAL PRIMARY KEY,
    user_id    INT NOT NULL REFERENCES users(id),
    amount     NUMERIC(10, 2),
    status     TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO orders (user_id, amount, status)
SELECT
    (random() * 999999 + 1)::INT,
    (random() * 5000)::NUMERIC(10, 2),
    (ARRAY['pending', 'paid', 'shipped', 'cancelled'])[ceil(random() * 4)]
FROM generate_series(1, 5000000);

-- 3. 只在 users.email 上建 unique index（刻意不建其他 index，方便示範 Seq Scan）
CREATE UNIQUE INDEX idx_users_email ON users(email);

-- 4. 更新統計資訊
ANALYZE users;
ANALYZE orders;
