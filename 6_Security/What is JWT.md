# JWT (JSON Web Token)

## 是什麼

- JWT（JSON Web Token）是一種「可攜帶 claims 的 token 格式」。
- 常用於登入後的身份驗證與授權傳遞（stateless auth）。
- 它是「簽章保完整性」，不是預設加密。

## 結構（3 段）

- `Header`：token 類型、簽章演算法（例如 HS256 / RS256）
- `Payload`：claims（例如 `sub`、`exp`、`iat`、`role`）
- `Signature`：用密鑰對前兩段簽章，防止被竄改

格式長這樣：`header.payload.signature`

## 你的範例 JWT 拆解

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0
.
KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30
```

- Header（Base64URL 解碼後）：

```json
{"alg":"HS256","typ":"JWT"}
```

- Payload（Base64URL 解碼後）：

```json
{"sub":"1234567890","name":"John Doe","admin":true,"iat":1516239022}
```

- Signature：
  - 這段不能「直接反解」成原文資料。
  - 伺服器會用同一套演算法與密鑰重新計算，比對是否一致。
  - 這顆 token 的 `alg=HS256`，代表驗簽會用 HMAC-SHA256。

## 編碼 vs 雜湊/簽章（你要記這段）

- `Header`、`Payload`：**Base64URL 編碼**（可被解碼閱讀，不是加密）。
- `Signature`：**簽章結果**，用來驗證內容是否被改。
  - `HS256`：HMAC（含雜湊）做訊息驗證。
  - `RS256/ES256`：非對稱數位簽章（不是單純「加密」或「只做雜湊」）。
- 結論：JWT 預設是「可讀 + 可驗完整性」，不是「預設保密」。

## 怎麼用（高階流程）

1. 使用者登入成功後，伺服器簽發 JWT。
2. Client 之後帶著 JWT 發請求（Web 常見放在 HttpOnly cookie）。
3. 伺服器驗簽 + 檢查 `exp` 等欄位，通過才放行。

## 簽發流程（Issuer 端）

1. 使用者用帳密/OAuth 登入，伺服器先完成身份驗證。
2. 伺服器建立 payload（例如 `role`、`exp`）。
3. 伺服器組出 `base64url(header) + "." + base64url(payload)`。
4. 用演算法與密鑰計算簽章（HS256 用同一把祕鑰；RS256 用私鑰簽）。
5. 回傳完整 token：`header.payload.signature`。

## 驗證流程（Verifier/Resource Server 端）

1. 從 `HttpOnly` cookie 取出 JWT（Web 常見做法；由瀏覽器自動夾帶）。
2. 解析 header，確認允許的演算法（避免接受錯誤/降級演算法）。
3. 用對應密鑰驗簽（HS256 用 shared secret；RS256 用公鑰驗）。
4. 檢查 claims：
   - `exp` 是否過期
   - `nbf` 是否已生效（若有）
   - `iss` 是否為信任簽發者（若有）
   - `aud` 是否是本服務（若有）
5. 全部通過才建立使用者身份（principal）並授權；失敗回 `401/403`。

## 優點 / 限制

- 優點：
  - 無狀態，易於橫向擴展
  - 跨服務傳遞身份資訊方便
- 限制：
  - token 一旦外洩，過期前都可能被濫用
  - 提前撤銷（logout all devices）比 session 複雜
  - payload 可被解碼，不要放敏感資料

## 最佳實務（面試常講）

- 用短效 access token + refresh token。
- 優先放在 HttpOnly + Secure + SameSite cookie（Web 場景）。
- 使用 HTTPS；妥善保管簽章密鑰並定期輪替。

## 一句話

JWT 是「可驗簽的身份聲明容器」：方便分散式驗證，但安全重點在金鑰管理、過期策略與儲存方式。
