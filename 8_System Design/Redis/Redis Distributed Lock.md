# Redis Distributed Lock

## 中文版

### 為什麼需要分散式鎖？

單機可以用 `threading.Lock` 或 DB transaction 控制並發。
多服務、多實例時，這些方式無效——需要一個所有節點都能看到的共享鎖。

### 基本實作：SET NX PX

```redis
SET lock_key unique_value NX PX 30000
```

| 參數 | 說明 |
|------|------|
| `NX` | 只有 key 不存在時才設定（原子性搶鎖） |
| `PX 30000` | 過期時間 30 秒（防止死鎖） |
| `unique_value` | 每個持鎖者用唯一值（UUID），防止誤刪他人的鎖 |

**釋放鎖（用 Lua 腳本保證原子性）**：
```lua
if redis.call("GET", KEYS[1]) == ARGV[1] then
    return redis.call("DEL", KEYS[1])
else
    return 0
end
```

不能先 GET 再 DEL，因為兩步之間可能鎖已被別人拿走。

### 常見問題

| 問題 | 說明 | 解法 |
|------|------|------|
| 鎖提前過期 | 業務還沒跑完，TTL 就到了 | Watchdog 機制自動續期（Redisson） |
| 誤刪別人的鎖 | 過期後被別人拿走，自己又來 DEL | 用 unique_value + Lua 腳本驗證 |
| Redis 單點故障 | Master 掛掉，Slave 還沒同步 | Redlock 演算法 |

### Redlock（多節點分散式鎖）

用 N 個（通常 5 個）**獨立** Redis 節點：

1. 記錄當前時間 `t1`
2. 依序對 N 個節點嘗試 SET NX PX
3. 若在 `TTL` 內取得超過 `N/2 + 1` 個鎖 → 加鎖成功
4. 實際有效時間 = TTL - (當前時間 - t1)
5. 任一步驟失敗 → 對所有節點釋放鎖

**Redlock 的爭議**：Martin Kleppmann 認為在 GC pause 或時鐘漂移下仍不安全；Antirez（Redis 作者）反駁其假設過於嚴格。實務上多數場景用單節點 + Watchdog 已足夠。

### 實務選擇

| 場景 | 建議 |
|------|------|
| 容許極低機率重複執行 | 單節點 SET NX + 冪等設計 |
| 嚴格不能重複 | Redlock 或改用 ZooKeeper / etcd |
| 高併發 + 強一致性 | 考慮 DB 行級鎖（SELECT FOR UPDATE） |

---

## English Version

### Why Distributed Locks?

Single-process locks (`threading.Lock`, DB transactions) don't work across multiple services or instances. A distributed lock needs to be visible to all nodes via a shared external store.

### Basic Implementation: SET NX PX

```redis
SET lock_key unique_value NX PX 30000
```

| Option | Description |
|--------|-------------|
| `NX` | Only set if key doesn't exist (atomic acquire) |
| `PX 30000` | 30-second TTL (prevents deadlock on crash) |
| `unique_value` | UUID per lock holder — prevents deleting someone else's lock |

**Releasing the lock (Lua script for atomicity)**:
```lua
if redis.call("GET", KEYS[1]) == ARGV[1] then
    return redis.call("DEL", KEYS[1])
else
    return 0
end
```

A GET-then-DEL approach is unsafe — another process might acquire the lock between the two commands.

### Common Pitfalls

| Problem | Description | Solution |
|---------|-------------|---------|
| Lock expires early | TTL runs out before business logic finishes | Watchdog auto-renewal (e.g., Redisson) |
| Deleting someone else's lock | Lock expired, re-acquired by another, then original deletes it | Validate with unique_value + Lua script |
| Redis single-node failure | Master crashes before replicating to replica | Redlock algorithm |

### Redlock (Multi-Node Distributed Lock)

Uses N independent Redis nodes (typically 5):

1. Record current time `t1`
2. Attempt `SET NX PX` on all N nodes sequentially
3. If `N/2 + 1` locks acquired within TTL → lock is held
4. Effective TTL = TTL - (current_time - t1)
5. On failure → release all acquired locks

**Controversy**: Martin Kleppmann argues Redlock is unsafe under GC pauses or clock drift. Antirez (Redis author) disputes the assumptions. In practice, single-node + idempotency is sufficient for most use cases.

### Practical Guidance

| Scenario | Recommendation |
|----------|---------------|
| Low-probability duplicate execution OK | Single-node SET NX + idempotent design |
| Strictly no duplicates | Redlock or ZooKeeper / etcd |
| High-concurrency + strong consistency | DB row-level lock (SELECT FOR UPDATE) |
