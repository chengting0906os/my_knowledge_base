# TCP vs UDP

## 中文版

| | TCP | UDP |
|---|---|---|
| 連線 | 需要三次握手（有狀態） | 無連線（無狀態） |
| 可靠性 | 保證送達、順序、不重複 | 不保證，封包可能遺失或亂序 |
| 速度 | 較慢（有握手、ACK、重傳） | 較快（直接送） |
| 流量控制 | 有（壅塞控制） | 無 |
| 使用場景 | HTTP、Email、FTP、資料庫 | 直播、線上遊戲、DNS、VoIP |

**核心差異**：TCP 重可靠，UDP 重速度。

**使用場景判斷**：
- 資料不能遺失 → TCP（金融交易、文件傳輸）
- 低延遲比正確率更重要 → UDP（遊戲、即時通訊）
- DNS 查詢 → UDP（快速，遺失了重查即可）

## English Version

| | TCP | UDP |
|---|---|---|
| Connection | 3-way handshake (stateful) | Connectionless (stateless) |
| Reliability | Guaranteed delivery, ordering, no duplicates | No guarantee — packets may be lost or reordered |
| Speed | Slower (handshake, ACK, retransmission) | Faster (fire and forget) |
| Flow control | Yes (congestion control) | No |
| Use cases | HTTP, Email, FTP, Databases | Live streaming, online gaming, DNS, VoIP |

**Core trade-off**: TCP prioritizes reliability; UDP prioritizes speed.

**When to choose**:
- Data must not be lost → TCP (financial transactions, file transfers)
- Low latency matters more than accuracy → UDP (gaming, real-time comms)
- DNS queries → UDP (fast; if lost, just retry)
