# MySQL vs PostgreSQL

## Technical Comparison

- PostgreSQL 的物件層級是 `Databases -> Schemas -> Tables`。
- MySQL 的物件層級通常是 `Databases -> Tables`（沒有 PostgreSQL 那種 schema 階層）。

### Schema 的好處

- 可在同一個 database 內做邏輯分層（例如 `app`, `audit`, `reporting`），管理更清楚。
- 可做更細的權限控管（可以授權到 schema 層級）。
- 可讓不同模組使用同名資料表（不同 schema 下名稱可重複），減少命名衝突。
- 搭配 `search_path` 可控制物件解析順序，支援多租戶或環境隔離策略。

## 效能

- MySQL 在讀多（read-heavy）場景通常表現不錯，前提是索引與快取有調好。
- 簡單 `INSERT/UPDATE` 下，MySQL 常可和 PostgreSQL 打平。
- PostgreSQL 在複雜寫入、複雜查詢與高併發交易時，常更有優勢（MVCC 降低鎖競爭）。
- 兩者都很吃調校；在 OLTP 或分析型工作負載下，PostgreSQL 常可達到或超過 MySQL。
- 但有實測指出，MySQL 更新後效能反而下滑

## PostgreSQL 可擴展性（Extensibility）

- PostgreSQL 可擴展性佳：可自訂資料型別、函數、索引方法與 extension。
- PostgreSQL 支援更多索引型別（如 `B-tree`、`Hash`、`GIN`、`GiST`、`SP-GiST`、`BRIN`）。
- 社群與 extension 生態通常被認為更活躍，新功能與外掛選擇多。
- 常見 extension：`pg_trgm`、`postgis`、`pg_stat_statements`。
- 對中大型系統來說，當需求變複雜（全文檢索、地理空間、進階監控）時，通常更容易沿用同一套資料庫能力擴充。

## 參考

- https://www.youtube.com/watch?v=iWcskTGXM-o
- https://dev.to/outerbase/postgres-vs-mysql-14cp
- https://www.percona.com/blog/sakila-where-are-you-going/
