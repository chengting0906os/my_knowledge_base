# CSRF (Cross-Site Request Forgery)

## Overview

CSRF（跨站請求偽造）是指攻擊者誘導使用者瀏覽器，從惡意網站對目標網站發出「帶有使用者憑證」的請求（通常是 Cookie），讓伺服器誤以為是使用者本人操作。

關鍵點：CSRF 的本質不是「偷看回應內容」，而是「冒用使用者身分去做狀態變更」。

## 什麼情況容易被 CSRF

根據 MDN，通常同時滿足下列條件就有風險：

- 網站用 HTTP request 做狀態變更（例如轉帳、修改設定、刪除資料）
- 伺服器主要靠 Cookie 判斷登入狀態
- 請求參數可被攻擊者預測或偽造

## Attack Flow（面試可講）

1. 使用者已登入目標站（瀏覽器有有效 session cookie）
2. 使用者開啟惡意網站
3. 惡意網站觸發對目標站的請求（例如 form auto-submit）
4. 瀏覽器可能自動帶上目標站 cookie
5. 目標站若只看 cookie，就可能執行敏感操作

## Defenses（MDN 重點）

### 1) CSRF Token（主要防線）

- 伺服器在頁面放入不可預測 token
- 前端送出狀態變更請求時一併帶回 token
- 後端驗證 token 正確才執行

### 2) Fetch Metadata 檢查

- 後端檢查 `Sec-Fetch-Site` 等 header
- 通常只允許 `same-origin` / `same-site` 的敏感請求
- `cross-site` 請求可直接拒絕

### 3) 避免 Simple Request（特別是 fetch/XHR）

- 對狀態變更請求使用非 simple request（例如 `Content-Type: application/json` 或自訂 header）
- 讓跨站請求先卡在瀏覽器的預設限制（需通過 CORS 才能放行）
- 注意：若 CORS 設定過度寬鬆（尤其 `Access-Control-Allow-Credentials` + 放行攻擊來源），仍可能有風險

### 4) SameSite Cookie（Defense in Depth）

- `SameSite=Strict` 防護最強，但可能影響使用者流程
- `SameSite=Lax` 較常見，但防護較弱
- SameSite 是輔助，不應單獨依賴

## Checklist（實務）

- 找出所有 state-changing endpoints
- 不要用 `GET` 做狀態變更
- 至少落實一種主要防線（Token 或 Non-simple request 策略）
- 敏感 cookie 設定 `SameSite`（優先考慮 `Strict`，不行再 `Lax`）
- 補上 Fetch Metadata 驗證做額外防護

## Interview Version (30s)

CSRF 是攻擊者利用使用者已登入狀態，誘導瀏覽器對目標站送出「帶 cookie 的偽造請求」，讓伺服器誤以為是本人操作。常見防禦是 CSRF token；若是前後端 API，也可透過非 simple request + 嚴謹 CORS 降低風險。`SameSite` cookie 可以加強防護，但不該當唯一防線。

## Reference

- https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF
