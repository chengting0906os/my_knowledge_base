# Kafka vs Redis as Message Queue

## 快速對照

|  | Redis List | Redis Stream | Kafka |
|---|---|---|---|
| 吞吐量 | ~10 萬 msg/s | ~10 萬 msg/s | 百萬 msg/s |
| 持久化 | 依 RDB/AOF，有遺失風險 | 依 RDB/AOF，有遺失風險 | 持久化，保證不遺失 |
| ACK 機制 | 無（RPOP 即刪除） | 有（XACK） | 有（commit offset） |
| 消費失敗 | 訊息消失，需自己處理 | 可重新消費（PEL） | 不 commit offset，自動重試 |
| Replay | 不支援 | 支援（範圍內） | 原生支援 |
| Consumer Group | 不支援 | 支援 | 支援 |
| 訊息保留 | 消費後刪除 | 依設定，可保留 | 依 retention，可長期保留 |
| 水平擴展 | 單節點瓶頸 | 單節點瓶頸 | partition + broker 水平擴展 |
| 部署複雜度 | 低 | 低 | 高（需 ZooKeeper 或 KRaft） |

## Redis List 的限制

- `LPUSH / BRPOP`：取出即刪除，沒有 ACK
- Consumer 處理失敗 → 訊息消失，需自己實作補救邏輯
- 沒有 Consumer Group：多個 consumer 會競爭同一個 list，無法讓多個 group 各自獨立消費
- 不支援 replay

## Redis Stream 補強了什麼

Redis Stream（5.0+）更像 Kafka：
- 有 Consumer Group，不同 group 各自獨立消費
- 有 PEL（Pending Entry List）：訊息取出後等待 XACK，未 ACK 的訊息記錄在 PEL，可重新投遞
- 有 message ID（stream offset），支援範圍查詢

但仍受限於 Redis 單節點吞吐，且 replay 範圍受 `MAXLEN` 限制。

## 為什麼訂票系統選 Kafka 而非 Redis

1. **吞吐量**：Redis 約 10 萬 RPS，Kafka 遠超過，適合高並發搶票
2. **持久化保證**：Redis 若在 RDB/AOF flush 前崩潰，訂票訊息可能遺失；Kafka 持久化更可靠
3. **Partition 有序性**：Kafka partition 內有序，天然解決同一座位的並發衝突，無需分散式鎖
4. **Consumer 失敗重試**：Kafka 不 commit offset 即可重試，Redis List 取出即刪，失敗需自己實作補救

## 何時選 Redis 當 MQ

- 訊息量小、容許少量遺失（如非關鍵通知）
- 已有 Redis，不想另外部署 Kafka
- 需要極低延遲、簡單任務分派
- 用 Redis Stream 且能接受其擴展限制

## 一句話

Redis 適合簡單、輕量、低成本的佇列需求；Kafka 適合高吞吐、可靠消費、需要 replay 或多 consumer group 的場景。
