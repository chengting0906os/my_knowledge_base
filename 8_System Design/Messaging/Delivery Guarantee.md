# Delivery Guarantee

## At-least-once vs At-most-once vs Exactly-once

## 中文版

| | At-most-once | At-least-once | Exactly-once |
|---|---|---|---|
| 會重複？ | 不會 | 可能 | 不會 |
| 會遺失？ | 可能 | 不會 | 不會 |
| 效能 | 最高 | 中 | 最低 |
| 實作難度 | 最低 | 低 | 最高 |

### At-most-once（最多一次）
- 訊息發出後不確認，也不重試
- 訊息可能遺失，但絕不重複
- 適合：日誌、監控指標（少一筆沒關係）

### At-least-once（至少一次）
- 訊息發出後等待 ACK，超時或失敗則重試
- 訊息一定送達，但**可能重複消費**
- **冪等性（Idempotency）是必要的**：Consumer 需設計成重複處理同一訊息不產生副作用
- 適合：訂單通知、帳務（搭配冪等設計）
- Kafka 預設提供 At-least-once

### Exactly-once（恰好一次）
- 訊息保證剛好被消費一次，不多不少
- 實作複雜：需要分散式事務或冪等 Producer + 事務型 Consumer
- Kafka 在同一叢集內可支援 Exactly-once（Transactional API）
- 適合：金融扣款、庫存扣減

### 實務建議
大多數系統選擇 **At-least-once + 冪等 Consumer**，比 Exactly-once 實作成本低且足夠可靠。

## English Version

| | At-most-once | At-least-once | Exactly-once |
|---|---|---|---|
| Duplicates? | No | Possible | No |
| Loss? | Possible | No | No |
| Performance | Highest | Medium | Lowest |
| Complexity | Lowest | Low | Highest |

### At-most-once
- Fire and forget — no ACK, no retry
- Messages may be lost but never duplicated
- Use cases: logs, metrics (losing one record is acceptable)

### At-least-once
- Wait for ACK; retry on timeout or failure
- Messages always delivered but **may be processed more than once**
- **Idempotency is required**: consumers must be designed so reprocessing the same message has no side effects
- Use cases: order notifications, billing (with idempotent design)
- Kafka default behavior

### Exactly-once
- Message delivered and processed exactly one time
- Complex to implement: requires distributed transactions or idempotent Producer + transactional Consumer
- Kafka supports Exactly-once within a single cluster (Transactional API)
- Use cases: financial deductions, inventory updates

### Practical Recommendation
Most systems use **At-least-once + idempotent Consumer** — lower implementation cost than Exactly-once while being sufficiently reliable.
