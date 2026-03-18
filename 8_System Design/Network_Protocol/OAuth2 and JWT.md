# OAuth2 & JWT

## 中文版

### OAuth2

一個**授權框架**，讓第三方應用程式在不取得使用者密碼的情況下，取得對使用者資源的有限存取權。

**核心角色**：
| 角色 | 說明 |
|------|------|
| Resource Owner | 使用者 |
| Client | 第三方應用程式 |
| Authorization Server | 負責驗證並發 token（如 Google、GitHub） |
| Resource Server | 存放使用者資源的 API |

**常見流程（Authorization Code Flow）**：
```
1. 使用者點「用 Google 登入」
2. 導向 Google 授權頁面
3. 使用者同意後，Google 回傳 Authorization Code
4. 後端用 Code 換取 Access Token
5. 用 Access Token 呼叫 Google API 取得資料
```

---

### JWT（JSON Web Token）

一個**自包含的 Token 格式**，由三部分組成：

```
Header.Payload.Signature
eyJhbGc...  .eyJ1c2Vy...  .SflKxw...
```

| 部分 | 內容 |
|------|------|
| Header | 算法（如 HS256）、Token 類型 |
| Payload | Claims（使用者 ID、角色、過期時間等） |
| Signature | 用 Secret Key 簽署，防止竄改 |

**優點**：無狀態，伺服器不需要儲存 Session；可跨服務驗證。
**缺點**：Token 無法提前撤銷（除非搭配黑名單或短 TTL）。

**OAuth2 vs JWT**：兩者不衝突。OAuth2 是授權框架，JWT 是 Token 格式；OAuth2 可以用 JWT 作為 Access Token。

## English Version

### OAuth2

An **authorization framework** that allows third-party applications to access user resources without obtaining the user's password.

**Core roles**:
| Role | Description |
|------|-------------|
| Resource Owner | The user |
| Client | Third-party application |
| Authorization Server | Issues tokens after authenticating the user (e.g., Google, GitHub) |
| Resource Server | API that hosts the user's protected resources |

**Common flow (Authorization Code Flow)**:
```
1. User clicks "Sign in with Google"
2. Redirected to Google's consent screen
3. User approves → Google returns an Authorization Code
4. Backend exchanges Code for an Access Token
5. Use Access Token to call Google API
```

---

### JWT (JSON Web Token)

A **self-contained token format** with three parts:

```
Header.Payload.Signature
```

| Part | Content |
|------|---------|
| Header | Algorithm (e.g., HS256), token type |
| Payload | Claims (user ID, roles, expiry, etc.) |
| Signature | Signed with a secret key to prevent tampering |

**Pros**: Stateless — server doesn't need to store session state; works across services.
**Cons**: Cannot be revoked before expiry (requires a blocklist or short TTL to mitigate).

**OAuth2 vs JWT**: Not mutually exclusive. OAuth2 is an authorization framework; JWT is a token format. OAuth2 can use JWT as the Access Token.
