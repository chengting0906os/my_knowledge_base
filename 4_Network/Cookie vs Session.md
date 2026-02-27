# Cookie vs Session

## English Version

### Cookie

- A small key-value data stored in the browser.
- Automatically sent by the browser to the matching domain/path on each request.
- Used for session IDs, user preferences, and tracking.
- Security-related flags:
  - `HttpOnly`: JavaScript cannot read it.
  - `Secure`: sent only over HTTPS.
  - `SameSite`: helps reduce CSRF risk.

### Session

- Server-side state for a user.
- Browser usually stores only a session ID (often in a cookie).
- Pros:
  - Better server control and easier invalidation.
  - Sensitive data stays on server.
- Cons:
  - Requires server/session store (Redis/DB) and scaling strategy.

### Quick Comparison

| Item | Cookie | Session |
| --- | --- | --- |
| Where data lives | Browser | Server (state), browser stores session ID |
| Sent by browser automatically | Yes | Session ID cookie: Yes |
| Stateless-friendly | Limited | No |
| Revocation | Delete cookie only | Easy (kill session on server) |
| Typical use | State persistence | Traditional web login |

### One-line Interview Summary

- Cookie is a storage/transport mechanism.
- Session is server-side login state.

---

## 中文版本

### Cookie

- 儲存在瀏覽器的小型 key-value 資料。
- 只要網域與路徑符合，瀏覽器會在每次請求自動帶上。
- 常見用途：Session ID、使用者偏好、追蹤資訊。
- 安全旗標：
  - `HttpOnly`：前端 JavaScript 無法讀取。
  - `Secure`：只在 HTTPS 傳送。
  - `SameSite`：可降低 CSRF 風險。

### Session

- 使用者狀態儲存在伺服器端。
- 瀏覽器通常只保存 Session ID（通常放在 Cookie）。
- 優點：
  - 伺服器可控性高、失效管理容易。
  - 敏感資料不落在前端。
- 缺點：
  - 需要伺服器記憶體或集中式儲存（如 Redis）來擴展。

### 快速比較

| 項目 | Cookie | Session |
| --- | --- | --- |
| 資料主要存放位置 | 瀏覽器 | 伺服器（瀏覽器只存 Session ID） |
| 瀏覽器是否自動帶上 | 會 | Session ID Cookie 會 |
| 是否適合無狀態 | 普通 | 否 |
| 失效/撤銷難度 | 刪 Cookie 即可 | 容易（伺服器刪 Session） |
| 常見場景 | 狀態保存 | 傳統網站登入 |

### 面試一句話版本

- Cookie 是儲存/傳輸機制。
- Session 是伺服器端登入狀態。
