# Event-Driven Architecture

## 中文版

系統中各元件透過**發布 / 訂閱事件**進行通訊，而不是直接呼叫彼此。

### 核心概念

| 概念 | 說明 |
|------|------|
| **Event** | 表示「已發生的事實」，不可變（如 `OrderPlaced`、`PaymentCompleted`） |
| **Producer** | 發布事件的服務 |
| **Consumer** | 訂閱並處理事件的服務 |
| **Event Broker** | 事件路由中介（Kafka、RabbitMQ、EventBridge） |

### 與 REST 呼叫的差異

| | 同步 REST | 事件驅動 |
|---|---|---|
| 耦合度 | 高（直接依賴） | 低（透過事件解耦） |
| 可用性 | 下游掛掉 → 上游受影響 | 下游掛掉 → 事件排隊等待 |
| 追蹤難度 | 容易（call stack） | 難（需分散式追蹤） |
| 最終一致性 | 通常強一致 | 通常最終一致 |

### 常見模式

**Event Notification**：服務 A 通知服務 B 某事發生，B 自行查詢詳情（輕量，但 B 需回查）

**Event-Carried State Transfer**：事件本身帶有完整資料，B 不需回查（資料量大但自給自足）

**Event Sourcing**：系統狀態由事件序列推導而來，事件日誌是唯一真相（可回放、可審計）

**CQRS（Command Query Responsibility Segregation）**：讀寫分離，Write Side 發事件，Read Side 訂閱並維護專屬的查詢模型

### 優缺點

**優點**：解耦、可擴展、支援非同步、天然的審計日誌

**缺點**：最終一致性難以處理、Debug 複雜、事件版本管理（Schema Evolution）挑戰

## English Version

Components communicate by **publishing and subscribing to events** rather than calling each other directly.

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Event** | Represents something that happened — immutable fact (e.g., `OrderPlaced`, `PaymentCompleted`) |
| **Producer** | Service that publishes events |
| **Consumer** | Service that subscribes to and handles events |
| **Event Broker** | Routes events between services (Kafka, RabbitMQ, EventBridge) |

### vs Synchronous REST

| | Synchronous REST | Event-Driven |
|---|---|---|
| Coupling | High (direct dependency) | Low (decoupled via events) |
| Availability | Downstream failure impacts upstream | Downstream failure → events queue up |
| Traceability | Easy (call stack) | Hard (requires distributed tracing) |
| Consistency | Usually strong | Usually eventual |

### Common Patterns

**Event Notification**: Service A notifies B that something happened; B queries for details separately (lightweight, but requires round-trip)

**Event-Carried State Transfer**: Event contains full data; B needs no additional queries (more data but self-contained)

**Event Sourcing**: System state derived from a sequence of events; the event log is the single source of truth (replayable, auditable)

**CQRS (Command Query Responsibility Segregation)**: Separate read and write paths; Write Side emits events; Read Side subscribes and maintains its own query-optimized model

### Pros & Cons

**Pros**: Decoupling, scalability, async-friendly, natural audit log

**Cons**: Eventual consistency is hard to reason about; debugging complexity; schema evolution challenges
