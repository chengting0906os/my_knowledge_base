# 什麼是 HTTP vs HTTPS

## 先理解 HTTP 是什麼

### English Key Points

- HTTP (HyperText Transfer Protocol) is the foundation of data exchange on the Web.
- It is a client-server protocol: the client (usually a browser) initiates requests, and the server returns responses.
- A web page is often composed of many resources (HTML, CSS, JS, images, videos), sometimes from different servers.
- HTTP communication is message-based:
  - Client sends a request
  - Server sends a response
- HTTP is an application-layer protocol.
  - Commonly runs over TCP
  - HTTPS means HTTP over TLS-encrypted transport
- HTTP is extensible and evolved from the early 1990s to support more use cases (API calls, partial updates, media delivery).

### 中文重點版

- HTTP（HyperText Transfer Protocol）是 Web 資料交換的基礎協定。
- 它是 client-server 模型：
  - Client（通常是瀏覽器）主動發 request
  - Server 回 response
- 一個網頁通常由多種資源組成（HTML、CSS、JS、圖片、影片），也可能來自不同伺服器。
- HTTP 是「訊息交換」模型，不是長時間持續串流同一格式資料。
  - Client 發 request
  - Server 回 response
- HTTP 屬於應用層協定：
  - 常跑在 TCP 之上
  - HTTPS 是 HTTP 跑在 TLS 加密連線上
- HTTP 從 1990 年代發展至今，具有可擴充性，不只拿 HTML，也常用於 API、檔案與多媒體傳輸。

典型結構：
- Request：Method、URL、Headers、Body
- Response：Status Code、Headers、Body

## 一句話差異

- `HTTP`：明文傳輸，內容可能被竊聽或篡改。
- `HTTPS`：`HTTP + TLS`，提供加密、完整性、身分驗證。

## 快速比較

| 項目 | HTTP | HTTPS |
| --- | --- | --- |
| 預設埠號 | `80` | `443` |
| 傳輸內容 | 明文 | 加密後傳輸 |
| 是否能防竊聽 | 否 | 是（大幅降低風險） |
| 是否能防中間人竄改 | 否 | 可透過 TLS 完整性驗證降低 |
| 是否驗證伺服器身分 | 否 | 是（憑證 + CA 鏈） |
| SEO / 瀏覽器信任 | 較差 | 較好（現代網站標準） |

## HTTPS 到底多了什麼

HTTPS 不是新協定，而是 HTTP 跑在 TLS 之上。  
TLS 主要提供三件事：

- Confidentiality（機密性）：內容被加密，旁路不易讀懂。
- Integrity（完整性）：傳輸中被修改會被偵測。
- Authentication（身分驗證）：確認你連的是持有合法憑證的網站。

## TLS 握手在做什麼（簡化版）

1. Client Hello：客戶端送出支援的 TLS 版本與加密套件。
2. Server Hello：伺服器選定套件並回傳憑證。
3. 驗證憑證：客戶端驗證 CA 信任鏈與網域是否匹配。
4. 金鑰交換：雙方建立 session key。
5. 之後 HTTP 資料以對稱加密傳輸。

## 常見實務設定

- 全站強制 HTTPS（`http -> https` 301/308）。
- 開啟 HSTS（`Strict-Transport-Security`）避免降級攻擊。
- 憑證定期更新（Let's Encrypt / ACME 常見）。
- 避免 mixed content（HTTPS 頁面載入 HTTP 子資源）。

## 常見誤解

- 「用了 HTTPS 就 100% 安全」：錯。HTTPS 只保護傳輸層，不會自動修掉 XSS/SQLi。
- 「只有登入頁要 HTTPS」：錯。現代建議全站 HTTPS。
- 「HTTPS 很慢」：舊觀念。現在硬體與協定優化後，成本通常可接受，且 HTTP/2/3 常搭配 HTTPS。

## 30 秒面試版

HTTP 是明文傳輸；HTTPS 是 HTTP 加上 TLS。  
HTTPS 透過憑證與金鑰交換提供加密、完整性與伺服器身分驗證，能有效降低竊聽與中間人攻擊風險。  
實務上應全站 HTTPS、設定 HSTS、避免 mixed content，並定期更新憑證。

## Ref

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
- https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/TLS
