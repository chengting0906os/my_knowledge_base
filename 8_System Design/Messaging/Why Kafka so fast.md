# Why Kafka so fast

## 一句話

Kafka 快的核心是：`順序寫入磁碟` + `零拷貝（zero-copy）`，再加上批次傳輸與作業系統 page cache。

## 順序寫入（Sequential Write）

- Kafka 的 partition 是 append-only log，資料基本上只是在檔案尾端追加。
- 順序 I/O 比隨機 I/O 成本低很多，磁碟吞吐更高。
- Kafka 避免了傳統 queue 常見的頻繁隨機更新，寫入路徑更短、更穩定。

## 零拷貝（Zero-Copy）

- Kafka 傳資料給 consumer 時可用 `sendfile`，盡量不把資料搬到 user space。
- 傳統路徑（非 zero-copy）通常是：`disk -> kernel buffer(page cache) -> user buffer -> kernel socket buffer -> NIC (Network Interface Card, 網路介面卡)`。
- `sendfile` 路徑可簡化成：`disk -> kernel buffer(page cache) -> kernel socket buffer -> NIC`（省掉 user buffer 來回拷貝）。
- 重點不是「完全 0 次拷貝」，而是大幅減少 user/kernel 之間的資料搬移與 context switch。
- 結果是 CPU 更省、每秒可處理更多資料，尤其在大流量傳輸時效果明顯。

## The Message Flow with Zero-Copy

```text
Producer Side:
Producer -> Network -> Kafka Broker
                     -> Append to partition log
                     -> OS page cache
                     -> Flush to disk (log segment)

Consumer Side (zero-copy path):
Consumer fetch request -> Kafka Broker
                        -> locate log segment / offset
                        -> FileChannel.transferTo() (sendfile)
                        -> page cache (or disk if cache miss) -> socket -> NIC
                        -> Consumer
```

- `transferTo()` 主要發生在 broker 回傳資料給 consumer 的 fetch 路徑。
- 並非每次都要碰磁碟；命中 page cache 時可直接送網路，未命中才回 disk。

### Consumer Fetch 詳細步驟（面試可直接講）
- Consumer 發 fetch request：`Give me messages from offset 1000, max 1MB`
- Broker 找到包含該 offset 的 log segment 檔案
- Broker 計算檔案位置（position）與長度（length）
- Broker 呼叫 `FileChannel.transferTo()`，底層走 `sendfile()`
- OS 透過 DMA：`disk -> kernel buffer(page cache)`
- OS 透過 DMA：`kernel buffer -> NIC`
- Data arrives at consumer

## 30 秒口說版

Kafka 之所以快，第一是它用 append-only log 做順序寫入，磁碟吞吐很高；第二是傳輸時用 zero-copy，減少 CPU 拷貝與 context switch。再配合批次與 page cache，所以在高流量事件流場景下吞吐量特別好。

## 參考資料

- https://www.linkedin.com/pulse/kafkas-zero-copy-architecture-behind-lightning-fast-message-konar-prw1c/
- https://ithelp.ithome.com.tw/m/articles/10218166
