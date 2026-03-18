# Rate Limiting

## 中文版

限制客戶端在一段時間內可以發送的請求數量，防止濫用、DoS 攻擊，保護系統穩定。

### 常見演算法

| 演算法 | 原理 | 特點 |
|--------|------|------|
| **Token Bucket** | 令牌桶以固定速率補充，每個請求消耗一個令牌 | 允許突發流量（burst），最常用 |
| **Leaky Bucket** | 請求排隊後以固定速率漏出 | 輸出平滑，不允許突發 |
| **Fixed Window** | 固定時間窗口（如每分鐘）計數 | 實作簡單，但有邊界問題（兩個窗口交界可被雙倍打） |
| **Sliding Window Log** | 記錄每個請求的時間戳 | 精確但記憶體消耗大 |
| **Sliding Window Counter** | Fixed Window + 前一窗口加權 | 精度與效能的平衡 |

### 實作位置
- **API Gateway**（最常見）：Nginx、Kong、AWS API Gateway
- **應用層**：Redis + Lua Script 實作分散式限流
- **客戶端**：SDK 層自主限制（輔助用）

### 限流後的回應
- HTTP `429 Too Many Requests`
- Header 回傳 `Retry-After`、`X-RateLimit-Remaining`

## English Version

Rate limiting restricts the number of requests a client can make within a time window, preventing abuse, DoS attacks, and protecting system stability.

### Common Algorithms

| Algorithm | How it works | Characteristics |
|-----------|-------------|-----------------|
| **Token Bucket** | Tokens refilled at fixed rate; each request consumes one token | Allows burst traffic; most common |
| **Leaky Bucket** | Requests queue up and drain at a fixed rate | Smooth output, no bursts |
| **Fixed Window** | Count requests within a fixed time window (e.g., per minute) | Simple to implement; boundary vulnerability (double rate at window edges) |
| **Sliding Window Log** | Record timestamp of each request | Accurate but memory-intensive |
| **Sliding Window Counter** | Fixed Window + weighted previous window | Balances accuracy and performance |

### Where to implement
- **API Gateway** (most common): Nginx, Kong, AWS API Gateway
- **Application layer**: Redis + Lua script for distributed rate limiting
- **Client SDK**: Self-throttling (supplementary)

### Response on limit exceeded
- HTTP `429 Too Many Requests`
- Include `Retry-After` and `X-RateLimit-Remaining` headers
