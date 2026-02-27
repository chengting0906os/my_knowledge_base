# OAuth

OAuth is a technical standard for authorizing users. It is a protocol for passing authorization from one service to another without sharing the actual user credentials, such as a username and password.

OAuth 是用於授權使用者的技術標準。此通訊協定用於將授權從一項服務傳遞給另一項服務，而無需共用實際的使用者驗證資訊，例如使用者名稱和密碼。使用 OAuth，使用者在一個平台上登入後，可被授權在另一個平台上執行動作和檢視資料。

## 簡答

OAuth 是一種授權的技術標準，常見用途是第三方登入。  
使用者在第三方（如 Google）完成登入與同意 scope 後，會被導回 `redirect_uri` 並帶回 `authorization code`（grant）。  
後端再用這個 code 向 Authorization Server 交換 `access token`，最後用 token 存取授權範圍內資料（如名稱、Email）。

OAuth is an authorization standard, and a common use case is third-party sign-in.  
After the user signs in and approves scope at a third-party provider (such as Google), the app is redirected to `redirect_uri` with an `authorization code` (grant).  
Your backend exchanges that code for an `access token`, then uses the token to access resources within the granted scope.

## Authorization Code Flow（以 Sign in with Google 為例）

同樣以使用者（Resource Owner）在應用程式中點擊「Sign in with Google」為例，並在瀏覽器中進行：

1. 瀏覽器將使用者導向 Authorization Server（以 Google 為例：`https://accounts.google.com/`），並帶上常見參數：
   - `client_id`：應用程式（Client）在 Authorization Server 的身份識別
   - `redirect_uri`：流程結束後要導回的位置
   - `response_type`：告知要取得哪一種 Authorization Grant
   - `scope`：定義應用程式可代使用者取得的資源範圍
2. Authorization Server 進行使用者身份驗證。
3. 驗證成功後，依據第 1 步設定的 `scope`，詢問使用者是否同意授權。
   - 例如只允許應用程式取得使用者在 Google 的名稱、Email 通訊錄，就會在這裡被明確詢問。
4. 使用者同意後，Authorization Server 依照 `redirect_uri` 導回應用程式，並依 `response_type` 回傳 Authorization Grant。
   - 若使用者不同意，則回傳對應錯誤。
5. 應用程式拿到 Authorization Grant 後，還不能直接向 Resource Server 拿資料；必須先向 Authorization Server 交換 Access Token。
   - Authorization Server 會驗證 Authorization Grant 與應用程式身分後，才核發 Access Token。
   - Access Token 權限只會落在第 1 步的 `scope` 範圍內。
   - 一般 Web App（Confidential Client）通常由後端做這一步；SPA/Mobile（Public Client）則常用 Authorization Code + PKCE 在前端完成 token 交換（不使用 `client_secret`）。
6. 應用程式在請求資源時夾帶 Access Token，向 Resource Server 取得資料。
   - 例如 scope 只允許名稱與 Email，就不能去拿使用者大頭貼。

### 為什麼要多一步「交換 Access Token」，而不是直接核發？

考量是安全性。

- 前段流程多發生在前端（瀏覽器）與頁面跳轉中，像 `callback/redirect_uri`、`scope`、Authorization Grant 等資料常會出現在 URL Query String，被看見的風險較高。
- 交換 Access Token 通常在後端進行（HTTP POST），會一併帶上應用程式身分資訊（如 `client_id`、`client_secret`）給 Authorization Server 驗證。
- `client_secret` 應只存放在後端，不暴露在前端程式碼，因此整體安全性更高。

## Ref

- https://medium.com/%E9%BA%A5%E5%85%8B%E7%9A%84%E5%8D%8A%E8%B7%AF%E5%87%BA%E5%AE%B6%E7%AD%86%E8%A8%98/%E7%AD%86%E8%A8%98-%E8%AA%8D%E8%AD%98-oauth-2-0-%E4%B8%80%E6%AC%A1%E4%BA%86%E8%A7%A3%E5%90%84%E8%A7%92%E8%89%B2-%E5%90%84%E9%A1%9E%E5%9E%8B%E6%B5%81%E7%A8%8B%E7%9A%84%E5%B7%AE%E7%95%B0-c42da83a6015
