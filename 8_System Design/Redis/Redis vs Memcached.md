# Redis vs Memcached

## 中文版

| | Redis | Memcached |
|---|---|---|
| 資料結構 | 豐富（String、Hash、List、Set、ZSet…） | 僅 String |
| 持久化 | 支援（RDB / AOF） | 不支援 |
| 叢集 | Redis Cluster（原生） | 需客戶端分片 |
| 多執行緒 | 單執行緒（命令執行層） | 多執行緒 |
| 記憶體效率 | 略低（資料結構 overhead） | 略高（純 K-V） |
| Pub/Sub | 支援 | 不支援 |
| Lua 腳本 | 支援 | 不支援 |
| 使用場景 | 快取 + 更多（排行榜、分散式鎖、訊息） | 單純大量快取 |

### 結論

絕大多數場景選 **Redis**，功能更豐富，生態更完整。
只有在極度追求多核心 CPU 吞吐量的純快取場景下，Memcached 的多執行緒才有優勢。

## English Version

| | Redis | Memcached |
|---|---|---|
| Data structures | Rich (String, Hash, List, Set, ZSet…) | String only |
| Persistence | Supported (RDB / AOF) | Not supported |
| Clustering | Redis Cluster (native) | Client-side sharding required |
| Threading | Single-threaded (command execution) | Multi-threaded |
| Memory efficiency | Slightly lower (data structure overhead) | Slightly higher (pure K-V) |
| Pub/Sub | Supported | Not supported |
| Lua scripting | Supported | Not supported |
| Use cases | Cache + more (leaderboards, distributed locks, messaging) | Simple large-scale caching |

### Bottom Line

Choose **Redis** in almost all cases — it's more feature-rich with a much larger ecosystem.
Memcached's multi-threaded advantage only matters in pure caching scenarios that are severely bottlenecked by multi-core CPU throughput.
