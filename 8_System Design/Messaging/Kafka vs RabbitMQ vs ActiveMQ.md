# Kafka vs RabbitMQ vs ActiveMQ

## 快速對照

|          | Kafka                              | RabbitMQ                          | ActiveMQ             |
| -------- | ---------------------------------- | --------------------------------- | -------------------- |
| 資料模型 | Append-only log（topic/partition） | Message queue（exchange → queue） | Queue / Topic（JMS） |
| 消費模式 | Pull（consumer 管理 offset）       | Push（broker 投遞）               | Push（JMS 標準）     |
| 訊息保留 | 依 retention 設定（可重播）        | 消費並 ACK 後刪除                 | 消費後刪除           |
| 吞吐量   | 極高（百萬 msg/s）                 | 中（萬級 msg/s）                  | 中低                 |
| 延遲     | 毫秒級                             | 微秒級（低延遲任務佳）            | 中                   |
| Replay   | 原生支援                           | 不支援（Streams 例外）            | 不支援               |
| 水平擴展 | 優秀（partition + broker）         | 有限                              | 有限                 |
| 適合場景 | 事件流、數據管線、高吞吐           | 任務分派、複雜 routing            | 企業級 JMS 整合      |

## 選擇指南

**選 Kafka**：需要高吞吐、多個消費者讀同一事件、需要 replay、建資料管線

**選 RabbitMQ**：任務做完即刪、複雜 routing（exchange/binding）、低延遲任務分派、不需要 replay

**選 ActiveMQ**：已有 JMS 生態、企業遺留系統整合

## 一句話

- Kafka：可回放的**事件日誌**（log + pull + consumer offset）
- RabbitMQ：**任務佇列**（queue + push + broker routing）
- ActiveMQ：企業 JMS 標準的老牌實作
