# Isolation Level（大概版）

## 先記三個問題

- `Dirty Read`：讀到別的交易還沒 `COMMIT` 的資料
- `Non-repeatable Read`：同一交易內，同一筆資料前後讀到不同值
- `Phantom Read`：同一交易內，同條件查詢，第二次多/少了幾筆

## SQL 標準四種隔離級別（由弱到強）

1. `READ UNCOMMITTED`
2. `READ COMMITTED`
3. `REPEATABLE READ`（預設）
4. `SERIALIZABLE`

## 隔離等級異常對照表

| 隔離等級           | Dirty Read                            | Nonrepeatable Read | Phantom Read                     | Serialization Anomaly |
| ------------------ | ------------------------------------- | ------------------ | -------------------------------- | --------------------- |
| `READ UNCOMMITTED` | 允許（但 PG 會當成 `READ COMMITTED`） | 可能               | 可能                             | 可能                  |
| `READ COMMITTED`   | 不可能                                | 可能               | 可能                             | 可能                  |
| `REPEATABLE READ`  | 不可能                                | 不可能             | SQL 標準允許（但 PG 中通常不會） | 可能                  |
| `SERIALIZABLE`     | 不可能                                | 不可能             | 不可能                           | 不可能                |

## PostgreSQL 實際可用層級（重點）

PostgreSQL 實際上可視為 3 層：

1. `READ COMMITTED`（預設）
2. `REPEATABLE READ`
3. `SERIALIZABLE`

補充：`READ UNCOMMITTED` 在 PostgreSQL 會被當成 `READ COMMITTED`。

## MySQL vs PostgreSQL（面試版）

- MySQL（InnoDB）預設：`REPEATABLE READ`
- PostgreSQL 預設：`READ COMMITTED`
- PostgreSQL 實際可用 3 層（`READ UNCOMMITTED` 會等同 `READ COMMITTED`）

## 各級別大概效果

- `READ UNCOMMITTED`：可能有 Dirty Read（實務很少用）
- `READ COMMITTED`：避免 Dirty Read，但可能 Non-repeatable/Phantom
- `REPEATABLE READ`：同筆資料重讀一致；MySQL 透過 next-key lock 也能壓制 Phantom
- `SERIALIZABLE`：最安全但最保守，衝突與等待成本最高

## PostgreSQL 補充

- 主要靠 `MVCC (Multi-Version Concurrency Control)` 提供一致快照
- `SERIALIZABLE` 可能出現 serialization failure，需要應用程式重試

## 常用 SQL

```sql
-- 查目前隔離級別
SHOW TRANSACTION ISOLATION LEVEL;

-- 設定目前交易隔離級別（PostgreSQL）
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- SQL...
COMMIT;
```

## 一句話總結

隔離級別是在「一致性」和「併發效能」之間做取捨：越嚴格越安全，但吞吐通常越差。
