# Redis Interview Q&A List

1. What is Redis, and what are its core characteristics?
   什麼是 Redis？它的核心特性是什麼？
   <details>
   <summary>Answer</summary>

   Redis（Remote Dictionary Server）是一個**記憶體內的資料結構儲存**，可作為快取、資料庫、訊息佇列使用。

   核心特性：
   - **單執行緒**（命令執行層）：命令原子執行，無鎖競爭
   - **記憶體儲存**：讀寫微秒級延遲
   - **豐富的資料結構**：String、Hash、List、Set、Sorted Set 等
   - **持久化可選**：RDB / AOF（見 Redis Persistence）
   - **非阻塞 I/O**：用 epoll/kqueue 處理大量連線
   </details>

2. Why is Redis single-threaded but still fast?
   Redis 是單執行緒，為什麼還這麼快？
   <details>
   <summary>Answer</summary>

   1. **資料全在記憶體**，無磁碟 I/O 瓶頸
   2. **單執行緒無鎖**，無 context switch overhead，命令排隊依序原子執行
   3. **高效的資料結構實作**（如 skiplist、ziplist、intset）
   4. **非阻塞 I/O（epoll）**：單執行緒可同時監聽大量 socket，I/O 不阻塞命令執行

   > Redis 6.0+ 的網路 I/O 改為多執行緒，但命令執行仍是單執行緒。
   </details>

3. What data structures does Redis support, and what are their use cases?
   Redis 支援哪些資料結構？各自適合什麼場景？
   <details>
   <summary>Answer</summary>

   | 類型 | 使用場景 |
   |------|----------|
   | **String** | 快取、計數器（INCR）、分散式鎖 |
   | **Hash** | 使用者資料、物件屬性（避免序列化整個 JSON） |
   | **List** | 訊息佇列（LPUSH/RPOP）、最新動態 |
   | **Set** | 標籤、去重、交集/聯集運算 |
   | **Sorted Set (ZSet)** | 排行榜、延遲任務隊列 |
   | **Bitmap** | 每日簽到、布林標記 |
   | **HyperLogLog** | 近似計數（UV 統計），誤差 < 1% |
   | **Stream** | 訊息流、消費者群組（比 Pub/Sub 可靠） |
   </details>

4. Why is Sorted Set suitable for leaderboards? What data structure does it use internally?
   Sorted Set 為什麼適合排行榜？內部用什麼資料結構？
   <details>
   <summary>Answer</summary>

   - 每個元素有一個 **score**，Redis 自動維護有序性
   - `ZADD`（插入）、`ZRANK`（查名次）、`ZRANGE`（取範圍）都是 **O(log N)**
   - 比 DB 的 `ORDER BY` 快：不需要每次重新排序，Redis 在 memory 裡維護好了

   **內部實作：**
   - 元素數量少時：**ziplist**（省記憶體）
   - 元素數量多時：**skiplist + hashtable**
     - skiplist：O(log N) 範圍查詢
     - hashtable：O(1) 單點查詢（by key）
   </details>

5. What are the common Redis cache patterns (Cache Aside, Write Through, Write Behind)?
   常見的 Redis 快取模式有哪些？
   <details>
   <summary>Answer</summary>

   **Cache Aside（最常用）**
   ```
   讀：查 Cache → miss → 查 DB → 寫入 Cache → 回傳
   寫：更新 DB → 刪除 Cache（讓下次讀時重新載入）
   ```
   - 應用程式自己管理快取，寫時**刪除** key，不要直接更新 Cache
   - **為什麼刪除而非更新**：T1 寫 DB=100、T2 寫 DB=200，若都去更新 Redis，誰後寫 Redis 誰決定最終值，可能與 DB 不一致。刪除的話 Redis 變空，下一次讀去 DB 拿，永遠是最新值。

   **Write Through**
   ```
   寫：同時寫 Cache + DB（同步）
   ```
   - Cache 永遠與 DB 一致，但寫入延遲高；冷資料也會進 Cache

   **Write Behind（Write Back）**
   ```
   寫：只寫 Cache → 非同步批次刷回 DB
   ```
   - 寫入效能最好，但 Cache 崩潰前未刷回的資料會遺失
   </details>

6. What are Cache Penetration, Cache Breakdown, and Cache Avalanche?
   什麼是快取穿透、快取擊穿、快取雪崩？如何解決？
   <details>
   <summary>Answer</summary>

   | 問題 | 說明 | 解法 |
   |------|------|------|
   | **快取穿透** | 查詢不存在的 key，每次都打到 DB | 快取空值（TTL 短）或用 Bloom Filter 過濾 |
   | **快取擊穿** | 熱點 key 過期，瞬間大量請求打到 DB | 互斥鎖重建快取，或設定熱點 key 不過期 |
   | **快取雪崩** | 大量 key 同時過期，DB 被打爆 | 隨機化 TTL、熱點 key 永不過期、限流降級 |

   - 穿透：key **不存在** DB 裡
   - 擊穿：key **存在** DB 裡，但快取剛過期
   - 雪崩：**大量** key 同時過期
   </details>

7. What is the difference between RDB and AOF persistence in Redis?
   Redis 的 RDB 和 AOF 持久化有什麼差異？
   <details>
   <summary>Answer</summary>

   | | RDB | AOF |
   |---|---|---|
   | 方式 | 定期快照（`.rdb`） | 追加寫入命令日誌 |
   | 資料丟失 | 最多幾分鐘 | 最多 1 秒（everysec） |
   | 恢復速度 | 快 | 較慢（需重播命令） |
   | 檔案大小 | 小 | 大 |
   | 效能影響 | 低 | 中（每秒 fsync） |

   **選擇建議：**
   - 純快取可丟 → 關閉持久化
   - 可接受少量丟失 → RDB
   - 不能丟資料 → AOF（everysec）
   - 兼顧 → 混合持久化（Redis 4.0+，AOF 開頭嵌入 RDB 快照）
   </details>

8. How do you implement a distributed lock with Redis?
   如何用 Redis 實作分散式鎖？
   <details>
   <summary>Answer</summary>

   **基本實作：SET NX PX**
   ```redis
   SET lock_key {unique_value} NX PX 30000
   ```
   - `NX`：只有 key 不存在才設定（原子搶鎖）
   - `PX 30000`：30 秒過期，防死鎖
   - `unique_value`：UUID，防止誤刪別人的鎖

   **釋放鎖（必須用 Lua 保證原子性）：**
   ```lua
   if redis.call("GET", KEYS[1]) == ARGV[1] then
       return redis.call("DEL", KEYS[1])
   end
   ```

   **常見問題：**
   - 鎖提前過期 → Watchdog 自動續期（Redisson）
   - 單節點故障 → Redlock（5 個獨立節點，取得 N/2+1 個鎖）
   </details>

9. What is the difference between Redis Pub/Sub and Stream?
   Redis Pub/Sub 和 Stream 差在哪？
   <details>
   <summary>Answer</summary>

   | | Pub/Sub | Stream |
   |---|---|---|
   | 訊息持久化 | 不持久，發出即消失 | 持久化，可重播 |
   | 消費者離線 | 訊息丟失 | 可從斷點繼續消費 |
   | 消費者群組 | 不支援 | 支援（Consumer Group） |
   | 確認機制 | 無 | 有（XACK） |
   | 適合場景 | 即時通知、不重要的廣播 | 可靠訊息傳遞、事件溯源 |

   - Pub/Sub：fire-and-forget，簡單但不可靠
   - Stream：類似 Kafka，適合需要可靠消費的場景
   </details>

10. How does Redis handle key expiration (TTL and eviction policies)?
    Redis 如何處理 key 的過期與記憶體淘汰？
    <details>
    <summary>Answer</summary>

    **過期機制（TTL）：**
    - **惰性刪除**：key 被訪問時才檢查是否過期，省 CPU 但記憶體可能累積
    - **定期刪除**：每隔一段時間隨機抽樣檢查，刪除已過期的 key

    **記憶體淘汰策略（maxmemory-policy）：**

    | 策略 | 說明 |
    |------|------|
    | `noeviction` | 不淘汰，記憶體滿時寫入報錯（預設） |
    | `allkeys-lru` | 所有 key 中，淘汰最久未使用的 |
    | `volatile-lru` | 只從有 TTL 的 key 中，淘汰最久未使用的 |
    | `allkeys-lfu` | 所有 key 中，淘汰使用頻率最低的 |
    | `allkeys-random` | 隨機淘汰 |

    快取場景通常選 `allkeys-lru` 或 `allkeys-lfu`。
    </details>

11. What is Redis pipelining, and when should you use it?
    什麼是 Redis Pipeline？什麼時候用？
    <details>
    <summary>Answer</summary>

    Pipeline 讓 client 一次批次送出多個命令，不等每個回應就繼續，最後一次收所有回應。

    - 減少 **RTT（Round-Trip Time）**：N 個命令只需 1 個 RTT，而非 N 個
    - 適合批次操作（如一次寫入 1000 個 key）
    - 注意：Pipeline 不是原子的，中途某個命令失敗不影響其他命令執行

    與 **Transaction（MULTI/EXEC）** 的差異：
    - Pipeline：純粹減少網路來回，無原子性保證
    - MULTI/EXEC：原子執行一組命令，但不支援條件分支（不能根據中間結果決定後續命令）
    </details>

12. What is Redis vs Memcached? When would you choose Memcached?
    Redis 和 Memcached 有什麼差別？什麼時候選 Memcached？
    <details>
    <summary>Answer</summary>

    | | Redis | Memcached |
    |---|---|---|
    | 資料結構 | 豐富（String、Hash、List、Set、ZSet…） | 僅 String |
    | 持久化 | 支援（RDB / AOF） | 不支援 |
    | 多執行緒 | 單執行緒（命令層） | 多執行緒 |
    | Pub/Sub | 支援 | 不支援 |
    | Cluster | 原生支援 | 需客戶端分片 |

    絕大多數場景選 Redis。
    Memcached 的優勢：多執行緒，在純 K-V 快取且嚴重受多核 CPU 限制的場景下吞吐量可能更高。
    </details>

13. What are some common Redis use cases in backend systems?
    Redis 在後端系統中有哪些常見用途？
    <details>
    <summary>Answer</summary>

    | 用途 | 實作方式 |
    |------|----------|
    | 快取 | Cache Aside，Cache Penetration/Breakdown/Avalanche 防護 |
    | Session 儲存 | 用 String/Hash 儲存 session，設 TTL 自動過期 |
    | 排行榜 | Sorted Set（ZADD/ZRANK/ZRANGE） |
    | 分散式鎖 | SET NX PX + Lua 釋放 |
    | 計數器 / 限流 | INCR + TTL，或 Sliding Window（ZSet） |
    | 訊息佇列 | List（LPUSH/BRPOP）或 Stream |
    | Pub/Sub 通知 | 即時廣播（不需可靠性時） |
    | 去重 | Set（SADD + SISMEMBER） |
    </details>

14. How would you implement a rate limiter using Redis?
    如何用 Redis 實作 Rate Limiter？
    <details>
    <summary>Answer</summary>

    **方法一：Fixed Window（計數器）**
    ```
    key = "rate:user_id:2024010112"  ← 以時間窗口為 key
    INCR key
    EXPIRE key 60
    if count > limit: reject
    ```
    - 簡單，但窗口邊界可能被突破（窗口切換瞬間可打兩倍流量）

    **方法二：Sliding Window（Sorted Set）**
    ```
    key = "rate:user_id"
    ZREMRANGEBYSCORE key 0 (now - window)  ← 移除過期請求
    count = ZCARD key
    if count < limit:
        ZADD key now now
        允許
    else:
        拒絕
    ```
    - 精確，但記憶體用量較高

    **方法三：Token Bucket / Leaky Bucket**
    - 可用 Lua 腳本原子執行，確保 check + deduct 的原子性
    </details>

15. What is the difference between WATCH/MULTI/EXEC and Lua scripts in Redis?
    Redis 的 WATCH/MULTI/EXEC 和 Lua 腳本有什麼差別？
    <details>
    <summary>Answer</summary>

    **MULTI/EXEC（Transaction）：**
    - 將一組命令排隊，EXEC 時原子執行
    - 命令執行期間不能讀中間結果，無法做條件判斷
    - WATCH：樂觀鎖，若 WATCH 的 key 被改動，EXEC 自動失敗（返回 nil）

    **Lua 腳本：**
    - 在 server 端原子執行任意邏輯，可以讀中間結果、做條件分支
    - 比 MULTI/EXEC 更靈活，分散式鎖的釋放就需要 Lua（GET + DEL 需要條件判斷）
    - 腳本執行期間 Redis 阻塞，不能有長時間運算

    **選擇原則：**
    - 簡單的批次操作 → MULTI/EXEC 或 Pipeline
    - 需要讀中間結果或條件判斷 → Lua 腳本
    </details>
