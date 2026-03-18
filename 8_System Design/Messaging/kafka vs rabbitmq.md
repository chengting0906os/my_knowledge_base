# Kafka vs RabbitMQ

## 一句話

- Kafka: `log-based`、`consumer-based`、`pull-based`
- RabbitMQ: `queue-based`、`broker-driven`、`push-based`（一般 queue 模式）

RabbitMQ is designed to deliver a task to a consumer, ensure it gets processed, and then remove it from the queue. A message is sent to a queue, consumed by a worker, acknowledged, and deleted.
使用完即刪除

Kafka, on the other hand, is built as a distributed log. When an event is written to Kafka, it stays there for a configured retention period (days, weeks, or even indefinitely).
Kafka 會因為你的 retention 設定決定留存多久

## 快速對照

- Data model
  - Kafka: append-only log（topic/partition）
  - RabbitMQ: message queue（exchange -> queue）
- Consumption
  - Kafka: consumer 自己管理 offset，可 replay
  - RabbitMQ: broker 投遞，ack 後通常視為完成消費
- Delivery style
  - Kafka: pull（consumer poll）將訊息發佈到佇列，而不管消費者是否已擷取它們
  - RabbitMQ: push（broker push 給 consumer） 生產者傳送訊息並監控其是否到達預期的取用者處
- Throughput
  - Kafka: 高吞吐、適合事件流/日誌流
  - RabbitMQ: 低延遲任務分發、工作佇列很常見
- Replay
  - Kafka: 原生強項（保留期間內可重讀）
  - RabbitMQ: 一般 queue 不擅長歷史 replay（Streams 例外）

## 高可用性與擴展性（補充）

- RabbitMQ
  - 高可用性：可透過多節點複寫提升容錯。過去常提 `Mirrored Queues`，現在實務上多建議使用 `Quorum Queues`。
  - 擴展性限制：在超大規模資料流場景下，水平擴展通常不如 Kafka 線性，較容易先遇到吞吐瓶頸。
- Kafka
  - 高可用性：基於 partition + replica 機制，broker 故障時可由副本接手。
  - 無縫水平擴展：新增節點後可透過分區重平衡分散負載，較適合超大規模事件流。

## 何時選哪個

- 選 Kafka: 搶票/行為追蹤/事件驅動、需要削峰填谷 + replay + 高吞吐
- 選 RabbitMQ: 任務分派、即時命令、複雜 routing、希望 broker 幫你 push 訊息

## 典型應用場景

- RabbitMQ
  - 即時任務排程：例如電子郵件通知、延遲任務處理
  - 微服務間通信：需要靈活路由與可靠投遞
  - 即時性應用：重視低延遲且可靠性高，例如交易處理流程
- Kafka
  - 大數據流管道：串接資料來源與處理系統，做即時資料傳輸
  - 日誌與事件流分析：處理海量系統日誌或使用者行為事件
  - 事件驅動架構：例如即時推薦系統、監控與告警系統

## 什麼時候選 RabbitMQ

RabbitMQ 很適合傳統背景工作（background worker）系統，特別是「任務做完就好」的場景。

- 你只需要任務被處理一次，完成後就不需要保留該訊息
- 典型例子：發送歡迎信、處理上傳圖片、呼叫支付 API
- 這類工作屬於 fire-and-forget：重點是可靠投遞與完成執行，不是長期留存或歷史重播

## 什麼時候選 Kafka

Kafka 適合事件驅動系統，特別是你有以下需求時：

- 多個服務都要消費同一個事件，且彼此獨立處理
  - 例如同一個 payment event，風控、通知、報表、對帳等服務都要用
  - 每個服務用自己的 consumer group，以自己的速度消費同一份事件流
- 需要 replay 能力
  - 可用於 bug 修復後重跑、邏輯更新後重處理、或新服務回補歷史資料
- 你在建資料管線（data pipeline）
  - 事件代表狀態變更，且多個下游系統都需要即時或批次讀取同一條資料流
- 規模與吞吐是重點
  - Kafka 適合高流量事件流（例如 clickstream、IoT、即時分析）
  - 比如：核心資料管線會先把多來源資料寫進 Kafka topics，再由多個服務各自消費；有些做即時處理，有些做分析洞察。不同 consumer 可以用不同速度讀同一條事件流，這正是 Kafka 的關鍵優勢。

## 面試一句話版本

- 「Kafka 比較像可回放的事件日誌（log + pull + consumer offset）；RabbitMQ 比較像任務佇列（queue + push + broker routing）。」

## 參考資料

- https://aws.amazon.com/tw/compare/the-difference-between-rabbitmq-and-kafka/
- https://medium.com/@taycode/rabbitmq-vs-kafka-a-practical-guide-61b82c096cf7
- https://vocus.cc/article/6740c646fd8978000184cae3
