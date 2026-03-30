# Database Interview Q&A List

## 基礎概念

1. What is ACID, and what does each property guarantee?
   什麼是 ACID？每個特性保證了什麼？
   <details>
   <summary>Answer</summary>

   | 特性 | 說明 |
   |---|---|
   | **Atomicity（原子性）** | 交易內所有操作要嘛全部成功，要嘛全部回滾，不存在部分完成 |
   | **Consistency（一致性）** | 交易前後，資料庫必須符合所有定義的規則（constraints、cascades） |
   | **Isolation（隔離性）** | 並發交易之間互不干擾，一個交易看不到另一個未提交的變更 |
   | **Durability（持久性）** | 交易提交後，即使系統崩潰，資料仍然保留（依靠 WAL/redo log） |

   </details>

2. What are the four transaction isolation levels, and what anomalies does each prevent?
   四種 Isolation Level 是什麼？各自防止哪些異常？
   <details>
   <summary>Answer</summary>

   | Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
   |---|---|---|---|
   | Read Uncommitted | 可能發生 | 可能發生 | 可能發生 |
   | Read Committed | 防止 | 可能發生 | 可能發生 |
   | Repeatable Read | 防止 | 防止 | 可能發生（MySQL InnoDB 靠 MVCC 防止）|
   | Serializable | 防止 | 防止 | 防止 |

   - **Dirty Read**：讀到另一個尚未 commit 的交易的資料
   - **Non-Repeatable Read**：同一筆資料在同一交易內讀兩次，結果不同
   - **Phantom Read**：同一個查詢在同一交易內跑兩次，第二次多出（或少了）幾筆資料

   </details>

3. What is MVCC, and how does it avoid lock contention?
   什麼是 MVCC？它如何避免鎖的競爭？
   <details>
   <summary>Answer</summary>

   **MVCC（Multi-Version Concurrency Control）**：為每筆資料保留多個版本，讀操作拿舊版本，寫操作建新版本，讀寫之間不互相阻塞。

   - 讀不阻寫、寫不阻讀
   - 每個交易有一個 snapshot（讀取時間點），只看在那個時間點之前已 commit 的資料
   - PostgreSQL 用 xmin/xmax 標記版本可見性；MySQL InnoDB 用 undo log 重建舊版本

   </details>

4. What is a deadlock, and how can it be prevented or detected?
   什麼是 Deadlock？如何預防或偵測？
   <details>
   <summary>Answer</summary>

   **Deadlock**：兩個（或多個）交易互相等待對方釋放鎖，形成循環等待，誰都無法繼續。

   **預防：**
   - 固定加鎖順序（所有交易都先鎖 A 再鎖 B）
   - 使用 `SELECT ... FOR UPDATE` 一次鎖定所有需要的資料
   - 縮短交易時間，減少持鎖時間

   **偵測與解除：**
   - DB 定期掃描 wait-for graph，發現環狀等待就選一個 victim 回滾
   - PostgreSQL/MySQL 都有內建 deadlock detection

   </details>

5. What is the difference between optimistic locking and pessimistic locking?
   樂觀鎖（Optimistic Locking）和悲觀鎖（Pessimistic Locking）差在哪？
   <details>
   <summary>Answer</summary>

   |  | 悲觀鎖 | 樂觀鎖 |
   |---|---|---|
   | 假設 | 衝突常發生，先鎖再操作 | 衝突少發生，操作完再驗證 |
   | 實作 | `SELECT ... FOR UPDATE` | version 欄位 + `WHERE version = ?` |
   | 適合 | 高競爭、寫多場景 | 低競爭、讀多場景 |
   | 代價 | 鎖等待，吞吐量低 | 衝突時需 retry |

   </details>

---

## 索引（Index）

6. What is a database index, and what are its benefits and costs?
   什麼是 Index？有什麼好處和代價？
   <details>
   <summary>Answer</summary>

   Index 是一種資料結構，讓 DB 不需掃描整張表就能快速找到資料。

   **好處：** SELECT/JOIN/WHERE/ORDER BY 加速，減少 I/O
   **代價：** 寫入（INSERT/UPDATE/DELETE）需同步維護索引、佔用磁碟空間、太多索引讓 Optimizer 選錯

   </details>

7. Why is B+ Tree good for databases? What makes it better than a binary search tree?
   B+ Tree 為什麼適合資料庫？比 BST 好在哪？
   <details>
   <summary>Answer</summary>

   - **低樹高**：B+ Tree 是多叉樹（每個節點可有幾百個子節點），相比 BST 高度遠低，磁碟 I/O 次數少
   - **Leaf Node 雙向連結**：支援 range scan（ORDER BY、BETWEEN），BST 做不到
   - **所有資料在 leaf**：inner node 只存 key，可在一個 disk page 放更多 key，減少 I/O
   - 節點大小設計為對齊磁碟 page（通常 4KB / 8KB / 16KB）

   </details>

8. What are the PostgreSQL index types, and when would you use each?
   PostgreSQL 有哪些 Index 類型？各自適合哪些場景？
   <details>
   <summary>Answer</summary>

   | 類型 | 適合場景 | 支援運算子 |
   |---|---|---|
   | **B-Tree**（預設） | 等值、範圍查詢 | `=` `<` `>` `BETWEEN` `LIKE 'abc%'` |
   | **Hash** | 純等值查詢 | `=` |
   | **GiST** | 空間資料、範圍型別（PostGIS） | `<<` `@>` `<@` |
   | **GIN** | 全文搜尋、陣列、JSONB | `<@` `@>` `&&` |
   | **BRIN** | 大型有序資料（時間戳、日誌） | `<` `>` `BETWEEN` |

   </details>

9. When does an index become ineffective?
   Index 在什麼情況下會失效？
   <details>
   <summary>Answer</summary>

   - **低基數欄位**（如 boolean、性別）：符合條件的列太多，全表掃描反而更快
   - **`LIKE '%keyword'`**：前綴萬用字元讓 B-Tree 無法使用
   - **對索引欄位套函數**：`WHERE LOWER(name) = 'foo'`（改用 functional index）
   - **資料表太小**：Optimizer 判斷 sequential scan 比 index lookup overhead 更快
   - **統計資料過時**：Optimizer 誤判選擇性，選了 full scan 而非 index scan

   </details>

10. What is the difference between a clustered index and a non-clustered index?
    Clustered Index 和 Non-Clustered Index 差在哪？
    <details>
    <summary>Answer</summary>

    | | Clustered Index | Non-Clustered Index |
    |---|---|---|
    | 資料存放 | 資料列本身按索引順序實體排列 | 索引是獨立結構，指向實體資料列 |
    | 數量 | 每張表只能有一個 | 可以有多個 |
    | 查詢速度 | range scan 最快（資料連續） | 需要額外 lookup（回表） |
    | PostgreSQL | 沒有傳統意義的 clustered index（用 CLUSTER 命令手動重排） | 所有 index 預設都是 non-clustered |
    | MySQL InnoDB | Primary Key 就是 clustered index | Secondary index leaf node 存 PK，再回 clustered index 查 |

    </details>

11. What is an Index Only Scan, and when does it happen?
    什麼是 Index Only Scan？什麼時候會觸發？
    <details>
    <summary>Answer</summary>

    當 SELECT 的欄位**全部都在 index 裡**時，DB 不需要讀原始 table，直接從 index 取值。

    ```sql
    CREATE INDEX idx_order_id ON orders (order_id);
    SELECT order_id FROM orders WHERE order_id > 100;
    -- 只讀 index，不碰 table → Index Only Scan
    ```

    PostgreSQL 還需要確認 visibility map（確認資料是否可見），若 visibility map 不夠新，仍需回 table。

    </details>

12. Why should you always use `CREATE INDEX CONCURRENTLY` in production?
    為什麼生產環境建索引一定要加 `CONCURRENTLY`？
    <details>
    <summary>Answer</summary>

    - 不加 `CONCURRENTLY`：建索引時鎖整張表，期間寫入被阻塞（生產環境不可接受）
    - 加 `CONCURRENTLY`：不鎖表，讀寫正常進行，但建索引需要更長時間（需掃描兩次）
    - 代價：不能在交易內使用、建立失敗會留下 invalid index 需手動清除

    </details>

---

## 查詢優化（Query Optimization）

13. What does `EXPLAIN ANALYZE` show, and how do you read it?
    `EXPLAIN ANALYZE` 顯示什麼？如何解讀？
    <details>
    <summary>Answer</summary>

    - `EXPLAIN`：顯示 Optimizer 規劃的執行計畫（估算值，不實際執行）
    - `EXPLAIN ANALYZE`：實際執行並顯示真實時間 vs 估算時間

    關鍵欄位：
    - `cost=0.00..8.27`：啟動成本..總成本（Optimizer 估算的 arbitrary unit）
    - `rows=100`：預估回傳行數
    - `actual time=0.1..5.2`：實際執行時間（ms）
    - `Seq Scan`：沒走 index；`Index Scan`：走了 index

    </details>

14. What is the N+1 query problem, and how do you fix it?
    什麼是 N+1 Query 問題？如何解決？
    <details>
    <summary>Answer</summary>

    查 N 筆資料後，對每筆再發一次查詢 → 共 N+1 次 DB 查詢。

    ```sql
    -- N+1 問題
    SELECT * FROM users;                        -- 1 次
    SELECT * FROM posts WHERE user_id = 1;      -- N 次（每個 user 一次）
    SELECT * FROM posts WHERE user_id = 2;
    ...

    -- 解法：JOIN 或 IN
    SELECT u.*, p.* FROM users u
    JOIN posts p ON p.user_id = u.id;           -- 1 次搞定
    ```

    ORM 解法：eager loading（Rails: `includes`，Django: `select_related` / `prefetch_related`）

    </details>

15. What are the different types of SQL JOINs?
    SQL JOIN 有哪些類型？
    <details>
    <summary>Answer</summary>

    | JOIN 類型 | 結果 |
    |---|---|
    | **INNER JOIN** | 只回傳兩表都有匹配的列 |
    | **LEFT JOIN** | 回傳左表全部 + 右表匹配的（右表無匹配補 NULL） |
    | **RIGHT JOIN** | 回傳右表全部 + 左表匹配的（左表無匹配補 NULL） |
    | **FULL OUTER JOIN** | 兩表全部，無匹配補 NULL |
    | **CROSS JOIN** | 笛卡兒積，每列互相配對 |
    | **SELF JOIN** | 同一張表 JOIN 自己（用別名） |

    </details>

16. What are the three SQL join strategies, and when does the Optimizer pick each?
    SQL 有哪三種 Join 執行策略？Optimizer 怎麼選？
    <details>
    <summary>Answer</summary>

    | 策略 | 適合場景 |
    |---|---|
    | **Nested Loop Join** | 小表 JOIN 大表，且大表有 index；outer table 小 |
    | **Hash Join** | 兩表都大、無 index；等值 JOIN |
    | **Merge Join** | 兩表都已排序或有排序索引；range JOIN |

    Optimizer 根據統計資料（rows、selectivity）估算成本，選最低的。

    </details>

17. What is query processing in SQL (parse → optimize → execute)?
    SQL 查詢處理的完整流程是什麼（parse → optimize → execute）？
    <details>
    <summary>Answer</summary>

    1. **Parser**：語法檢查、語意檢查，將 SQL 轉成 AST（Abstract Syntax Tree）
    2. **Shared Pool Check**：hash 命中 → Soft Parse（跳過 Optimizer）；未命中 → Hard Parse
    3. **Optimizer**：評估多種執行計畫（index scan vs seq scan、join 順序、join 策略），選最低成本的
    4. **Row Source Generator**：將計畫轉成可執行的 binary plan
    5. **Execution Engine**：執行計畫，從磁碟或 Buffer Cache 讀取資料，回傳結果

    </details>

---

## 正規化（Normalization）

18. What is database normalization, and what are 1NF, 2NF, 3NF?
    什麼是資料庫正規化？1NF、2NF、3NF 各是什麼？
    <details>
    <summary>Answer</summary>

    正規化是減少資料冗餘、提高一致性的設計過程。

    - **1NF**：每個欄位只有一個值（不存陣列、不存逗號分隔值）
    - **2NF**：在 1NF 基礎上，非 key 欄位必須完全依賴**整個** primary key（消除部分依賴）
    - **3NF**：在 2NF 基礎上，非 key 欄位不能依賴另一個非 key 欄位（消除遞移依賴）

    </details>

---

## 架構與擴展

19. What is the difference between SQL and NoSQL?
    SQL 和 NoSQL 的差異是什麼？
    <details>
    <summary>Answer</summary>

    | | SQL（RDBMS） | NoSQL |
    |---|---|---|
    | Schema | 固定結構 | 彈性（schema-less） |
    | ACID | 完整支援 | 通常最終一致性（部分支援） |
    | 擴展 | 垂直擴展（Scale Up）為主 | 水平擴展（Scale Out）為主 |
    | 查詢 | SQL，強大的 JOIN | 各家 API 不同，JOIN 受限 |
    | 適合 | 強一致性需求、複雜查詢 | 高吞吐、大量讀寫、schema 多變 |
    | 範例 | PostgreSQL、MySQL | MongoDB、Redis、Cassandra、DynamoDB |

    </details>

20. What is the difference between OLTP and OLAP?
    OLTP 和 OLAP 的差異是什麼？
    <details>
    <summary>Answer</summary>

    | | OLTP | OLAP |
    |---|---|---|
    | 用途 | 日常交易處理（下單、付款） | 分析、報表（月銷售、趨勢） |
    | 查詢特性 | 小量資料、高頻讀寫 | 大量資料、複雜聚合 |
    | 資料量 | 數 GB（Gigabyte） | 數 TB（Terabyte）~ PB（Petabyte） |
    | 優化方向 | 低延遲、高並發 | 高吞吐、Column Store |
    | 範例 | PostgreSQL、MySQL | Snowflake、BigQuery、Redshift |

    </details>

21. What is the difference between sharding and partitioning?
    Sharding 和 Partitioning 的差異是什麼？
    <details>
    <summary>Answer</summary>

    | | Partitioning | Sharding |
    |---|---|---|
    | 範圍 | 同一個 DB instance 內切分 | 切分到多個 DB instance（跨機器） |
    | 目的 | 提升查詢效率、管理方便 | 水平擴展，突破單機容量上限 |
    | 複雜度 | 低（DB 原生支援） | 高（應用層需處理路由） |
    | 跨分片查詢 | 簡單 | 困難（需 scatter-gather 或拒絕跨片 JOIN） |

    </details>

22. What is replication, and what are the risks of replication lag?
    什麼是 Replication？Replication Lag 有什麼風險？
    <details>
    <summary>Answer</summary>

    **Replication**：主節點（Primary）的資料變更同步到副本（Replica），用於讀寫分離、高可用。

    **Replication Lag**：Primary commit 到 Replica 收到之間的延遲。

    **風險：**
    - 讀 Replica 拿到舊資料（使用者剛更新，馬上查卻看到舊值）
    - Failover 時 Replica 可能遺失尚未同步的資料

    **對策：** 強一致性讀走 Primary；使用同步複製（性能代價）；應用層容忍最終一致性

    </details>

---

## 快取（Cache）

23. What is connection pooling, and why is it needed?
    什麼是 Connection Pooling？為什麼需要它？
    <details>
    <summary>Answer</summary>

    建立 DB 連線代價高（TCP 握手、身份驗證、記憶體分配），Connection Pool 預先建立一批連線並重複使用。

    - 沒有 pool：每個 request 建新連線 → 延遲高、DB 連線數爆炸
    - 有 pool：請求來時直接拿現成連線，用完還回去
    - 常見工具：PgBouncer（PostgreSQL）、HikariCP（Java）

    </details>

24. What are the three Redis cache failure patterns: cache penetration, cache avalanche, and cache breakdown?
    Redis 三大快取失效問題：Cache Penetration、Avalanche、Breakdown 各是什麼？如何解決？
    <details>
    <summary>Answer</summary>

    | 問題 | 原因 | 解法 |
    |---|---|---|
    | **Cache Penetration（穿透）** | 查詢不存在的 key，每次都打到 DB | Bloom Filter 過濾；快取空值（TTL 短） |
    | **Cache Avalanche（雪崩）** | 大量 key 同時過期，DB 被打爆 | TTL 加隨機抖動；熱點 key 永不過期 + 後台更新 |
    | **Cache Breakdown（擊穿）** | 一個熱點 key 過期，大量並發同時打 DB | 互斥鎖（mutex）；熱點 key 不設 TTL |

    </details>

---

## 進階

25. What is a WAL (Write-Ahead Log), and why is it critical for durability?
    什麼是 WAL（Write-Ahead Log）？為何對 Durability 至關重要？
    <details>
    <summary>Answer</summary>

    **WAL**：所有資料修改在實際寫入資料頁之前，先寫到順序日誌（WAL）。

    - 順序寫 WAL 比隨機寫資料頁快很多
    - crash 後，DB 用 WAL replay 恢復到 crash 前的狀態，保證 Durability
    - PostgreSQL WAL 同時用於 Replication（Replica 消費 WAL 跟上 Primary）

    </details>

26. What is an LSM-Tree, and how does it differ from a B+ Tree?
    LSM-Tree 是什麼？和 B+ Tree 有什麼不同？
    <details>
    <summary>Answer</summary>

    | | B+ Tree | LSM-Tree |
    |---|---|---|
    | 寫入 | 隨機 I/O（就地更新） | 順序 I/O（append-only，批次合併） |
    | 讀取 | 快（直接定位） | 較慢（可能需查多層 SSTable） |
    | 寫放大 | 較低 | 較高（compaction） |
    | 適合 | 讀多寫少（OLTP） | 寫多讀少（時序資料、日誌、KV store） |
    | 使用者 | PostgreSQL、MySQL | RocksDB、Cassandra、LevelDB |

    </details>

27. What is the difference between MySQL and PostgreSQL?
    MySQL 和 PostgreSQL 的主要差異是什麼？
    <details>
    <summary>Answer</summary>

    | | MySQL | PostgreSQL |
    |---|---|---|
    | MVCC 實作 | undo log（InnoDB） | 多版本資料列（xmin/xmax） |
    | JSON 支援 | 基本 | 強大（JSONB + GIN index） |
    | 全文搜尋 | 有限 | tsvector + GIN，更完整 |
    | Replication | Binary log（row/statement/mixed） | WAL streaming |
    | 授權 | GPL（有商業版） | BSD（完全開源） |
    | 適合 | Web 應用、簡單 CRUD | 複雜查詢、地理資料、分析型工作 |

    </details>

28. What is ORM, and what are its trade-offs?
    什麼是 ORM？有什麼優缺點？
    <details>
    <summary>Answer</summary>

    ORM（Object-Relational Mapping）把資料庫表映射成程式語言的物件，讓開發者用物件操作 DB 而不直接寫 SQL。

    **優點：** 開發速度快、防 SQL Injection（參數化查詢）、跨 DB 移植性
    **缺點：** 隱藏 SQL 細節（難優化）、容易產生 N+1 問題、複雜查詢需要 raw SQL、效能不如手寫 SQL

    </details>

29. What is the SQL execution order?
    SQL 的執行順序是什麼？
    <details>
    <summary>Answer</summary>

    ```
    1. FROM
    2. JOIN
    3. WHERE
    4. GROUP BY
    5. HAVING
    6. SELECT      ← alias 在這步才被定義
    7. ORDER BY
    8. LIMIT
    ```

    **實際影響：**

    | 子句 | 能不能用 SELECT 的 alias |
    |---|---|
    | WHERE | ❌ SELECT 還沒執行 |
    | HAVING | ❌ SELECT 還沒執行 |
    | ORDER BY | ✅ 在 SELECT 之後 |
    | LIMIT | ✅ 在 SELECT 之後 |

    所以 `HAVING SUM(amount) > 100000` 不能寫成 `HAVING amount > 100000`（alias），但 `ORDER BY amount DESC` 可以用 alias。

    </details>

30. What is the difference between UNION, UNION ALL, INTERSECT, and EXCEPT?
    UNION、UNION ALL、INTERSECT、EXCEPT 的差異是什麼？
    <details>
    <summary>Answer</summary>

    | 運算子 | 意思 | 去重 |
    |---|---|---|
    | `UNION` | 兩個查詢結果的**聯集** | ✅ 去重 |
    | `UNION ALL` | 兩個查詢結果的**聯集** | ❌ 保留重複 |
    | `INTERSECT` | 兩個查詢結果的**交集**（兩邊都有的） | ✅ 去重 |
    | `EXCEPT` | 左邊有、右邊沒有的（**差集**） | ✅ 去重 |

    **使用條件：** 兩個查詢的欄位數量和型別必須一致。

    ```sql
    -- UNION：合併兩年的門市清單（去重）
    SELECT store_id FROM sales WHERE EXTRACT(YEAR FROM sale_date) = 2023
    UNION
    SELECT store_id FROM sales WHERE EXTRACT(YEAR FROM sale_date) = 2024;

    -- EXCEPT：2024 有但 2023 沒有的門市
    SELECT store_id FROM sales WHERE EXTRACT(YEAR FROM sale_date) = 2024
    EXCEPT
    SELECT store_id FROM sales WHERE EXTRACT(YEAR FROM sale_date) = 2023;

    -- INTERSECT：2023 和 2024 都有銷售的門市
    SELECT store_id FROM sales WHERE EXTRACT(YEAR FROM sale_date) = 2023
    INTERSECT
    SELECT store_id FROM sales WHERE EXTRACT(YEAR FROM sale_date) = 2024;
    ```

    **UNION vs UNION ALL：** `UNION ALL` 效能較好（不需要排序去重），若確定結果不會重複或不在意重複，優先用 `UNION ALL`。

    </details>

31. What is the difference between WHERE and HAVING?
    WHERE 和 HAVING 的差異是什麼？
    <details>
    <summary>Answer</summary>

    | | WHERE | HAVING |
    |---|---|---|
    | 執行時機 | GROUP BY 之前 | GROUP BY 之後 |
    | 作用對象 | 原始 row | 聚合後的群組 |
    | 能用聚合函式 | ❌ | ✅ |

    ```sql
    -- WHERE：先過濾原始資料，再聚合
    SELECT store_id, SUM(amount)
    FROM sales
    WHERE sale_date >= '2024-01-01'   -- 先篩日期
    GROUP BY store_id;

    -- HAVING：聚合後再過濾
    SELECT store_id, SUM(amount)
    FROM sales
    GROUP BY store_id
    HAVING SUM(amount) > 100000;      -- 篩總額
    ```

    能用 WHERE 就用 WHERE，因為先過濾資料量少，聚合更快。

    </details>

32. What is the difference between RANK(), DENSE_RANK(), and ROW_NUMBER()?
    RANK()、DENSE_RANK()、ROW_NUMBER() 的差異是什麼？
    <details>
    <summary>Answer</summary>

    | 函式 | 並列時 | 並列後下一名 |
    |---|---|---|
    | `ROW_NUMBER()` | 強制給不同號碼 | 連續 |
    | `RANK()` | 給相同號碼 | 跳號 |
    | `DENSE_RANK()` | 給相同號碼 | 不跳號 |

    ```
    資料：500, 500, 300

    ROW_NUMBER：1, 2, 3
    RANK：       1, 1, 3   ← 跳過 2
    DENSE_RANK： 1, 1, 2   ← 不跳號
    ```

    **什麼時候用哪個：**
    - 取「前 N 名」且並列也要都取 → `DENSE_RANK`
    - 取「第 N 筆」不管並列 → `ROW_NUMBER`
    - 標準競賽排名 → `RANK`

    </details>
