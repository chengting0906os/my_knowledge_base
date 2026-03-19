# Redis Cache Patterns

## 中文版

### Cache Aside（旁路快取）— 最常用

```
讀：先查 Cache → miss → 查 DB → 寫入 Cache → 回傳
寫：更新 DB → 刪除 Cache（讓下次讀時重新載入）
```

- 應用程式自己管理快取
- Cache 只存被讀過的資料（Lazy Loading）
- **刪除 vs 更新**：寫時要刪除 key，不要直接更新 Cache
  - **更新的問題**：T1 寫 DB=100、T2 寫 DB=200，若 T2 先更新 Redis（200）、T1 後更新 Redis（100），結果 DB=200 但 Redis=100，不一致。Redis 的值由「誰最後寫 Redis」決定，不一定跟「誰最後寫 DB」一致。
  - **刪除的做法**：兩者都只是刪掉 key，Redis 變空。下一次讀去 DB 查，永遠拿到最新值再存回 Cache。Redis 的值由「下一次讀 DB」決定，必然正確。

### Write Through（直寫）

```
寫：同時寫 Cache + DB（同步）
讀：先查 Cache → miss → 查 DB
```

- Cache 永遠與 DB 一致
- 缺點：寫入延遲變高（需等 DB）；冷資料也會寫進 Cache

### Write Behind / Write Back（非同步回寫）

```
寫：只寫 Cache → 非同步批次刷回 DB
讀：先查 Cache
```

- 寫入效能最好
- 缺點：Cache 若在刷回前崩潰，資料遺失

### Read Through

```
讀：查 Cache → miss → Cache 自動查 DB 並填入 → 回傳
```

- 應用程式只跟 Cache 互動，Cache 層負責填充
- 常見於 ORM 或 Cache 框架實作

### 快取一致性問題

| 問題 | 說明 | 解法 |
|------|------|------|
| 快取穿透 | 查詢不存在的 key，每次都打到 DB | 快取空值或用 Bloom Filter |
| 快取擊穿 | 熱點 key 過期，瞬間大量請求打到 DB | 加互斥鎖（Mutex）重建，或設定較長 TTL |
| 快取雪崩 | 大量 key 同時過期 | 隨機化 TTL，熱點 key 設永不過期 |

## English Version

### Cache Aside — Most Common

```
Read:  Check Cache → miss → Query DB → Write to Cache → Return
Write: Update DB → Delete Cache (reload lazily on next read)
```

- Application manages the cache explicitly
- Only data that has been read is cached (Lazy Loading)
- **Delete vs Update on write**: deletion is safer than updating — avoids race conditions writing stale values

### Write Through

```
Write: Write to Cache AND DB synchronously
Read:  Check Cache → miss → Query DB
```

- Cache always stays in sync with DB
- Cons: Higher write latency (must wait for DB); cold data also gets cached

### Write Behind / Write Back

```
Write: Write to Cache only → async batch flush to DB
Read:  Check Cache
```

- Best write performance
- Cons: Data loss if cache crashes before flushing

### Read Through

```
Read: Check Cache → miss → Cache fetches from DB and populates itself → Return
```

- Application only interacts with the cache layer
- Common in ORM or caching framework implementations

### Cache Consistency Issues

| Issue | Description | Solution |
|-------|-------------|---------|
| Cache Penetration | Querying non-existent keys hits DB every time | Cache null values or use Bloom Filter |
| Cache Breakdown | Hot key expires; massive requests hit DB simultaneously | Use mutex lock to rebuild, or set longer TTL |
| Cache Avalanche | Many keys expire at the same time | Randomize TTLs; set hot keys to never expire |
