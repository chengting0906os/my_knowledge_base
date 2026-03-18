# What is Redis

## 中文版

Redis（Remote Dictionary Server）是一個**記憶體內的資料結構儲存**，可作為資料庫、快取、訊息佇列使用。

### 核心特性
- **單執行緒**（命令執行層）：避免鎖競爭，每個命令原子執行
- **記憶體儲存**：讀寫速度極快（微秒級）
- **持久化可選**：RDB / AOF（見 Redis Persistence）
- **豐富的資料結構**

### 支援的資料結構

| 類型 | 使用場景 |
|------|----------|
| **String** | 快取、計數器、分散式鎖 |
| **Hash** | 使用者資料、物件屬性 |
| **List** | 訊息佇列、最新動態 |
| **Set** | 標籤、去重、交集運算 |
| **Sorted Set (ZSet)** | 排行榜、延遲任務 |
| **Bitmap** | 簽到、布林標記 |
| **HyperLogLog** | 近似計數（UV 統計） |
| **Stream** | 訊息流、消費者群組 |

### 為什麼 Redis 快？
1. 資料全在記憶體，無磁碟 I/O
2. 單執行緒無鎖，無 context switch
3. 高效的資料結構實作
4. 非阻塞 I/O（epoll / kqueue）

## English Version

Redis (Remote Dictionary Server) is an **in-memory data structure store** used as a database, cache, and message broker.

### Core Characteristics
- **Single-threaded** (command execution): no lock contention; every command is atomic
- **In-memory storage**: extremely fast reads and writes (microsecond latency)
- **Optional persistence**: RDB / AOF (see Redis Persistence)
- **Rich data structures**

### Supported Data Structures

| Type | Use Cases |
|------|-----------|
| **String** | Caching, counters, distributed locks |
| **Hash** | User data, object attributes |
| **List** | Message queues, recent activity feeds |
| **Set** | Tags, deduplication, intersection operations |
| **Sorted Set (ZSet)** | Leaderboards, delayed task scheduling |
| **Bitmap** | Daily check-ins, boolean flags |
| **HyperLogLog** | Approximate counting (unique visitor stats) |
| **Stream** | Message streams, consumer groups |

### Why is Redis fast?
1. All data lives in memory — no disk I/O
2. Single-threaded — no locks, no context switching
3. Highly optimized data structure implementations
4. Non-blocking I/O (epoll / kqueue)
