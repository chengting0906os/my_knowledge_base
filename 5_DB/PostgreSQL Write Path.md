# PostgreSQL 寫入資料的完整過程

以 PostgreSQL 為例，資料從應用程式寫入到真正存到磁碟，經過以下幾個階段：

---

## 1. 應用程式發送 SQL

```python
# 例如 Python 用 psycopg2
conn = psycopg2.connect("dbname=mydb user=postgres")
cur = conn.cursor()
cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 30))
conn.commit()
```

---

## 2. Parser & Planner

PostgreSQL 收到 SQL 字串後：

- **Parser**：把 SQL 字串解析成語法樹
- **Planner/Optimizer**：決定最佳執行計劃（要不要用 index、用哪種 join 等）
- **Executor**：執行計劃

---

## 3. 寫入 WAL（Write-Ahead Log）

這是 PostgreSQL 保證資料不丟失的核心機制。**資料在真正寫入資料頁之前，先寫入 WAL log**。

```
WAL (pg_wal/)
└── 000000010000000000000001  ← 順序寫入的 log 檔
```

WAL 是順序寫入，比隨機寫入快很多。若系統崩潰，重啟時可以用 WAL 重播還原資料。

---

## 4. 寫入 Shared Buffer（記憶體）

實際的資料頁（data page，每頁 8KB）被載入到 **Shared Buffer**（記憶體中的 buffer pool）。

```
Shared Buffer（RAM）
└── Page: users 的某個 8KB 資料頁
    └── 插入 ("Alice", 30) 這筆 tuple
```

此時這個頁面變成 **dirty page**（已修改但還未寫到磁碟）。

---

## 5. COMMIT

當應用程式呼叫 `commit()`：

- WAL 的這筆 transaction 被標記為 committed 並 **fsync 到磁碟**
- 但 **data page 不一定馬上寫到磁碟**，可能還留在 Shared Buffer

---

## 6. Checkpointer 寫入磁碟

PostgreSQL 的背景程式 **checkpointer** 定期把 Shared Buffer 中的 dirty pages 寫回磁碟的實際資料檔：

```
資料檔（$PGDATA/base/）
└── 16384/          ← database OID
    └── 24601       ← table 的資料檔
        └── 8KB pages，存放實際的 tuple
```

---

## 整體流程圖

```
應用程式 SQL
    ↓
Parser → Planner → Executor
    ↓
WAL log 寫入（fsync，保證持久性）
    ↓
Shared Buffer（dirty page，記憶體）
    ↓         ← commit 就回傳成功
Checkpointer 定期刷到磁碟
    ↓
磁碟資料檔（pg_data/base/...）
```

---

## 關鍵設計原則

**WAL 先於 data** 的設計叫做 **Write-Ahead Logging**，保證即使 commit 後系統當掉，重啟時可以從 WAL 重播，資料不會丟失，但不需要每次 commit 都等 data page 寫到磁碟，大幅提升效能。
