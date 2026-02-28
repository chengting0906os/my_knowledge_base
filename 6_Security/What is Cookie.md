# What is Cookie

## Overview

Cookie 是瀏覽器儲存在本機的一小段資料，由伺服器透過 `Set-Cookie` 回應標頭設定。  
之後瀏覽器在符合條件的請求中，會自動用 `Cookie` 請求標頭帶回。

白話：Cookie 是網站讓瀏覽器「記住狀態」的方式（例如登入狀態、偏好設定）。

## Basic Flow

1. Server 回應：`Set-Cookie: session_id=abc123; HttpOnly; Secure; SameSite=Lax`
2. Browser 儲存這個 cookie
3. 下次請求同站資源時，自動夾帶：`Cookie: session_id=abc123`
4. 同一個 response 可帶多個 `Set-Cookie`，一次設定多顆 cookie

## Creation / Removal / Update（MDN 重點）

- 建立：Server 用 `Set-Cookie: name=value` 設定 cookie。
- 更新：用相同 cookie 名稱重新 `Set-Cookie` 即可覆蓋值。
- 刪除：用相同 `name + path + domain` 重設，並設 `Max-Age=0`（或 `Expires` 設過去時間）。

## Common Use Cases

- Session 管理（登入狀態）
- 使用者偏好（語系、佈景）
- 購物車暫存
- 追蹤與分析（廣告/分析 cookie）

## Important Cookie Attributes

- `Expires` / `Max-Age`: 設定有效時間
  - 沒設 `Expires/Max-Age` -> session cookie
  - 同時設兩者時，`Max-Age` 優先
- `Domain`: 哪些網域可帶上 cookie
- `Path`: 哪些路徑可帶上 cookie
- `HttpOnly`: 禁止 JavaScript 讀取（降低 XSS 竊取風險）
- `Secure`: 只在 HTTPS 傳送
- `SameSite`: 限制跨站請求攜帶 cookie（`Strict` / `Lax` / `None`）
  - 先記：`cross-site` = 請求來源網站和目標網站不同（例如 `a.com` 發請求到 `b.com`）。
  - `Strict`: 只要是 cross-site 就不帶 cookie。安全最高，但使用者從外站點連進來時可能看起來像未登入。
  - `Lax`: 預設常用。大多數 cross-site 請求不帶 cookie，但「使用者點連結造成的頂層 GET 導頁」通常會帶 cookie。
  - `None`: 允許 cross-site 請求帶 cookie（例如第三方登入/嵌入情境需要）。
  - `SameSite=None` 必須搭配 `Secure`，否則現代瀏覽器通常會拒收該 cookie。

## Cookie Types (Practical)

- Session Cookie：未設 `Expires/Max-Age`，理論上在 client shutdown 後移除。
  - 「session 何時結束」由瀏覽器定義。
  - 但多數瀏覽器有 session restore，重開瀏覽器時可能把 session cookie 一起恢復。
- Persistent Cookie：有明確過期時間
- First-party Cookie：由當前網站設定
- Third-party Cookie：由第三方網域設定（現代瀏覽器限制越來越多）
  - 常見於第三方廣告、追蹤與嵌入元件，主流瀏覽器正逐步收緊或預設封鎖。
  - 理解重點：你開一個頁面時，瀏覽器通常不只連主站，還會同時請求 CDN、分析、廣告、影片等不同網域資源；這些第三方網域若在回應中 `Set-Cookie`，就形成 third-party cookie。

## Security Risks

- XSS 可能偷 cookie（若未設 `HttpOnly`）
- CSRF 利用瀏覽器自動帶 cookie 偽造請求
- 傳輸未加密時，cookie 可能被攔截（應搭配 HTTPS + `Secure`）

## Best Practices

- Session cookie 一律設 `HttpOnly` + `Secure`
- 依需求設定 `SameSite`（預設建議 `Lax`，高敏感可考慮 `Strict`）
- 不在 cookie 放敏感明文資料（如密碼、完整個資）
- 設定合理過期時間，並在登出時主動失效 session

## Interview Version (30s)

Cookie 是伺服器存到瀏覽器的小型狀態資料，透過 `Set-Cookie` 設定，之後瀏覽器會在符合條件的請求自動帶回。最常見用途是登入 session。安全上要重點設定 `HttpOnly`、`Secure`、`SameSite`，分別對應降低 XSS 竊取、避免明文傳輸、減少 CSRF 風險。

## Ref

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie
