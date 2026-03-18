# Microservices vs Monolith

## 中文版

| | Monolith（單體） | Microservices（微服務） |
|---|---|---|
| 部署 | 整體一起部署 | 各服務獨立部署 |
| 擴展 | 整體擴展 | 各服務獨立擴展 |
| 技術選擇 | 統一技術棧 | 各服務可選不同語言 / DB |
| 開發複雜度 | 低（初期） | 高（分散式系統複雜度） |
| 故障隔離 | 差（一個模組掛掉影響全體） | 好（服務間隔離） |
| 網路通訊 | 函數呼叫（低延遲） | HTTP / gRPC（有網路 overhead） |
| 適合規模 | 小團隊、早期產品 | 大型團隊、成熟產品 |

### Monolith 的優點（別急著微服務）
- 開發快、部署簡單
- 無分散式系統問題（跨服務事務、網路故障）
- Debug 容易（單一 log、單一 process）

### Microservices 的挑戰
- **服務間通訊**：同步（HTTP/gRPC）vs 非同步（MQ）
- **分散式事務**：Saga Pattern（補償機制）
- **服務發現**：Consul、Kubernetes Service
- **可觀測性**：需要分散式追蹤（Jaeger、Zipkin）
- **部署複雜度**：需要 Container + Orchestration（K8s）

### 建議路徑
**從 Monolith 開始 → 找到邊界後再拆分**

先做 Modular Monolith（模組化單體），模組邊界清晰後再依需求拆成微服務。

## English Version

| | Monolith | Microservices |
|---|---|---|
| Deployment | Deploy as a single unit | Each service deployed independently |
| Scaling | Scale the whole thing | Scale individual services |
| Tech stack | Uniform | Each service can use different language/DB |
| Dev complexity | Low (initially) | High (distributed systems complexity) |
| Fault isolation | Poor (one module can take down everything) | Good (services are isolated) |
| Communication | Function calls (low latency) | HTTP / gRPC (network overhead) |
| Best for | Small teams, early-stage products | Large teams, mature products |

### Why Monolith is underrated
- Fast to develop, simple to deploy
- No distributed systems problems (cross-service transactions, network failures)
- Easy to debug (single log stream, single process)

### Microservices challenges
- **Inter-service communication**: synchronous (HTTP/gRPC) vs async (MQ)
- **Distributed transactions**: Saga Pattern (compensating transactions)
- **Service discovery**: Consul, Kubernetes Service
- **Observability**: requires distributed tracing (Jaeger, Zipkin)
- **Deployment complexity**: requires containers + orchestration (K8s)

### Recommended path
**Start with a Monolith → extract services when boundaries are clear**

Build a Modular Monolith first. Once module boundaries are well-defined, extract into microservices based on actual need.
