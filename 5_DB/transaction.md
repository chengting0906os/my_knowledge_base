# Transaction：MySQL vs PostgreSQL（大概版）

## 名詞對照（中英）

- `DML (Data Manipulation Language, 資料操作語言)`：`INSERT / UPDATE / DELETE`（有些情境也含 `SELECT`）
- `DDL (Data Definition Language, 資料定義語言)`：`CREATE / ALTER / DROP`
- `MVCC (Multi-Version Concurrency Control, 多版本並行控制)`
- `Implicit Commit`：隱式提交（系統自動幫你 `COMMIT`）
- `Atomic DDL`：DDL 要嘛全成功、要嘛全失敗（避免半套狀態）

## MySQL（以 InnoDB 為主）

- `BEGIN / COMMIT / ROLLBACK` 主要保護 `DML (Data Manipulation Language)`
- 預設隔離級別通常是 `REPEATABLE READ`
- 用 `MVCC (Multi-Version Concurrency Control) + next-key lock` 降低幻讀
- 很多 `DDL (Data Definition Language)` 會觸發 `implicit commit`（前後自動提交）
- MySQL 8 有 `Atomic DDL`（崩潰一致性更好），但不代表你可在同一交易裡隨意 `ROLLBACK DDL`
- 記法：MySQL 比較偏 `statement-level atomicity`（單一 DDL 指令層級）

## PostgreSQL

- `BEGIN / COMMIT / ROLLBACK` 對 `DML` 很完整
- 預設隔離級別是 `READ COMMITTED`
- 也用 `MVCC`，但鎖模型與 MySQL 不同（無 `next-key lock` 這套）
- 大多數 `DDL` 可放在 `transaction` 內，失敗可整包回滾
- 記法：PostgreSQL 比較偏 `transaction-level atomicity`（同一交易內多個步驟一起成功/失敗）

## PostgreSQL 可以回滾表結構嗎？

可以，**大多數表結構變更可以回滾**，例如：

```sql
BEGIN;
ALTER TABLE users ADD COLUMN age int;
ROLLBACK; -- 欄位不會真的留下
```

但有少數指令本來就不能在 transaction block 內執行（例如部分系統層級指令），這種就談不上用 `ROLLBACK` 回滾。
