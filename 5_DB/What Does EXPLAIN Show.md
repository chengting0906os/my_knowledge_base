下面給你 **面試等級、可直接背、可直接畫白板、可用在 MySQL / MariaDB 都通的版本**。保證你講完直接被判「對 SQL 真的有研究」。

## **🚀 EXPLAIN 怎麼解讀（面試用完整講法）**
EXPLAIN 會顯示 MySQL 實際執行查詢時的 **執行計畫**，核心目的：
找出效能瓶頸，例如：全表掃描、未使用索引、排序/temporary table。
下面用 **最強框架**拆 10 個欄位，逐項解釋。

## **🟦 1. id**
代表執行計畫中的「查詢階層」。
規則：

| id | 意義 |
| --- | --- |
| 相同 id | 同一層 JOIN，一起執行 |
| id 大的 | 優先執行（例如子查詢） |


講法（面試可用）：
id 越大表示越早被執行，通常子查詢 / derived table 的 id 會比較大。

## **🟦 2. select_type**
**最需要熟記**，面試必問。
常見值：

| select_type | 意義 |
| --- | --- |
| SIMPLE | 單純 SELECT（無子查詢） |
| PRIMARY | 最外層 SELECT |
| SUBQUERY | WHERE 或 SELECT 裡的子查詢 |
| DERIVED | FROM (...) 子查詢 → 會建立 temporary table |
| UNION | UNION 後的第二段以後 |
| DEPENDENT SUBQUERY | 子查詢依賴外層欄位（很慢） |


講法：
DERIVED 和 DEPENDENT SUBQUERY 最容易造成效能問題。

## **🟦 3. table**
表示當前正在處理哪一張表，如果是 `<derivedX>` → 表示子查詢產生的臨時表。
面試講法：
出現 `<derivedX>` 通常代表有 FROM 子查詢，意謂著會產生 temporary table（較耗效能）。

## **🟦 4. type（最重要：JOIN 型態 → 效能指標）**
**這欄是 EXPLAIN 的靈魂。**MySQL 官方效能由快到慢：

| type | 意義 | 效能 |
| --- | --- | --- |
| **system** | 只有一列 | 🔥 最快 |
| **const** | 用主鍵查一筆 | 🔥 |
| **eq_ref** | 唯一索引 JOIN | 🔥 |
| **ref** | 普通 index JOIN | 很快 |
| **range** | 用 index 做範圍查詢 | 快 |
| **index** | 全 index scan | 慢 |
| **ALL** | 全表掃描 | ❌ 最慢 |


面試的標準講法：
我最關注 type 欄位，因為它直接表示 MySQL 做了什麼搜尋方式。ALL 是最差情況，表示沒有用到任何索引。

## **🟦 5. possible_keys**
MySQL **可能**會用到的 index。
- 不代表一定會用
- None = 沒有任何 index 可用（通常設計不良）

## **🟦 6. key（真正使用的 index）**
這是你最該看的一欄。

| key | 意義 |
| --- | --- |
| NULL | 沒用 index（通常有問題） |
| idx_xxx | 實際使用的 index |


## **🟦 7. key_len**
MySQL 使用 index 的長度（bytes）。
面試講法：
key_len 越接近 index 長度越好，代表 index 有被完整使用（最佳化 JOIN 條件）。

## **🟦 8. ref**
顯示 JOIN 條件實際用到哪一列，例如：
## const
## table.column
如果看到：
## func
代表 index 沒被用（被 function 包住）。

## **🟦 9. rows**
MySQL 預估需要掃多少筆 row。
面試講法：
rows 越少越好，越大代表查詢成本越高，是我判斷效能問題的重要指標。

## **🟦 10. Extra（藏在這裡的都很關鍵）**
常見且重要的 Extra：

| Extra | 意義 |
| --- | --- |
| **Using index** | 覆蓋索引（最快） |
| **Using where** | 透過 index 過濾（正常） |
| **Using temporary** | 使用臨時表（GROUP BY / ORDER BY 常見） |
| **Using filesort** | 需要額外排序（ORDER BY 未走 index） |
| **Using index condition** | ICP → 還 OK |
| **Using join buffer** | JOIN 沒用索引 |


最危險的是：
- **Using temporary**
- **Using filesort**
- **Using join buffer**
- **ALL**

## **📌 最強面試回答示範（你可以直接背）**
我會從三個面向解讀 EXPLAIN：① **type**（JOIN 型態）② **key / key_len**（是否有效使用索引）③ **Extra**（是否有 temporary / filesort）
type 若是 ALL 表示全表掃描，需要 index。key 代表實際用哪個 index，若是 NULL 表示沒用到。Extra 如果出現 Using temporary 或 Using filesort，代表 GROUP BY 或 ORDER BY 沒走 index，通常是效能瓶頸。
select_type 出現 DERIVED 或 DEPENDENT SUBQUERY 通常也意味著需要重寫 SQL 才能最佳化。
這一段講出來 → 面試官直接知道你真的懂。

## **📚 要不要我幫你做「EXPLAIN 面試教材」？**
我可以做一份：
✔ 一張圖總結 EXPLAIN 所有欄位✔ 面試時的標
