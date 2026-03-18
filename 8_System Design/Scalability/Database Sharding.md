# Database Sharding

## 中文版

將一張大表的資料水平切分到多個資料庫（Shard），每個 Shard 只負責一部分資料，解決單一資料庫的容量與效能瓶頸。

### 分片策略

| 策略 | 說明 | 優點 | 缺點 |
|------|------|------|------|
| **Hash Sharding** | `shard = hash(key) % N` | 資料分布均勻 | 擴容時需 re-hash（一致性雜湊可緩解） |
| **Range Sharding** | 按值範圍切（如 user_id 1~100萬 一個 Shard） | 範圍查詢快 | 容易造成熱點（Hot Shard） |
| **Directory Sharding** | 維護一個映射表決定路由 | 彈性高 | 映射表本身是瓶頸與單點 |

### 帶來的挑戰

- **Cross-Shard Query**：JOIN 需要跨多個 Shard，通常要在應用層組合
- **跨 Shard 事務**：分散式交易複雜度高（通常用最終一致性取代）
- **Rebalancing**：新增 Shard 時資料遷移困難
- **Hotspot**：分片鍵選不好容易集中在某個 Shard

### 什麼時候用？
先考慮 Vertical Scaling → Read Replica → Caching → 最後才是 Sharding（複雜度最高）

## English Version

Sharding horizontally splits a large table's data across multiple databases (shards), where each shard holds only a subset of the data — solving capacity and performance bottlenecks of a single database.

### Sharding Strategies

| Strategy | Description | Pros | Cons |
|----------|-------------|------|------|
| **Hash Sharding** | `shard = hash(key) % N` | Even data distribution | Re-hashing required on scale-out (consistent hashing mitigates) |
| **Range Sharding** | Split by value range (e.g., user_id 1–1M on one shard) | Fast range queries | Prone to hot shards |
| **Directory Sharding** | Maintain a lookup table for routing | Flexible | Lookup table is a bottleneck and single point of failure |

### Challenges

- **Cross-Shard Queries**: JOINs span multiple shards; usually must be assembled at the application layer
- **Cross-Shard Transactions**: Distributed transactions are complex (eventual consistency is often used instead)
- **Rebalancing**: Migrating data when adding new shards is non-trivial
- **Hotspots**: Poor shard key selection concentrates traffic on one shard

### When to use?
Prefer Vertical Scaling → Read Replicas → Caching first — only shard when those are exhausted (sharding adds significant complexity).
