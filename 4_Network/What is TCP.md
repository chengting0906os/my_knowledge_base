# What is TCP

## English Version

### Definition

TCP (Transmission Control Protocol) is a transport-layer protocol that provides reliable, ordered, and full-duplex byte-stream communication between two endpoints.

### Core Characteristics

- Connection-oriented: communication starts after connection setup.
- Reliable delivery: lost data can be retransmitted.
- Ordered delivery: data is delivered in sequence.
- Flow control: receiver window helps prevent receiver overload.
- Congestion control: sender adapts rate based on network congestion.

### How TCP Reliability Works (High Level)

- Sequence numbers identify byte positions.
- ACKs confirm received data.
- Retransmission handles packet loss (for example after timeout or duplicate ACK signals).
- Checksum detects transmission corruption.

### TCP Connection Lifecycle

1. 3-way handshake (`SYN` -> `SYN-ACK` -> `ACK`)
2. Data transfer (bytes + ACKs, with flow/congestion control)
3. Connection close (typically `FIN/ACK` exchange, then `TIME-WAIT` behavior)

### Trade-offs

- Pros:
  - Reliable and ordered transport
  - Good for correctness-critical applications
- Cons:
  - More protocol overhead and latency than UDP in many cases
  - Head-of-line effects at TCP layer (in-order delivery requirement)

### Common Use Cases

- HTTP/1.1 and HTTP/2
- HTTPS (HTTP over TLS over TCP)
- SMTP, IMAP, POP3
- SSH, FTP

### 30s Interview Version

## TCP is a transport-layer protocol for reliable, ordered byte-stream communication. It uses handshake, sequence numbers, ACKs, retransmission, flow control, and congestion control to deliver data correctly.

## 中文版本

### 定義

TCP（Transmission Control Protocol，傳輸控制協定）是傳輸層協定，提供兩端之間「可靠、保序、全雙工」的位元組流傳輸。

### 核心特性

- 連線導向：先建立連線再傳資料。
- 可靠傳輸：封包遺失可重傳。
- 保序傳輸：資料依序交付給應用層。
- 流量控制：透過接收端視窗避免把對方塞爆。
- 壅塞控制：依網路擁塞狀態調整傳送速率。

### TCP 如何做到可靠（高層次）

- Sequence Number：標記資料位元組位置。
- ACK：確認已收到的資料範圍。
- Retransmission：逾時或重複 ACK 時重傳遺失資料。
- Checksum：偵測傳輸中的資料損毀。

### TCP 連線生命週期

1. 三向交握（`SYN` -> `SYN-ACK` -> `ACK`）
2. 資料傳輸（資料 + ACK，並套用流量/壅塞控制）
3. 連線關閉（常見 `FIN/ACK` 交換，並有 `TIME-WAIT`）

### 取捨

- 優點：
  - 傳輸可靠、順序正確
  - 適合資料正確性要求高的場景
- 缺點：
  - 相比 UDP，協定開銷與延遲通常較高
  - TCP 保序特性可能帶來隊首阻塞影響

### 常見使用場景

- HTTP/1.1、HTTP/2
- HTTPS（HTTP over TLS over TCP）
- SMTP、IMAP、POP3
- SSH、FTP

### 30 秒面試版

TCP 是傳輸層的可靠保序協定。它透過三向交握、序號、ACK、重傳、流量控制與壅塞控制，確保資料正確傳到對端。

## Ref (Professional Sources)

- RFC 9293 (IETF): Transmission Control Protocol (TCP)  
  https://datatracker.ietf.org/doc/html/rfc9293
- RFC 5681 (IETF): TCP Congestion Control  
  https://datatracker.ietf.org/doc/html/rfc5681
