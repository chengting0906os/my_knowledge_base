# What is Message Queue

## 中文版

訊息佇列（Message Queue）是一種非同步通訊機制，讓生產者（Producer）與消費者（Consumer）解耦，中間透過佇列傳遞訊息。

### 核心優點

| 優點 | 說明 |
|------|------|
| **解耦** | Producer 不需知道 Consumer 是誰，兩者可獨立部署、擴展 |
| **非同步** | Producer 發完訊息立即返回，不必等 Consumer 處理完 |
| **削峰填谷** | 突發流量先進佇列，Consumer 按自身速率消費，保護下游 |
| **可靠性** | 訊息持久化後，即使 Consumer 暫時掛掉也不遺失 |

### 使用場景

- 訂單系統 → MQ → 庫存扣減、通知服務（解耦多個下游）
- 秒殺活動（高峰流量削峰）
- 跨服務的事件通知（Email、Push Notification）
- 日誌收集與分析管線

### 常見模式

| 模式 | 說明 |
|------|------|
| **Point-to-Point** | 一個訊息只被一個 Consumer 消費（Queue） |
| **Publish / Subscribe** | 一個訊息廣播給多個 Consumer（Topic） |

### 常見 MQ 系統

| 系統 | 特點 |
|------|------|
| **Kafka** | 高吞吐、持久化日誌、適合大數據管線 |
| **RabbitMQ** | 靈活路由、AMQP 協定、適合複雜業務訊息 |
| **ActiveMQ** | JMS 標準、老牌企業級 |
| **SQS** | AWS 托管、簡單易用 |

## English Version

A Message Queue is an asynchronous communication mechanism that decouples producers from consumers — messages are placed in a queue and processed independently.

### Core Benefits

| Benefit | Description |
|---------|-------------|
| **Decoupling** | Producers don't know who the consumers are; both can scale independently |
| **Async processing** | Producer returns immediately after publishing; doesn't wait for consumer |
| **Traffic shaping** | Burst traffic queues up; consumers process at their own pace — protects downstream |
| **Reliability** | Persisted messages survive consumer downtime |

### Use Cases

- Order service → MQ → inventory, notification services (fan-out to multiple consumers)
- Flash sales (absorb traffic spikes)
- Cross-service event notifications (email, push)
- Log collection and analytics pipelines

### Common Patterns

| Pattern | Description |
|---------|-------------|
| **Point-to-Point** | One message consumed by exactly one consumer (Queue) |
| **Publish / Subscribe** | One message broadcast to multiple consumers (Topic) |

### Common MQ Systems

| System | Characteristics |
|--------|----------------|
| **Kafka** | High throughput, persistent log, great for data pipelines |
| **RabbitMQ** | Flexible routing, AMQP protocol, complex business messaging |
| **ActiveMQ** | JMS standard, enterprise legacy |
| **SQS** | AWS managed, simple to use |
