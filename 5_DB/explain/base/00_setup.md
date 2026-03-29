# Chapter 0：環境準備

## 目標
啟動 PostgreSQL，建立 100 萬筆 users + 500 萬筆 orders，準備好實驗環境。

---

## Step 1：啟動 Docker

```bash
cd /path/to/explain
docker compose up -d
```

首次啟動會自動執行 `setup.sql`，資料寫入約需 **2～3 分鐘**。

確認 log 出現這行代表完成：
```
LOG:  database system is ready to accept connections
```

```bash
# 查看 log
docker compose logs -f
# Ctrl+C 離開 log 追蹤
```

---

## Step 2：連線進去

```bash
psql -h localhost -U lab -d lab
# 密碼：lab
```

---

## Step 3：確認資料

```sql
SELECT COUNT(*) FROM users;
-- 應該是 1000000

SELECT COUNT(*) FROM orders;
-- 應該是 5000000
```

---

## Step 4：看一下表結構

```sql
\d users
\d orders
```

輸出：
```
               Table "public.users"
   Column   |            Type             |
------------+-----------------------------+
 id         | integer                     |
 name       | text                        |
 email      | text                        |
 age        | integer                     |
 city       | text                        |
 score      | numeric(10,2)               |
 created_at | timestamp without time zone |

Indexes:
    "users_pkey" PRIMARY KEY, btree (id)
    "idx_users_email" UNIQUE, btree (email)
```

**目前只有兩個 index：`id`（PK）和 `email`（unique）。**
其他欄位刻意不建 index，之後各章節再逐步加上，才能看到效果的變化。

---

## Step 5：了解實驗資料的分佈

```sql
-- age 分佈（18~78，大約均勻）
SELECT MIN(age), MAX(age), AVG(age)::INT FROM users;

-- city 分佈（5個城市，大致平均各 20 萬）
SELECT city, COUNT(*) FROM users GROUP BY city ORDER BY city;

-- orders status 分佈（4種，各約 25%）
SELECT status, COUNT(*) FROM orders GROUP BY status;
```

---

## 本章小結

| 表 | 筆數 | 現有 index |
|----|------|-----------|
| users | 100 萬 | id (PK), email (unique) |
| orders | 500 萬 | user_id (FK) 無 index |

環境準備好了，進入 [Chapter 1：認識 EXPLAIN 輸出結構](01_explain_structure.md)。
