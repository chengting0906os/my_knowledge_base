# Rate Limiter

## 是什麼

- Rate Limiter（限流）是限制「在一段時間內可發送多少請求」的機制。
- 目標是保護系統穩定性、避免資源被濫用，並提升公平性。

## 為什麼需要

- 防止暴力破解（login brute force）
- 防止 API 被刷爆（DoS / abuse）
- 保護高成本操作（寄信、簡訊、AI 推論、報表查詢）
- 避免單一租戶吃光資源（multi-tenant fairness）

## 常見限流維度（Key）

- 依使用者：`user_id`
- 依 API key：`api_key`
- 依 IP：`ip`
- 依路由：`method + path`
- 依租戶：`tenant_id`

實務常用多層：`global` + `per-user` + `per-endpoint` 一起上。

## 常見演算法

### 1. 固定窗口（Fixed Window）

- 例：每分鐘最多 100 次。
- 優點：實作最簡單、效能高。
- 缺點：窗口邊界可能突刺（59 秒打滿一次，60 秒再打滿一次）。

### 2. 滑動窗口（Sliding Window）

- 觀念：根據「當下往前 N 秒」計算，不吃整分鐘邊界。
- 優點：比固定窗口更平滑、更公平。
- 缺點：實作與儲存成本較高（尤其 sliding log）。

### 3. 令牌桶（Token Bucket）

- 觀念：桶內令牌固定速率補充；每個請求消耗 1 個令牌。
- 優點：允許短暫突發流量（burst），長期速率仍受控。
- 缺點：參數（桶大小、補充速率）需要調整。

## 回應行為（HTTP）

- 超限通常回 `429 Too Many Requests`。
- 可搭配 `Retry-After` 告知客戶端多久後重試。
- 也可回傳剩餘額度資訊（例如 `RateLimit-Limit`、`RateLimit-Remaining`、`RateLimit-Reset`）。

## 實務設計重點

- 儲存位置：
  - 單機可用記憶體
  - 分散式建議 Redis（原子操作）
- 原子性：
  - 避免 race condition，常用 Lua script 或原子指令
- 失效策略：
  - fail-open（限流系統掛掉先放行）或 fail-close（先擋）要先決策
- 白名單/灰名單：
  - 內部服務、健康檢查可放寬
- 觀測：
  - 要打 metrics/log（命中率、429 比例、熱點 key）

## 常見踩雷

- 只限 IP：NAT 後面會誤傷很多正常使用者
- 沒分 endpoint：昂貴 API 和便宜 API 用同一額度不合理
- 只做應用層限流：邊界（CDN/WAF/API Gateway）沒擋住，後端壓力仍大
- 忘記給重試資訊：client 無法合理 backoff

## 面試短答

Rate Limiter 是在時間窗口內限制請求數，常見有固定窗口、滑動窗口、令牌桶。  
實務上我會用 Redis 做分散式限流，回 429 + Retry-After，並採用多維度 key（user/ip/route）避免誤傷與濫用。

## Ref

- https://www.explainthis.io/zh-hant/swe/rate-limiter
- https://vocus.cc/article/68886aacfd897800017c2d8e
- https://datatracker.ietf.org/doc/html/rfc6585
- https://datatracker.ietf.org/doc/html/rfc9333
