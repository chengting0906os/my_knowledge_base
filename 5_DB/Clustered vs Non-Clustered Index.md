# Clustered vs Secondary Index:

## MySQL

主鍵索引（Clustered Index）葉節點直接存整筆資料
Secondary Index 儲存「索引鍵 + 主鍵 ID」，查完整資料要再回主鍵索引

- Hash Index：主要用於 `MEMORY/NDB` 這類引擎（`USING HASH`）
  只適合等值查詢（`=`），不適合範圍查詢與排序
  InnoDB 一般索引仍是 B+Tree（另有內部的 Adaptive Hash Index，不是手動建的）

## PostgreSQL

- 都是 Secondary Index（包含 PK 索引）
  資料本體放在 Heap Table，索引只存 key + TID（Tuple ID，指到 heap 資料列）
  因此不像 MySQL 存在性能差異，插入數據時可以直接添加到 heap table 的末尾

- Hash Index：可用 `USING HASH` 建立，主要加速等值查詢（`=`）
  不支援範圍查詢/排序，實務上通用場景仍常用 B-tree

  ```sql
  CREATE INDEX idx_users_email_hash ON users USING HASH (email);
  ```

- GIN 是倒排索引（Inverted Index）：是「index key / token -> 多筆 TID」，不是「一筆資料 -> 一個 index key」
  類比像書本最後的關鍵字索引：先找關鍵字，再拿到很多頁碼（TID）
  - `array`、`jsonb`、全文檢索（`tsvector`）都適合用 GIN

- GiST（Generalized Search Tree）是可擴充索引框架：可依 operator class 支援不同資料型別，不是單一固定結構
  常用在幾何/空間資料、範圍型別，也常用於最近鄰查詢（KNN，`ORDER BY <->`）
  - 當查詢不是單純等值或一般範圍，而是「距離最近、是否重疊、是否包含」時，常考慮 GiST

- Partial Index（部分索引）：只索引「符合條件」的資料列，不是整張表都建索引
  常見用法：只對有效資料建索引，讓索引更小、查詢更快

  ```sql
  CREATE INDEX idx_users_active_email
  ON users (email)
  WHERE deleted_at IS NULL;
  ```

  重點：查詢條件要包含（或可推導出）`WHERE deleted_at IS NULL`，規劃器才會用到這顆索引

- Expression Index（表達式索引）：索引欄位不一定是原始欄位，也可以是函數或 scalar expression 的計算結果
  適用場景：你常用「運算後的值」查詢，例如不分大小寫、字串拼接、日期函數
  ```sql
  -- 不分大小寫查詢
  CREATE INDEX test1_lower_col1_idx ON test1 (lower(col1));
  SELECT * FROM test1 WHERE lower(col1) = 'value';
  ```
  ```sql
  -- 常查 full name
  CREATE INDEX people_names ON people ((first_name || ' ' || last_name));
  SELECT * FROM people WHERE (first_name || ' ' || last_name) = 'John Smith';
  ```
  UNIQUE 也可用在表達式索引，可強制「邏輯唯一」，
  例如 `UNIQUE (lower(email))` 可避免 `A@x.com` 與 `a@x.com` 同時存在
  成本：INSERT/UPDATE 時要重算表達式，寫入成本較高；讀取時可直接走索引，查詢很快

## Reference

-  