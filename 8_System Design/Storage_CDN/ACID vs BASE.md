# ACID vs BASE

## 中文版

### ACID（關聯式資料庫的事務保證）

| 字母 | 名稱 | 說明 |
|------|------|------|
| **A** | Atomicity 原子性 | 事務內所有操作要麼全部成功，要麼全部回滾 |
| **C** | Consistency 一致性 | 事務前後資料庫都符合所有約束（如外鍵、唯一性） |
| **I** | Isolation 隔離性 | 並行事務互不干擾，效果如同序列執行 |
| **D** | Durability 持久性 | 事務提交後即使系統崩潰，資料也不會遺失（寫入磁碟） |

### BASE（NoSQL 的設計哲學）

| 縮寫 | 名稱 | 說明 |
|------|------|------|
| **BA** | Basically Available | 系統保證可用性，允許部分失敗 |
| **S** | Soft State | 狀態可以隨時間改變，即使沒有輸入（因為資料在同步中） |
| **E** | Eventually Consistent | 資料最終會達到一致，但不保證立即一致 |

### 對比

| | ACID | BASE |
|---|---|---|
| 一致性 | 強一致（立即） | 最終一致 |
| 可用性 | 有時犧牲可用性 | 優先保證可用性 |
| 效能 | 較低（鎖、rollback） | 較高 |
| 適合場景 | 金融、訂單、庫存 | 社交動態、購物車、推薦 |

## English Version

### ACID (Transaction guarantees in relational databases)

| Letter | Name | Description |
|--------|------|-------------|
| **A** | Atomicity | All operations in a transaction succeed or all are rolled back |
| **C** | Consistency | Database remains in a valid state before and after the transaction |
| **I** | Isolation | Concurrent transactions don't interfere — result is as if they ran serially |
| **D** | Durability | Committed data persists even after a system crash (written to disk) |

### BASE (NoSQL design philosophy)

| Acronym | Name | Description |
|---------|------|-------------|
| **BA** | Basically Available | System guarantees availability, tolerating partial failures |
| **S** | Soft State | State can change over time even without new input (data is propagating) |
| **E** | Eventually Consistent | Data will become consistent eventually, but not immediately |

### Comparison

| | ACID | BASE |
|---|---|---|
| Consistency | Strong (immediate) | Eventual |
| Availability | Sometimes sacrificed | Prioritized |
| Performance | Lower (locks, rollback overhead) | Higher |
| Use cases | Finance, orders, inventory | Social feeds, shopping carts, recommendations |
