# SQL vs NoSQL

## 中文版

| | SQL（關聯式） | NoSQL（非關聯式） |
|---|---|---|
| 資料結構 | 固定 Schema（表格） | 彈性（文件、K-V、寬欄、圖） |
| 查詢語言 | SQL | 各自 API |
| ACID | 完整支援 | 通常只有最終一致性（部分支援） |
| 水平擴展 | 困難（Sharding 複雜） | 原生支援 |
| JOIN | 支援 | 通常不支援或效能差 |
| 代表系統 | MySQL、PostgreSQL | MongoDB、Cassandra、Redis、DynamoDB |

### NoSQL 四大類型

| 類型 | 代表 | 適合場景 |
|------|------|----------|
| **Key-Value** | Redis、DynamoDB | 快取、Session、排行榜 |
| **Document** | MongoDB、Firestore | 彈性結構內容、使用者 Profile |
| **Wide-Column** | Cassandra、HBase | 時序資料、高寫入量 |
| **Graph** | Neo4j | 社交關係、推薦系統 |

### 如何選擇？
- 資料有複雜關聯、需要 JOIN → SQL
- 需要快速水平擴展、Schema 不固定 → NoSQL
- 強一致性要求（金融） → SQL
- 高寫入量、最終一致性可接受 → NoSQL（Cassandra）

## English Version

| | SQL (Relational) | NoSQL (Non-relational) |
|---|---|---|
| Data structure | Fixed schema (tables) | Flexible (document, K-V, wide-column, graph) |
| Query language | SQL | Proprietary APIs |
| ACID | Full support | Usually eventual consistency (partial support) |
| Horizontal scaling | Difficult (complex sharding) | Native support |
| JOIN | Supported | Usually unsupported or poor performance |
| Examples | MySQL, PostgreSQL | MongoDB, Cassandra, Redis, DynamoDB |

### Four NoSQL Types

| Type | Examples | Best for |
|------|---------|---------|
| **Key-Value** | Redis, DynamoDB | Cache, sessions, leaderboards |
| **Document** | MongoDB, Firestore | Flexible content, user profiles |
| **Wide-Column** | Cassandra, HBase | Time-series data, high write throughput |
| **Graph** | Neo4j | Social graphs, recommendation engines |

### How to choose?
- Complex relationships requiring JOINs → SQL
- Flexible schema, rapid horizontal scaling needed → NoSQL
- Strong consistency required (finance) → SQL
- High write volume, eventual consistency acceptable → NoSQL (Cassandra)
