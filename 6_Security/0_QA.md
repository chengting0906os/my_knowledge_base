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
    <details>
    <summary>Answer</summary>

   **JWT（JSON Web Token）** 是一種用於在雙方之間安全傳遞資訊的 token 格式，常用於身份驗證。

   格式：`xxxxx.yyyyy.zzzzz`（三段用 `.` 分隔，皆為 Base64URL 編碼）

   | 段     | 名稱          | 內容                                             |
   | ------ | ------------- | ------------------------------------------------ |
   | 第一段 | **Header**    | token 類型（JWT）+ 簽章演算法（如 HS256）        |
   | 第二段 | **Payload**   | Claims，即實際資料（如 user_id、role、過期時間） |
   | 第三段 | **Signature** | 用 secret 對前兩段簽章，確保資料未被竄改         |

   ```
   Header:    { "alg": "HS256", "typ": "JWT" }
   Payload:   { "sub": "user123", "exp": 1700000000 }
   Signature: HMAC-SHA256(base64(header) + "." + base64(payload), secret)
   ```

   - Header 和 Payload 只是 Base64URL 編碼，**任何人都能解碼讀取**，不要放敏感資料
   - Signature 才是安全性的關鍵，沒有 secret 就無法偽造
   </details>

10. In JWT, what is encoding vs signature?  
    JWT 裡哪些部分是編碼，哪些是簽章？

11. How is a JWT signed (HS256 vs RS256)?  
    JWT 在 HS256 和 RS256 下是怎麼簽發的？

12. How is JWT verified on server side?
    後端驗 JWT 的正確流程是什麼？
    <details>
    <summary>Answer</summary>
    1. **取出 token**：從 `Authorization: Bearer <token>` header 或 Cookie 取得 JWT
    2. **拆分三段**：split by `.` 得到 header、payload、signature
    3. **驗證 signature**：
       - 用相同的 secret（HS256）或公鑰（RS256）重新計算 `HMAC(header + "." + payload)`
       - 比對與 token 裡的 signature 是否一致，不一致代表被竄改，拒絕
    4. **驗證 claims**：
       - `exp`（過期時間）：是否已過期
       - `iss`（issuer）：是否為可信的發行者
       - `aud`（audience）：是否為正確的接收對象
    5. **取出 payload 使用**：驗證通過後取出 user_id、role 等資料

    **重點：** signature 驗證確保資料未被竄改，claims 驗證確保 token 仍然有效。
    </details>

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
    <details>
    <summary>Answer</summary>

    **非對稱加密（Asymmetric）**：速度慢，但能安全交換金鑰
    **對稱加密（Symmetric）**：速度快，適合大量資料加密

    TLS 結合兩者：用非對稱加密安全地交換一把對稱金鑰，再用對稱金鑰加密實際資料。

    **TLS 握手流程（簡化）：**

    ```
    1. Client Hello  →  告知支援的加密演算法
    2. Server Hello  ←  選定演算法，回傳憑證（含公鑰）
    3. 金鑰交換（非對稱）：
       - RSA：Client 用 server 公鑰加密 pre-master secret 送出
       - ECDHE：雙方各產生臨時金鑰對，交換公鑰，計算出相同的 shared secret
    4. 雙方用 shared secret 推導出 Session Key（對稱金鑰）
    5. 之後所有資料用 Session Key（AES 等）對稱加密傳輸
    ```

    **為什麼不全程用非對稱？**
    非對稱加密計算量大，加密大量資料會很慢。所以只用它在握手階段安全地協商出對稱金鑰，後續改用快速的對稱加密。
    </details>

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
    <details>
    <summary>Answer</summary>

    **不是**，CA 只負責「驗證身份」，不負責產生金鑰交換用的公私鑰。

    兩件事要分清楚：

    |           | 憑證公私鑰（Certificate Key）                                 | 金鑰交換公私鑰（ECDHE Ephemeral Key） |
    | --------- | ------------------------------------------------------------- | ------------------------------------- |
    | 由誰產生  | Server 自己產生                                               | 每次握手臨時產生                      |
    | CA 的角色 | CA 對 server 的公鑰**簽章**，證明「這把公鑰確實屬於這個域名」 | CA 完全不介入                         |
    | 用途      | 身份驗證                                                      | 協商 Session Key                      |
    | 生命週期  | 憑證有效期（1~2 年）                                          | 只用一次（Forward Secrecy）           |

    **CA 做的事：**
    - Server 把自己的公鑰和域名資訊送給 CA
    - CA 驗證你確實擁有這個域名
    - CA 用自己的私鑰簽章，產生憑證（Certificate）
    - Client 收到憑證後，用內建的 CA 公鑰驗證簽章，確認這個 server 是真的

    CA 簽的是「身份」，金鑰交換是雙方自己談的。
    </details>

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
    - 同源政策是瀏覽器的安全機制，禁止 A 網站的 JS 讀取 B 網站的回應內容。
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
    <details>
    <summary>Answer</summary>

    **CSP（Content Security Policy）** 是透過 HTTP header 告訴瀏覽器「哪些來源的資源可以執行」，不符合的一律阻擋。

    ```
    Content-Security-Policy: script-src 'self' https://trusted.com
    ```

    → 只有來自同源或 `trusted.com` 的 script 才能執行，其他全擋。

    **為什麼是第二層防線？**
    - 第一層：輸入驗證 + 輸出 escape（防止惡意 script 被注入 HTML）
    - 第二層（CSP）：就算攻擊者成功注入了 script，瀏覽器也會拒絕執行

    即使第一層有漏洞，CSP 可以阻止惡意 script 真正執行，降低攻擊成功率。這就是「縱深防禦（defense-in-depth）」的概念。
    </details>

37. How do you roll out CSP safely (Report-Only -> Enforce)?  
    CSP 實務上如何從 Report-Only 漸進上線到 Enforce？

38. What is clickjacking, and how do `frame-ancestors` / `X-Frame-Options` help?
    什麼是 clickjacking？`frame-ancestors` / `X-Frame-Options` 怎麼防？
    <details>
    <summary>Answer</summary>

    **Clickjacking（點擊劫持）：**
    攻擊者把目標網站嵌入透明的 `<iframe>`，疊在誘騙頁面上，讓使用者以為在點攻擊者的按鈕，實際上點到的是目標網站的操作（如轉帳、按讚、刪除帳號）。

    ```
    攻擊頁面：
    ┌────────────────────────┐
    │  "點我領獎"（誘餌按鈕） │
    │  ░░░░░░░░░░░░░░░░░░░  │  ← 透明 iframe 疊在上面
    │  ░  銀行轉帳按鈕  ░░  │
    └────────────────────────┘
    ```

    **防禦方式：**
    - **`X-Frame-Options`**（舊）：
      - `DENY` — 完全不允許被嵌入 iframe
      - `SAMEORIGIN` — 只允許同源嵌入

    - **`Content-Security-Policy: frame-ancestors`**（新，優先使用）：
      - `frame-ancestors 'none'` — 完全不允許
      - `frame-ancestors 'self'` — 只允許同源
      - `frame-ancestors https://trusted.com` — 允許特定來源

    兩者功能相近，`frame-ancestors` 更靈活且是現代標準，`X-Frame-Options` 是為了向下相容舊瀏覽器。
    </details>

39. What does `X-Content-Type-Options: nosniff` protect against?  
    `X-Content-Type-Options: nosniff` 主要在防什麼？

40. What is SQL Injection, and how is it caused?
    什麼是 SQL Injection？通常怎麼產生？
    <details>
    <summary>Answer</summary>

    **SQL Injection** 是攻擊者把惡意 SQL 語法注入輸入欄位，讓 server 執行非預期的資料庫指令。

    **產生原因：直接把使用者輸入拼接進 SQL 字串**

    ```js
    // 危險寫法
    const sql = `SELECT * FROM users WHERE name = '${userInput}'`;

    // 攻擊者輸入：' OR '1'='1
    // 實際執行：SELECT * FROM users WHERE name = '' OR '1'='1'
    // → 回傳所有使用者資料
    ```

    更嚴重的攻擊可以：刪除資料表、繞過登入驗證、取得所有帳密。
    </details>

41. What are the most important SQL Injection mitigations?
    防 SQL Injection 最重要的做法有哪些？
    <details>
    <summary>Answer</summary>
    1. **Prepared Statement（參數化查詢）**：最重要的防禦，把 SQL 結構與資料分開

    ```js
    db.query("SELECT * FROM users WHERE name = ?", [userInput]);
    // 輸入永遠被當作資料，不會被解析為 SQL 語法
    ```

    **為什麼有效？** 參數化查詢分兩階段送給 DB：先送 SQL 模板（DB 完成語法解析），再送資料（DB 只把它當純值填入，不再重新解析語法）。攻擊者輸入的 `'`、`--`、`;` 都只是資料的一部分，無法改變 SQL 結構。

    2. **ORM**：使用 Sequelize、Prisma 等 ORM，預設就用參數化查詢

    3. **輸入驗證**：限制輸入格式（如只允許數字、英文），減少攻擊面

    4. **最小權限原則**：資料庫帳號只給必要的權限，不用 root 連線

    5. **不要顯示詳細錯誤訊息**：避免洩漏資料庫結構給攻擊者
    </details>

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

48. What are common symmetric and asymmetric encryption algorithms?
    對稱加密與非對稱加密各有哪些常見演算法？
    <details>
    <summary>Answer</summary>

    **對稱加密（Symmetric）**：加解密用同一把金鑰

    | 演算法 | 說明 |
    | ------ | ---- |
    | AES    | 目前最主流，128/192/256-bit key，安全且快速 |
    | DES    | 已淘汰，key 太短（56-bit）不安全 |
    | 3DES   | DES 的改良版，效能差，逐漸淘汰 |
    | ChaCha20 | Google 推廣，適合行動裝置，TLS 1.3 支援 |

    **非對稱加密（Asymmetric）**：公鑰加密、私鑰解密（或私鑰簽章、公鑰驗章）

    | 演算法  | 說明 |
    | ------- | ---- |
    | RSA     | 最廣泛使用，常見 2048/4096-bit |
    | ECC     | 橢圓曲線，同等安全性 key 更短、效能更好 |
    | ECDSA   | ECC-based 數位簽章，JWT RS256 的替代方案 |
    | DSA     | 早期數位簽章標準，已被 ECDSA 取代 |
    | Diffie-Hellman (DH/ECDHE) | 金鑰交換用（不用於加密/簽章），TLS 握手常見 |

    </details>

49. What encryption algorithms does JWT use?
    JWT 使用哪種加密演算法？
    <details>
    <summary>Answer</summary>

    JWT 本身不加密內容，而是做**簽章（Signature）**，確保 token 未被竄改。常見演算法：

    | 演算法 | 類型 | 說明 |
    | ------ | ---- | ---- |
    | HS256  | 對稱（HMAC） | 用同一個 secret 簽章與驗章；簡單但 server 間需共享 secret |
    | RS256  | 非對稱（RSA） | 私鑰簽章、公鑰驗章；適合多服務場景，公鑰可公開發布 |
    | ES256  | 非對稱（ECDSA） | 同 RS256 概念但用 ECC，key 更短、效能更好 |

    **HS256 vs RS256 選哪個？**
    - 單一服務：HS256 夠用，簡單
    - 多個服務需驗證同一個 token（如 microservices）：RS256，不需要每個服務都持有 secret，只需要公鑰

    **誰用非對稱（RS256/ES256）簽章？**
    主要是 **Identity Provider（IdP）**，例如 Google、Apple、Okta、Auth0，或自建的 Auth Server。
    Auth Server 用私鑰簽章發出 JWT，其他服務（resource servers）透過公開的 JWKS endpoint 取得公鑰驗章，不需要持有 secret，私鑰只有 Auth Server 知道，洩漏面最小。

    補充：若需要真正加密 JWT 內容（payload 不可讀），要用 **JWE（JSON Web Encryption）**，這與 JWS（簽章）是不同規格。

    </details>
