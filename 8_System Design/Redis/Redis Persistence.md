# Redis Persistence

## 中文版

Redis 是記憶體資料庫，預設重啟後資料消失。持久化讓資料能在重啟後恢復。

### RDB（Redis Database Snapshot）

**快照方式**：每隔一段時間將記憶體中的資料快照到磁碟（`.rdb` 檔案）。

| | 說明 |
|---|---|
| 觸發方式 | 定時（BGSAVE）或達到閾值（如 60 秒內有 1000 次寫入） |
| 優點 | 檔案小、恢復速度快、對效能影響小 |
| 缺點 | 快照之間的資料會遺失（最多丟失幾分鐘資料） |

### AOF（Append-Only File）

**日誌方式**：將每個寫入命令追加寫入日誌檔案，重啟時重播日誌恢復資料。

| fsync 策略 | 說明 | 資料安全性 |
|-----------|------|------------|
| `always` | 每次寫入都 fsync | 最安全，效能最差 |
| `everysec` | 每秒 fsync（預設） | 最多丟 1 秒資料 |
| `no` | 交由 OS 決定 | 效能最好，安全性最低 |

| | 說明 |
|---|---|
| 優點 | 資料丟失最少（everysec 最多丟 1 秒） |
| 缺點 | 檔案較大、重播速度較慢 |

### 混合持久化（Redis 4.0+）

AOF 檔案開頭嵌入一份 RDB 快照，之後追加增量 AOF 命令。兼顧快速恢復與資料完整性。

### 如何選擇？

| 場景 | 建議 |
|------|------|
| 純快取，資料可丟 | 關閉持久化 |
| 可接受少量丟失 | RDB |
| 資料不能丟 | AOF（everysec） |
| 兼顧效能與安全 | 混合持久化 |

## English Version

Redis is an in-memory database — data is lost on restart by default. Persistence allows data to survive restarts.

### RDB (Redis Database Snapshot)

**Snapshot approach**: Periodically dumps the in-memory dataset to disk as an `.rdb` file.

| | Description |
|---|---|
| Trigger | Scheduled (BGSAVE) or threshold-based (e.g., 1000 writes in 60 seconds) |
| Pros | Small file, fast recovery, minimal performance impact |
| Cons | Data between snapshots is lost (up to a few minutes) |

### AOF (Append-Only File)

**Log approach**: Every write command is appended to a log file. On restart, the log is replayed.

| fsync Policy | Description | Durability |
|-------------|-------------|-----------|
| `always` | fsync on every write | Safest, slowest |
| `everysec` | fsync every second (default) | Max 1 second of data loss |
| `no` | Let OS decide | Fastest, least safe |

| | Description |
|---|---|
| Pros | Minimal data loss (everysec loses at most 1 second) |
| Cons | Larger file size, slower replay on restart |

### Hybrid Persistence (Redis 4.0+)

AOF file starts with an embedded RDB snapshot, followed by incremental AOF commands. Best of both worlds: fast recovery + data completeness.

### How to choose?

| Scenario | Recommendation |
|----------|---------------|
| Pure cache, data loss acceptable | Disable persistence |
| Minor data loss tolerable | RDB |
| Data must not be lost | AOF (everysec) |
| Balance performance and safety | Hybrid persistence |
