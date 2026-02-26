# CORS (Cross-Origin Resource Sharing)

### What is CORS

CORS (Cross-Origin Resource Sharing) is an HTTP-header-based mechanism that allows a server to specify which cross-origin clients can read its resources in a browser.

### Same-Origin Policy First

Same-Origin Policy is a core browser security rule. A page can read another resource only when protocol, domain, and port are all the same.

If any of these differ, the request is cross-origin.

### Why CORS Exists

- It prevents arbitrary cross-site data access by default.
- It gives servers controlled, explicit cross-origin access.
- It governs browser-side JavaScript access to response data.

### CORS Flow

1. A browser sends a cross-origin request.
2. Browser checks whether it is a simple request.
3. For simple requests, browser sends it directly and validates CORS headers in the response.
4. For non-simple requests (e.g., `PUT`, `DELETE`, custom headers), browser sends a preflight `OPTIONS` request first.
5. Only when preflight is allowed does the browser send the actual request.

### Why Preflight Is Needed (Interview Question)

Interviewers often ask: "Why add an extra request before the real one? Isn't it wasteful?"

Security-first answer:

- Same-Origin Policy mainly prevents JavaScript from reading cross-origin responses; it does not reliably stop every cross-origin request from reaching the server.
- A malicious site may still trigger state-changing requests (for example, `DELETE`) to a target server.
- If the server has no extra CORS gate, dangerous actions could be executed even though the attacker cannot read the response.
- Preflight adds a permission check before non-simple, higher-risk requests. If preflight fails, the browser does not send the actual request.

Performance answer:

- Preflight is not for every request; it is mainly for non-simple requests.
- Browsers can cache preflight results via `Access-Control-Max-Age`, reducing repeated preflight overhead.
- This is a deliberate security/performance tradeoff: one lightweight check helps reduce high-impact cross-origin abuse.

### Common CORS Headers

- `Access-Control-Allow-Origin`
- `Access-Control-Allow-Methods`
- `Access-Control-Allow-Headers`
- `Access-Control-Allow-Credentials`
- `Access-Control-Max-Age`

### Interview Key Points

- CORS is not authentication/authorization.
- CORS may not block the network request itself, but it can block browser access to the response.
- If credentials are allowed, `Access-Control-Allow-Origin` must be a specific origin, not `*`.

### 30-Second Interview Version (English)

CORS is a browser security mechanism for controlled cross-origin resource access. Because of Same-Origin Policy, frontend code cannot read resources from different protocol/domain/port by default. For non-simple requests, browsers send a preflight `OPTIONS` request first, then proceed only if the server returns proper `Access-Control-Allow-*` headers. CORS controls browser access to responses; it is not a backend authorization mechanism.

### CORS 是什麼

CORS（Cross-Origin Resource Sharing，跨來源資源共享）是一種基於 HTTP Header 的機制，讓伺服器可以明確告訴瀏覽器：哪些不同來源（origin）的前端可以讀取這個回應。

### 先理解同源政策（Same-Origin Policy）

同源政策是瀏覽器的核心安全機制，限制網頁只能讀取同源資源。

同源必須同時滿足以下三者：

- 同通訊協定（Protocol）
- 同網域（Domain）
- 同通訊埠（Port）

只要有任一項不同，就屬於跨來源（Cross-Origin）。

### 為什麼需要 CORS

- 同源政策是預設保護層，避免惡意網站任意讀取其他網站資料。
- CORS 讓伺服器可以「有條件」開放跨來源存取，而不是全部封鎖或全部放行。
- 重點是：CORS 控制的是瀏覽器是否允許前端 JavaScript 讀取回應內容。

### CORS 的運作流程

1. 前端發出跨來源請求。
2. 瀏覽器判斷是否為簡單請求（simple request）。
3. 若是簡單請求：直接送出請求，收到回應後檢查 CORS header。
4. 若非簡單請求（例如 `PUT`、`DELETE`、自訂 header）：先送預檢請求（preflight, `OPTIONS`）。
5. 伺服器回覆允許後，瀏覽器才送真正請求。

### 為什麼需要預檢請求（面試常見追問）

面試常見問題是：「正式請求前多一次 `OPTIONS`，不是浪費資源嗎？」

可以先從安全性回答：

- 同源政策主要是限制前端 JavaScript 讀取跨來源回應，不是完整阻止所有跨來源請求到達伺服器。
- 惡意網站仍可能嘗試觸發具副作用的請求（例如 `DELETE`）。
- 如果沒有額外檢查，伺服器可能在使用者不知情下執行刪除或修改等操作。
- 預檢請求就是在正式請求前先做一次「是否允許」的過濾；預檢不通過，瀏覽器就不會送出真正請求。

再補充效能面：

- 預檢不是每個請求都會發生，主要針對非簡單請求。
- 可透過 `Access-Control-Max-Age` 快取預檢結果，降低重複 `OPTIONS` 的成本。
- 這是安全與效能的權衡：多一次輕量檢查，換取對高風險跨來源操作的保護。

### 常見 CORS Response Headers

- `Access-Control-Allow-Origin`: 允許的來源（如 `https://app.example.com` 或 `*`）
- `Access-Control-Allow-Methods`: 允許的方法（GET/POST/PUT...）
- `Access-Control-Allow-Headers`: 允許的請求 headers
- `Access-Control-Allow-Credentials`: 是否允許攜帶 cookie/credential
- `Access-Control-Max-Age`: preflight 快取時間

### 面試常考重點

- CORS 不是用來做身分驗證或授權；後端仍需做 Authentication/Authorization。
- 即使請求已送到伺服器，若 CORS 不通過，瀏覽器仍會攔截回應給前端 JS。
- 若要允許 credentials，`Access-Control-Allow-Origin` 不能是 `*`，必須是明確 origin。

### 30 秒面試版（中文）

CORS 是瀏覽器的跨來源讀取控制機制。因為同源政策，前端預設不能讀取不同協定、網域或埠的資源。當請求是非簡單請求時，瀏覽器會先送 `OPTIONS` preflight，確認伺服器允許後才送正式請求，並依 `Access-Control-Allow-*` 標頭決定是否把回應交給前端程式使用。CORS 保護的是瀏覽器讀取行為，不等於後端授權機制。

## REF

- https://www.explainthis.io/zh-hant/swe/what-is-cors
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- https://realnewbie.com/posts/understanding-same-origin-policy-from-scratch-first-line-of-browser-security
