- Object Relational Mapping
- 有 ORM 時，ORM 會將資料表對映為類別（class），將資料列（row）對映為該類別的物件實例（object instance）
- 以物件導向的方式操作資料庫，通常不必直接寫 SQL 語句，除非是複雜操作
- 可以提高開發時的可讀性
- ORM 通常透過參數綁定（parameter binding）產生 SQL，因此**可降低 SQL Injection 風險**
- 轉移資料庫時有好處，ORM 可減少與資料庫互動層的修改量，但還是需注意到不同資料庫間的差異，比如在 Django ORM 中，JSONField 在 PostgreSQL 預設對應 jsonb，而在 MySQL 則對應 JSON 
- 效能通常會較慢，以我個人曾經測過會慢到 50%
- 需要注意 N + 1 問題


https://www.geeksforgeeks.org/dbms/what-is-object-relational-mapping-orm-in-dbms/
