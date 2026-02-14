# What is LSM Tree

LSM Tree（Log-Structured Merge-Tree）是一種針對高寫入吞吐設計的儲存結構，核心做法是「先快寫、再背景合併」。

## How it works

- Write path: 先寫 `WAL`（確保持久化）與 `MemTable`（記憶體排序結構）
- Flush: `MemTable` 滿了後落盤成不可變的 `SSTable`
- Compaction: 背景把多層 SST 合併，清理舊版本與 tombstone
- Read path: 查詢會先看 MemTable，再看較新的 SST，並配合 Bloom Filter/Index 減少 I/O

## Why use it

- 寫入多為順序 I/O，吞吐高
- 對大規模寫入與 disk-based 儲存友善

## Trade-offs

- Compaction 會吃 CPU/I/O，可能造成延遲抖動
- 讀取路徑較複雜，調參成本高
- 空間放大、寫放大需要管理

## Common systems

- RocksDB
- LevelDB
- Cassandra（變體）
- HBase（變體）

## Interview one-liner

LSM Tree 是用「先寫記憶體+WAL、再背景合併到 SST」換取高寫入吞吐的結構，代價是 compaction 帶來的讀寫放大與延遲抖動。

## 參考資料

https://medium.com/@thegiive/lsm-tree-%E4%BB%8B%E7%B4%B9-3dc32873fa66
https://www.scylladb.com/glossary/log-structured-merge-tree/
