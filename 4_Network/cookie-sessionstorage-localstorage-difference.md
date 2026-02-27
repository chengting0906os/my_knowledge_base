# Cookie vs sessionStorage vs localStorage

## English Version

### 1. How They Work

- `cookie`: server can set it via `Set-Cookie` response header; browser sends it automatically in matching HTTP requests.
- `localStorage` / `sessionStorage`: client-side key-value storage via Web Storage API.

```js
localStorage.setItem("memberName", "John");
localStorage.getItem("memberName");

sessionStorage.setItem("memberName", "John");
sessionStorage.getItem("memberName");
```

### 2. Common Use Cases

- `cookie`: user identity/session-related info that server needs on requests.
- `localStorage`: data that should persist across tabs/pages and browser restarts.
- `sessionStorage`: short-lived data for one tab/session, such as temporary form state.

### 3. Lifetime

- `cookie`: controlled by `Expires` / `Max-Age`; without explicit expiry, usually ends with browser session.
- `localStorage`: persists until manually or programmatically cleared.
- `sessionStorage`: cleared when the page/tab session ends.

### 4. Storage Size

- `cookie`: about 4KB.
- `localStorage` / `sessionStorage`: roughly 5MB to 10MB (browser-dependent).

### 5. HTTP Request Behavior

- `cookie`: included in request headers automatically; too many/large cookies can hurt performance.
- `localStorage` / `sessionStorage`: stay in browser only and are not automatically sent with HTTP requests.

### 6. Cookie Security Basics

- `Secure`: cookie is sent only over HTTPS.
- `HttpOnly`: JavaScript cannot read it via `document.cookie`, helping reduce XSS exposure.

---

## 中文版本

### 1. 使用方式

- `cookie`：伺服器可透過回應標頭 `Set-Cookie` 設定；之後瀏覽器會在符合條件的請求中自動帶上。
- `localStorage` / `sessionStorage`：使用 Web Storage API 在前端以 key-value 形式儲存。

```js
localStorage.setItem("memberName", "John");
localStorage.getItem("memberName");

sessionStorage.setItem("memberName", "John");
sessionStorage.getItem("memberName");
```

### 2. 常見使用場景

- `cookie`：伺服器需要辨識使用者時（例如登入狀態相關）。
- `localStorage`：跨頁面、較長期保存的資料。
- `sessionStorage`：單次頁面工作流程中的暫存資料（例如表單暫存）。

### 3. 生命週期

- `cookie`：可透過 `Expires` / `Max-Age` 設定；若未設定，通常在瀏覽器 session 結束後失效。
- `localStorage`：除非手動或程式清除，否則會長期存在。
- `sessionStorage`：頁籤或該次瀏覽 session 結束後清除。

### 4. 容量

- `cookie`：大約 4KB。
- `localStorage` / `sessionStorage`：約 5MB 到 10MB（依瀏覽器而異）。

### 5. 是否參與 HTTP 請求

- `cookie`：會自動夾帶在請求 header；過多或過大可能影響效能。
- `localStorage` / `sessionStorage`：只存在瀏覽器端，不會自動隨請求送出。

### 6. Cookie 安全設定重點

- `Secure`：僅在 HTTPS 傳送。
- `HttpOnly`：前端 JavaScript 無法透過 `document.cookie` 讀取，可降低 XSS 風險面。

## Ref

- https://www.explainthis.io/zh-hant/swe/cookie-sessionstorage-localstorage-difference
