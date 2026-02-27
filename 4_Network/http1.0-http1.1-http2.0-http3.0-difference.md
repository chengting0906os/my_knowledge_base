# HTTP/1.0 vs HTTP/1.1 vs HTTP/2 vs HTTP/3

## Quick Comparison

| Version  | Transport       | Key Improvement                                                         | Main Limitation                                                                 |
| -------- | --------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| HTTP/1.0 | TCP             | Introduced status code + headers + `Content-Type`                       | Typically one request per connection, high overhead                             |
| HTTP/1.1 | TCP             | Persistent connection (reuse), `Host`, better caching, chunked transfer | Still text-based; request/response ordering constraints; HOL issues in practice |
| HTTP/2   | TCP             | Binary framing, multiplexing, header compression                        | TCP packet loss can still block streams (TCP-level HOL)                         |
| HTTP/3   | QUIC (over UDP) | Keeps HTTP semantics, reduces latency, per-stream loss handling         | Requires QUIC support on both ends                                              |

## HTTP/1.0 (Building Extensibility)

- Added explicit version info in request line (e.g. `HTTP/1.0`).
- Added status line in response (e.g. `200 OK`).
- Introduced request/response headers.
- `Content-Type` made it possible to transfer non-HTML content.
- In typical use, each request often opened a new TCP connection.

## HTTP/1.1 (Standardized Protocol)

- Connection reuse (persistent connection / keep-alive) became practical default behavior.
- Added/standardized important mechanisms:
  - `Host` header (virtual hosting on same IP)
  - Additional cache control mechanisms were introduced (for example `Cache-Control`, `ETag`)
  - Chunked transfer
  - Pipelining (historically defined, limited real-world usage)
- Browser behavior note:
  - In HTTP/1.x, browsers limit concurrent connections per domain (commonly around 6 in modern practice).
  - Extra requests may queue, which is one reason heavy pages felt slower under HTTP/1.1.
  - Domain sharding was once used to bypass this limit, but is generally an anti-pattern with HTTP/2+.
- Big improvement over 1.0, but still has performance bottlenecks for modern heavy pages.

## HTTP/2 (Performance-Oriented)

- Changed wire format from text to binary framing.
- Multiplexing: multiple streams on one connection.
- Header compression reduces repeated metadata overhead.
- Keeps HTTP semantics (methods/status codes), but improves transport efficiency.
- Note: Because it runs over TCP, packet loss can still cause TCP-level head-of-line blocking.

### What Is TCP-level HOL?

- HOL = Head-of-Line blocking.
- In TCP, bytes must be delivered in order.
- If one packet is lost, later packets may arrive but cannot be delivered to upper layers until the lost packet is retransmitted.
- In HTTP/2, many streams share one TCP connection, so one packet loss can temporarily stall multiple streams on that connection.

## HTTP/3 (HTTP over QUIC)

- Keeps the same HTTP semantics as previous versions.
- Uses QUIC instead of TCP at transport layer.
- QUIC handles loss/retransmission per stream, so one stream's packet loss is less likely to block all streams.
- Main goal: lower latency and better behavior on unstable networks.
- HTTP/3 can reduce connection setup latency because QUIC integrates transport and TLS handshakes.
- The real-world gain varies by network quality, server/CDN configuration, and whether the connection is reused.
- Supports 0-RTT in resumed sessions:
  - Client may send data earlier without waiting for a full handshake round trip.
  - This can reduce TTFB in some reconnect scenarios.
  - 0-RTT data has replay risk, so avoid non-idempotent operations.

## Practical Interview Notes

- In most cases, you do not pick HTTP version per request in application code.
- You usually configure what versions the server/CDN supports, and the client/server then negotiate the final version (for example via ALPN).
- HTTP/2 and HTTP/3 are mainly performance upgrades, not a change to REST semantics.
- Real-world tests (including reports shared by engineers from CDN providers such as Cloudflare) sometimes show only small speed differences between HTTP/2 and HTTP/3.
- This can be related to congestion control algorithm, packet loss pattern, RTT, and deployment details.
- If asked "biggest jump":
  - 1.1 -> 2: multiplexing + binary framing + header compression
  - 2 -> 3: QUIC transport to reduce TCP-level HOL impact + integrated TLS 1.3 handshake for faster setup

## 30s Interview Version

- HTTP/1.0 introduced the core structure: version, status code, headers, and content type.
- HTTP/1.1 improved connection reuse and standardization (`Host`, caching, chunked transfer).
- HTTP/2 improved performance with binary framing, multiplexing, and header compression over TCP.
- HTTP/3 keeps HTTP semantics but runs on QUIC (UDP), reducing latency and stream-blocking issues under packet loss.

---

## 中文版

## 快速比較

| 版本     | 傳輸層         | 主要改進                                                   | 主要限制                            |
| -------- | -------------- | ---------------------------------------------------------- | ----------------------------------- |
| HTTP/1.0 | TCP            | 建立狀態碼、Header、`Content-Type` 等核心結構              | 常見情況是一個請求一條連線，開銷高  |
| HTTP/1.1 | TCP            | 連線重用（keep-alive）、`Host`、快取控制、chunked transfer | 仍是文字協定；在實務上仍有 HOL 問題 |
| HTTP/2   | TCP            | Binary framing、多工（multiplexing）、Header 壓縮          | 仍受 TCP 封包遺失影響（TCP 層 HOL） |
| HTTP/3   | QUIC（UDP 上） | 保留 HTTP 語意並降低延遲、以 stream 為單位處理遺失         | 需要雙端支援 QUIC                   |

## HTTP/1.0（可擴充基礎期）

- 在請求列中明確帶版本（例如 `HTTP/1.0`）。
- 回應有狀態列（例如 `200 OK`）。
- 引入 request/response headers。
- `Content-Type` 讓非 HTML 內容可被正確傳輸。
- 常見使用模式是一個請求開一條 TCP 連線。

## HTTP/1.1（標準化與實用化）

- 連線重用（persistent connection / keep-alive）成為實務主流。
- 強化與標準化機制：
  - `Host` header（同 IP 多網站）
  - 新增並強化快取控制機制（例如 `Cache-Control`、`ETag`）
  - Chunked transfer
  - Pipelining（規範存在，但實務使用有限）
- 瀏覽器行為補充：
  - 在 HTTP/1.x 下，瀏覽器會限制每個網域的並行連線數（現代實務常見約 6 條）。
  - 超過限制的請求會排隊，這也是 HTTP/1.1 在重資源頁面較慢的原因之一。
  - 過去曾用 domain sharding 繞過限制，但在 HTTP/2+ 通常被視為反模式。
- 相比 1.0 大幅進步，但面對現代大型頁面仍有效能瓶頸。

## HTTP/2（效能優化期）

- 線路格式由文字改為二進位分幀（binary framing）。
- 多工：同一連線可同時跑多個 stream。
- Header 壓縮降低重複傳輸成本。
- HTTP 語意（method/status code）不變，但傳輸效率更好。
- 由於底層仍是 TCP，封包遺失時仍可能出現 TCP 層 HOL。

### 什麼是 TCP 層 HOL？

- HOL = Head-of-Line blocking（隊首阻塞）。
- TCP 必須保序交付資料。
- 如果前面某個封包遺失，後面的封包就算先到，也要等前面遺失封包重傳成功後才能往上交付。
- 在 HTTP/2 中，多個 stream 共用同一條 TCP 連線，因此一次丟包可能暫時卡住同連線上的多個 stream。

## HTTP/3（HTTP over QUIC）

- 維持既有 HTTP 語意。
- 傳輸層改用 QUIC（非 TCP）。
- QUIC 以 stream 為單位處理重傳，單一 stream 丟包較不會拖慢全部 stream。
- 核心目標是更低延遲、在不穩定網路下有更好表現。
- HTTP/3 因為 QUIC 將傳輸與 TLS 握手整合，通常可降低連線建立延遲。
- 但實際提升幅度會受網路品質、伺服器/CDN 設定與連線是否重用影響。
- 支援 0-RTT（Zero Round Trip Time，通常發生在連線重用/重連）：
  - 客戶端可在完整握手完成前提早送出資料。
  - 在部分重連情境下可降低首位元組時間（TTFB）。
  - 0-RTT 有 replay 風險，不適合非冪等操作。

## 30 秒面試版

- HTTP/1.0 建立了版本、狀態碼、Header、`Content-Type` 等核心結構。
- HTTP/1.1 強化連線重用與標準化（`Host`、快取、chunked transfer）。
- HTTP/2 在 TCP 上加入 binary framing、多工與 header 壓縮，提升效能。
- HTTP/3 保留 HTTP 語意但改跑 QUIC（UDP），核心是降低 TCP 層 HOL 影響，並透過整合 TLS 與支援 0-RTT 來縮短連線啟動時間。
- 補充：實測上 HTTP/3 沒有明顯快於 HTTP/2

## REF

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Evolution_of_HTTP
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP_1.x
- https://developer.mozilla.org/en-US/docs/Glossary/Domain_sharding
- https://datatracker.ietf.org/doc/html/rfc9112
- https://datatracker.ietf.org/doc/html/rfc9113
- https://datatracker.ietf.org/doc/html/rfc9114

- https://medium.com/@bharathofficial05/http-2-vs-http-3-6adb15a8ffae
