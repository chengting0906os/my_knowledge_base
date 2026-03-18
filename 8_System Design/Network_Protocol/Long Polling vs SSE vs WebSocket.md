# Long Polling vs SSE vs WebSocket

## 中文版

三種讓伺服器即時推送資料給客戶端的技術。

| | Long Polling | SSE | WebSocket |
|---|---|---|---|
| 協定 | HTTP | HTTP | WS（升級自 HTTP） |
| 方向 | 半雙工（模擬推送） | 單向（Server → Client） | 全雙工 |
| 連線 | 每次回應後重新建立 | 持久連線 | 持久連線 |
| 瀏覽器支援 | 全支援 | 全支援（IE 除外） | 全支援 |
| 複雜度 | 低 | 低 | 中 |
| 使用場景 | 舊系統相容 | 通知、Feed、股票行情 | 聊天、協作、遊戲 |

**Long Polling**：客戶端發 request → 伺服器 hold 住直到有資料 → 回傳後客戶端立刻再發下一個 request。

**SSE**：伺服器透過一條持久的 HTTP 連線持續推送文字事件，客戶端只能收不能傳（單向）。

**WebSocket**：一次 HTTP upgrade 後切換為 WS 協定，雙向實時通訊，適合需要頻繁雙向交換的場景。

## English Version

Three techniques for pushing real-time data from server to client.

| | Long Polling | SSE | WebSocket |
|---|---|---|---|
| Protocol | HTTP | HTTP | WS (upgraded from HTTP) |
| Direction | Half-duplex (simulated push) | One-way (Server → Client) | Full-duplex |
| Connection | Re-established after each response | Persistent | Persistent |
| Browser support | Universal | Universal (except IE) | Universal |
| Complexity | Low | Low | Medium |
| Use cases | Legacy compatibility | Notifications, feeds, stock tickers | Chat, collaboration, gaming |

**Long Polling**: Client sends a request → server holds it until data is available → client immediately sends another request after receiving the response.

**SSE**: Server pushes text events over a single persistent HTTP connection. Client can only receive (one-way).

**WebSocket**: One HTTP upgrade handshake, then switches to the WS protocol for full-duplex real-time communication.
