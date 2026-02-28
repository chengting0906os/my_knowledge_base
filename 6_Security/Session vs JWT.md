# Session vs JWT

### 核心差異

- `Session`：狀態存在伺服器（server-side state），client 通常只存 session id（常放 cookie）。
- `JWT`：狀態主要放在 token 內（stateless），伺服器每次驗簽後即可判斷身份。

### 快速比較

| 項目     | Session                   | JWT                         |
| -------- | ------------------------- | --------------------------- |
| 狀態儲存 | 伺服器                    | Token（Client 持有）        |
| 撤銷能力 | 容易（刪 server session） | 較麻煩（常靠短效 + 黑名單） |
| 擴展性   | 需共享 session store      | 較容易橫向擴展              |
| 安全風險 | session 被竊取            | token 外洩可被重放直到過期  |
| 常見用途 | 傳統 Web、後台系統        | API、微服務、跨服務驗證     |

### 何時選哪個

- 想要「好控管登出/強制失效」：偏 `Session`。
- 想要「跨服務、低耦合、易擴展」：偏 `JWT`。

### 實務建議

- Web 場景常見做法：`HttpOnly + Secure + SameSite` cookie。
- JWT 建議：短效 access token + refresh token，並做金鑰輪替。

### 一句話

- Session 好管控；JWT 好擴展。選型看你的撤銷需求與系統規模。

---

### Core Difference

- `Session`: server stores auth state; client usually keeps only a session ID.
- `JWT`: auth claims are carried in a signed token; server validates token each request.

### Quick Comparison

| Aspect         | Session                    | JWT                              |
| -------------- | -------------------------- | -------------------------------- |
| State location | Server-side                | In token (client-held)           |
| Revocation     | Easy                       | Harder (short TTL + denylist)    |
| Scalability    | Needs shared session store | Easier horizontal scaling        |
| Main risk      | Stolen session ID          | Stolen token replay until expiry |
| Typical usage  | Traditional web apps       | APIs and distributed services    |

### When to Choose

- Need strict logout/invalidation control: choose `Session`.
- Need cross-service portability and scale: choose `JWT`.

### Practical Note

- For browser apps, prefer secure cookies (`HttpOnly`, `Secure`, `SameSite`).
- For JWT, use short-lived access tokens + refresh tokens and key rotation.

### One-liner

- Session is easier to control; JWT is easier to scale.
