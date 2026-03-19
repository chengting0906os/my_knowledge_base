# Messaging Interview Q&A List

1. What is a Message Queue, and what problems does it solve?
   什麼是訊息佇列？它解決了什麼問題？
   <details>
   <summary>Answer</summary>

   訊息佇列是一種非同步通訊機制，讓 Producer 與 Consumer 解耦，訊息透過佇列傳遞。

   解決的問題：
   - **解耦**：Producer 不需知道 Consumer 是誰，兩者可獨立部署、擴展
   - **非同步**：Producer 發完立即返回，不必等 Consumer 處理完
   - **削峰填谷**：突發流量先進佇列，Consumer 按自身速率消費，保護下游
   - **可靠性**：訊息持久化後，Consumer 暫時掛掉也不遺失
   </details>

2. What is the difference between At-most-once, At-least-once, and Exactly-once delivery?
   At-most-once、At-least-once、Exactly-once 差在哪？
   <details>
   <summary>Answer</summary>

   | | At-most-once | At-least-once | Exactly-once |
   |---|---|---|---|
   | 會重複？ | 不會 | 可能 | 不會 |
   | 會遺失？ | 可能 | 不會 | 不會 |
   | 效能 | 最高 | 中 | 最低 |
   | 實作難度 | 最低 | 低 | 最高 |

   - **At-most-once**：Fire and forget，適合日誌、監控（丟一筆沒關係）
   - **At-least-once**：有 ACK + retry，可能重複，需要 Consumer **冪等性**；Kafka 預設
   - **Exactly-once**：需分散式事務或 Kafka Transactional API，適合金融扣款

   實務建議：**At-least-once + 冪等 Consumer**，成本低且足夠可靠。
   </details>

3. What is idempotency in message consumption, and how do you implement it?
   什麼是消費冪等性？怎麼實作？
   <details>
   <summary>Answer</summary>

   冪等性：同一訊息處理多次，結果與處理一次相同。

   **常見實作方式：**
   - **唯一 message ID**：每筆訊息帶 unique ID，Consumer 處理前查 DB/Redis 是否已處理過，是則跳過
   - **資料庫唯一鍵**：用訊息的業務 key 做 DB unique constraint，重複 insert 直接忽略
   - **冪等操作設計**：`UPDATE balance = 100 WHERE id = 1` 比 `UPDATE balance = balance - 10` 更安全

   冪等性是 At-least-once 能在實務中運作的關鍵保障。
   </details>

4. What is a Kafka partition, and why does it matter?
   Kafka 的 partition 是什麼？為什麼重要？
   <details>
   <summary>Answer</summary>

   Partition 是 Kafka topic 的最小並行單位，每個 partition 是一個 append-only log。

   重要性：
   - **並行度**：每個 partition 同一時間只被 consumer group 內的一個 consumer 消費，partition 數量決定最大並行度
   - **有序性**：同一 partition 內訊息有序，不同 partition 間無法保證順序
   - **水平擴展**：增加 partition 可分散到更多 broker，提升吞吐量

   **Partition Key 的選擇**：
   - 相同 key 的訊息進同一 partition（保證順序）
   - 例如：用 `user_id` 確保同一用戶的事件有序處理
   - 若 key 分布不均，可能產生 hotspot partition
   </details>

5. What is a Kafka Consumer Group, and how does it work?
   什麼是 Kafka Consumer Group？如何運作？
   <details>
   <summary>Answer</summary>

   Consumer Group 是一組 consumer 的集合，共同消費同一個 topic。

   規則：
   - 同一 partition 同一時間只被 group 內**一個** consumer 消費
   - 不同 group 可以各自獨立消費同一 topic（互不影響）
   - Consumer 數量 > partition 數量時，多餘的 consumer 閒置

   ```
   Topic: order-events (3 partitions)

   Group A (訂單服務):   C1 → P0, P1   C2 → P2
   Group B (通知服務):   C3 → P0   C4 → P1   C5 → P2
   ```

   兩個 group 互相獨立，各自維護自己的 offset。
   </details>

6. What is an offset in Kafka, and how does it relate to message replay?
   Kafka 的 offset 是什麼？和 replay 有什麼關係？
   <details>
   <summary>Answer</summary>

   Offset 是 partition 內每條訊息的**序號**（從 0 開始），由 consumer 自己管理。

   - Consumer 消費後 commit offset，下次從該位置繼續
   - 若 consumer 故障，從上次 committed offset 重新消費（At-least-once）
   - **Replay**：手動把 offset 重設到過去的位置，重新消費歷史訊息
     - 用途：bug 修復後重處理、新服務回補歷史資料、測試

   Offset 由 consumer 管理（而非 broker）是 Kafka 能做 replay 的關鍵。
   </details>

7. Why is Kafka fast?
   Kafka 為什麼快？
   <details>
   <summary>Answer</summary>

   兩個核心原因：

   **1. 順序寫入（Sequential Write）**
   - Partition 是 append-only log，資料只在尾端追加
   - 順序 I/O 比隨機 I/O 快很多，磁碟吞吐高

   **2. 零拷貝（Zero-Copy）**
   - 傳統路徑：`disk → kernel buffer → user buffer → kernel socket buffer → NIC`
   - sendfile 路徑：`disk → kernel buffer → NIC`（省掉 user space 拷貝）
   - CPU 更省，每秒可傳更多資料

   加上**批次寫入**與 **OS page cache**，在高流量事件流場景下吞吐量特別高。
   </details>

8. What is the difference between Kafka and RabbitMQ?
   Kafka 和 RabbitMQ 差在哪？各自適合什麼場景？
   <details>
   <summary>Answer</summary>

   | | Kafka | RabbitMQ |
   |---|---|---|
   | 資料模型 | Append-only log | Message queue |
   | 消費模式 | Pull（consumer 管理 offset） | Push（broker 投遞） |
   | 訊息保留 | 依 retention 保留，可重播 | ACK 後刪除 |
   | 吞吐量 | 極高 | 中 |
   | 延遲 | 毫秒級 | 微秒級（單訊息低延遲） |
   | Replay | 原生支援 | 不支援 |

   **選 Kafka**：高吞吐、多 consumer 讀同一事件、需要 replay、數據管線

   **選 RabbitMQ**：任務做完即刪、複雜 routing、低延遲任務分派

   一句話：Kafka 是可回放的**事件日誌**；RabbitMQ 是**任務佇列**。
   </details>

9. What is the difference between Redis List and Kafka as a message queue?
   Redis List 和 Kafka 作為訊息佇列，差在哪？
   <details>
   <summary>Answer</summary>

   | | Redis List | Kafka |
   |---|---|---|
   | 吞吐量 | ~10 萬 msg/s | 百萬 msg/s |
   | 持久化 | 依 RDB/AOF 設定，有遺失風險 | 持久化，保證不遺失 |
   | ACK 機制 | 無（RPOP 即刪除） | 有（consumer commit offset） |
   | 消費失敗 | 訊息消失，需自己實作 dead letter | 不 commit offset，可重試 |
   | Replay | 不支援 | 原生支援 |
   | Consumer Group | 不支援 | 支援 |

   Redis List 適合簡單、低成本、容許少量遺失的場景。
   Kafka 適合需要可靠消費、高吞吐、或多個服務消費同一事件的場景。
   </details>

10. What is a Dead Letter Queue (DLQ)?
    什麼是死信佇列（Dead Letter Queue）？
    <details>
    <summary>Answer</summary>

    DLQ 是存放**無法被正常消費的訊息**的佇列。

    訊息進入 DLQ 的原因：
    - 消費失敗超過最大重試次數
    - 訊息格式錯誤（無法反序列化）
    - 訊息超過 TTL 未被消費

    用途：
    - 排查問題（為什麼這些訊息一直失敗？）
    - 修復後手動重處理

    **Kafka 沒有內建 DLQ**，需自己實作（消費失敗 → 發到另一個 topic）。
    RabbitMQ 有原生 Dead Letter Exchange（DLX）支援。
    </details>

11. How does Kafka guarantee ordering within a partition?
    Kafka 如何保證 partition 內的訊息有序？
    <details>
    <summary>Answer</summary>

    Partition 內的訊息是 **append-only**，offset 單調遞增，Consumer 按 offset 順序消費，因此 partition 內天然有序。

    跨 partition 無法保證順序。

    **實務設計**：需要有序處理的訊息，用相同的 partition key（如 `user_id`、`order_id`），確保進同一 partition。

    你的 ticketing system 用座位號 / 100 作為 partition key，就是為了讓同一區的訂票請求依序處理，避免同一座位被重複售出。
    </details>

12. What is consumer rebalancing in Kafka, and what problems can it cause?
    Kafka 的 consumer rebalance 是什麼？會帶來什麼問題？
    <details>
    <summary>Answer</summary>

    Rebalance 是 consumer group 內 partition 分配重新調整的過程。

    **觸發時機：**
    - Consumer 加入或離開 group
    - Consumer 崩潰（heartbeat 超時）
    - Partition 數量變化

    **Rebalance 的問題：**
    - Rebalance 期間，所有 consumer **暫停消費**（Stop-the-world）
    - 若 consumer 在處理中途被踢出（GC pause 導致 heartbeat 超時），已處理但未 commit 的訊息會被另一個 consumer 重新處理 → 重複消費
    - 高頻 rebalance 會嚴重影響吞吐量

    **緩解方式：**
    - 調整 `session.timeout.ms` 和 `max.poll.interval.ms`
    - Kafka 2.4+ 的 Incremental Cooperative Rebalancing（只重分配需要移動的 partition，不全停）
    </details>
