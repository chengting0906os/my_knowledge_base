
# What is RocksDB

RocksDB 是一個嵌入式（embedded）高效能 key-value 儲存引擎，由 Facebook 基於 LevelDB 發展而來，適合高寫入吞吐、可落盤（disk-based）的場景。

## 核心特性
- `LSM-tree` 架構：寫入先進記憶體，再背景合併到磁碟
- `WAL`（Write-Ahead Log）：先記錄日誌，提升 crash recovery 能力
- `SSTable`：磁碟上不可變且排序好的檔案
- 高可調參：可依 workload 調整 compaction、cache、block size 等

## 為什麼快
- 寫入多為順序寫（memtable + WAL），減少隨機 I/O
- 背景 `flush/compaction` 整理資料，維持長期讀寫效率
- 讀取可配合 `block cache` 與 `Bloom filter` 降低磁碟存取

## Trade-offs
- compaction 會消耗 CPU / I/O，可能造成延遲抖動
- 讀路徑較複雜，調參成本高於簡單記憶體 KV
- 極低延遲要求場景下，純記憶體系統可能更有優勢

## 適用場景
- 需要大容量且成本可控的 KV 儲存
- 寫入量大、可接受最終在磁碟持久化
- 作為上層系統引擎（例如 Kvrocks、狀態儲存、事件索引）

## 面試一句話
RocksDB 是一個基於 LSM-tree 的嵌入式 KV 引擎，透過「順序寫入 + 背景 compaction」在 disk-based 架構下取得高寫入吞吐，但代價是 compaction 帶來的複雜度與延遲抖動。

## 參考資料
- https://medium.com/%E9%AB%94%E9%A9%97%E4%BA%BA%E7%94%9F-touch-life/rocksdb-overview-110bf8eaaea9
