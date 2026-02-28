# Security Interview Q&A List

1. What is the difference between authentication and authorization?  
   Authentication（驗證身份）和 Authorization（授權）差異是什麼？

2. Why do we say authentication comes before authorization?  
   為什麼說要先驗證身份，再做授權判斷？

3. What problem does SSO (Single Sign-On) solve?  
   SSO（單一登入）主要解決什麼問題？

4. What is OAuth, and what is it used for?  
   OAuth 是什麼？主要用在哪裡？

5. Walk through OAuth Authorization Code Flow at a high level.  
   請高層描述 OAuth 的 Authorization Code Flow。

6. Why do we exchange authorization code for access token on backend?  
   為什麼要在後端用 authorization code 換 access token？

7. What are the core differences between Session and JWT?  
   Session 和 JWT 的核心差異是什麼？

8. When would you choose Session over JWT, and vice versa?  
   實務上什麼情況選 Session？什麼情況選 JWT？

9. What is JWT, and what are its three parts?  
   JWT 是什麼？三段結構是什麼？

10. In JWT, what is encoding vs signature?  
    JWT 裡哪些部分是編碼，哪些是簽章？

11. How is a JWT signed (HS256 vs RS256)?  
    JWT 在 HS256 和 RS256 下是怎麼簽發的？

12. How is JWT verified on server side?  
    後端驗 JWT 的正確流程是什麼？

13. What is a cookie, and how does `Set-Cookie` work?  
    Cookie 是什麼？`Set-Cookie` 是怎麼運作的？

14. What do `HttpOnly`, `Secure`, and `SameSite` mean for cookies?  
    Cookie 的 `HttpOnly`、`Secure`、`SameSite` 各代表什麼？

15. How does `SameSite` help mitigate CSRF?  
    `SameSite` 怎麼幫助降低 CSRF 風險？

16. What is the difference between encoding, hashing, and encryption?  
    Encoding、Hashing、Encryption 差異是什麼？

17. Symmetric vs asymmetric encryption: key differences and use cases?  
    對稱與非對稱加密的差異與常見用途是什麼？

18. How do symmetric and asymmetric cryptography work together in TLS?  
    在 TLS 裡，對稱與非對稱密碼學如何搭配？

19. What is the difference between SSL and TLS?  
    SSL 和 TLS 差異是什麼？

    <details>
    <summary>Answer</summary>

    TLS 使用更安全、更新的密碼套件；另外 TLS 也是 SSL 的後繼協定，握手與安全機制更完整。實務上 SSL 已淘汰，現代應使用 TLS 1.2/1.3。

    </details>

20. What security properties does HTTPS provide?  
    HTTPS 提供哪些安全性保證？

    <details>
    <summary>Answer</summary>
    - 機密性（Confidentiality）：傳輸內容被加密，旁路無法直接讀到明文。
    - 完整性（Integrity）：若中途有人改封包內容（例如把匯款帳號改掉），接收端會因驗證失敗而丟棄連線/資料。
    - 身份驗證（Authentication）：瀏覽器會驗證憑證鏈與網域。  
      例：你連 `bank.com`，若中間人給的是假憑證或網域不匹配，瀏覽器會顯示憑證警告並阻擋連線。

    </details>

21. Walk through TLS 1.3 handshake steps.  
    請描述 TLS 1.3 的握手流程。

22. Are TLS key-exchange public/private keys issued by a CA?  
    TLS 交換用的公私鑰是由 CA 簽發的嗎？

23. What is MITM attack, and how does HTTPS reduce its risk?  
    什麼是 MITM（中間人攻擊）？HTTPS 怎麼降低風險？
    <details>
    <summary>Answer</summary>
    - 攻擊者攔截傳輸的資料，偷看或改封包
    - 可設定 HSTS（Strict-Transport-Security）標頭，強制只用 HTTPS>

    </details>

24. What is Same-Origin Policy (SOP), and what does it restrict?  
    Same-Origin Policy（同源政策）是什麼？限制了哪些行為？
	<details>
	<summary>Answer</summary>

	- 同源政策是瀏覽器的安全機制。
	- 前端 JS 只能讀取同 `protocol + host(domain) + port` 的資源。
	- 若是跨源，要由 server 明確開放 CORS，瀏覽器才會讓 JS 讀回應。
	- SOP 主要限制「讀取」，不是完全禁止「送出跨站請求」。

	</details>

25. Why does Same-Origin Policy (SOP) exist?  
    為什麼需要同源政策（SOP）？
	<details>
	<summary>Answer</summary>

	- SOP 先把跨源讀取預設關閉，避免惡意網站直接讀取你在其他網站的敏感回應。
	- 例如你已登入 `bank.com`，若沒有 SOP，`evil.com` 可能用前端 JS 直接讀到銀行 API 回應。
	- 在此基礎上，再由 CORS 做「可控放行」。

	</details>



26. What is an origin in the browser security model?  
    瀏覽器安全模型中的 origin（同源）是怎麼定義的？

27. Why does CORS exist?  
    為什麼會有 CORS？

	<details>
	<summary>Answer</summary>

	CORS 的存在是為了在安全性與方便性之間取得平衡：保留 SOP 預設防護，同時允許受控的跨源存取。

	</details>

28. What is a CORS preflight request, and when is it triggered?  
    什麼是 CORS 預檢請求（preflight）？什麼情況會觸發？

	<details>
	<summary>Answer</summary>

	CORS preflight 是瀏覽器先送的 `OPTIONS` 探測請求，用來確認 server 是否允許真正跨源請求。  
	通常在「非 simple request」時觸發，例如：
	- method 不是 `GET/HEAD/POST`（如 `PUT/DELETE/PATCH`）
	- `POST` 但 `Content-Type` 非 simple 類型
	- 帶自訂 headers（如 `Authorization`）

	補充：CORS 是瀏覽器端限制。若 server 未正確限制，請求可能到達 server，但瀏覽器會阻擋前端 JS 讀回應。

	</details>

29. What are key CORS headers and common misconfigurations?  
    CORS 常見 headers 有哪些？常見錯誤設定是什麼？

	<details>
	<summary>Answer</summary>

	常見 CORS headers：
	- `Access-Control-Allow-Origin`：允許哪些 origin
	- `Access-Control-Allow-Methods`：允許哪些 HTTP 方法
	- `Access-Control-Allow-Headers`：允許哪些 request headers
	- `Access-Control-Allow-Credentials`：是否允許帶 cookie/credentials
	- `Access-Control-Max-Age`：preflight 快取秒數
	- `Access-Control-Expose-Headers`：允許前端 JS 讀哪些 response headers

	常見錯誤設定：
	- `Allow-Origin: *` 同時 `Allow-Credentials: true`（瀏覽器規範不允許）
	- 把不該開放的 origin 全開（過度寬鬆）
	- 忘記處理 `OPTIONS`，導致 preflight 失敗
	- 沒有 `Vary: Origin`，造成快取污染/錯誤回應
	- 以為 CORS 是 server 安全邊界（其實主要是瀏覽器讀取限制）

	</details>

30. What is CSRF, and when is an application vulnerable to it?  
    什麼是 CSRF？什麼情況容易被 CSRF 攻擊？

31. What are practical CSRF defenses?  
    CSRF 在實務上的防禦手段有哪些？

	<details>
	<summary>Answer</summary>

	- CSRF Token（主防線，最重要）
	- 檢查 `Origin` / `Referer`
	- 檢查 Fetch Metadata（如 `Sec-Fetch-Site`）
	- Cookie 設 `SameSite`（Lax/Strict，視業務需求）
	- 敏感操作加二次驗證（re-auth / OTP）
	- 補充：CSP 主要防 XSS，不是 CSRF 主防線

	</details>

32. What is XSS, and what are Stored / Reflected / DOM-based XSS?  
    什麼是 XSS？Stored / Reflected / DOM-based 差在哪？

	<details>
	<summary>Answer</summary>

	- XSS：把惡意腳本注入網頁，讓受害者瀏覽器執行。
	- Stored XSS：惡意內容先被存到資料庫（如留言），之後回給其他使用者時執行。
	- Reflected XSS：惡意內容常放在 URL 參數，後端在 response 時反射到頁面後執行。
	- DOM-based XSS：漏洞在前端 JS，直接把不可信資料寫進危險 DOM API（如 `innerHTML`）而執行。
	- 一句話：Stored/Reflected 多與後端回應有關，DOM-based 重點在前端程式。

	</details>

33. What is the difference between Reflected XSS and DOM-based XSS?  
    Reflected XSS 和 DOM-based XSS 的關鍵差異是什麼？

34. How do you prevent XSS in practice?  
    實務上如何防止 XSS？
	<details>
	<summary>Answer</summary>

	- Output encoding（依 context 正確 escape）
	- 避免把不可信資料直接放進 `innerHTML`，優先 `textContent`
	- 需要富文字時用 allowlist sanitization
	- 啟用 CSP（建議先 Report-Only 再 Enforce）
	- 重要 cookie 設 `HttpOnly` + `Secure`，降低被竊後影響

	</details>

35. Output encoding vs sanitization: when do you use each?  
    Output encoding 和 sanitization 差在哪？各自何時用？

	<details>
	<summary>Answer</summary>

	- Output encoding（escaping）：
	- 把內容當純文字輸出，避免被當成 HTML/JS 執行。
	- 用在「不需要保留 HTML」的一般文字欄位（暱稱、留言純文字）。

	- Sanitization（清洗）：
	- 允許部分 HTML，但移除危險標籤/屬性（如 `<script>`、`onerror`、`javascript:`）。
	- 用在「需要保留有限格式」的內容（富文字編輯器、文章內容）。

	- 一句話：不需要 HTML 就 encode；需要部分 HTML 就 sanitize（allowlist）。

	</details>

36. What is CSP, and why is it defense-in-depth for XSS?  
    CSP 是什麼？為什麼說它是 XSS 的第二層防線？

37. How do you roll out CSP safely (Report-Only -> Enforce)?  
    CSP 實務上如何從 Report-Only 漸進上線到 Enforce？

38. What is clickjacking, and how do `frame-ancestors` / `X-Frame-Options` help?  
    什麼是 clickjacking？`frame-ancestors` / `X-Frame-Options` 怎麼防？

39. What does `X-Content-Type-Options: nosniff` protect against?  
    `X-Content-Type-Options: nosniff` 主要在防什麼？

40. What is SQL Injection, and how is it caused?  
    什麼是 SQL Injection？通常怎麼產生？

41. What are the most important SQL Injection mitigations?  
    防 SQL Injection 最重要的做法有哪些？

42. Why do systems need rate limiting?  
    為什麼系統需要 Rate Limiter？

43. Compare Fixed Window, Sliding Window, and Token Bucket.  
    固定窗口、滑動窗口、令牌桶三種限流演算法怎麼比較？

44. Why is rate limiting by IP alone risky (e.g., NAT)?  
    為什麼只用 IP 做限流有風險（例如 NAT 誤傷）？

45. What should an API return when throttled (`429`, `Retry-After`)?  
    API 被限流時應該回什麼（`429`、`Retry-After`）？

46. In distributed systems, why is Redis commonly used for rate limiting?  
    在分散式系統中，為什麼限流常用 Redis？

47. What is fail-open vs fail-close in rate limiter design?  
    限流設計裡的 fail-open 和 fail-close 差異是什麼？
