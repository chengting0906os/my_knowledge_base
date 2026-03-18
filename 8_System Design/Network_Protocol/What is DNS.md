# What is DNS

## 中文版

DNS（Domain Name System）是網際網路的「電話簿」，將人類可讀的網域名稱（如 `google.com`）解析為機器可讀的 IP 位址（如 `142.250.80.46`）。

### 解析流程

```
瀏覽器輸入 google.com
    ↓
1. 查本地快取（瀏覽器 / OS）
    ↓ 沒有
2. 問 Recursive Resolver（通常是 ISP 或 8.8.8.8）
    ↓ 沒有
3. 問 Root Name Server（知道 .com 的位置）
    ↓
4. 問 TLD Name Server（知道 google.com 的位置）
    ↓
5. 問 Authoritative Name Server → 回傳 IP
    ↓
6. Recursive Resolver 快取並回傳給瀏覽器
```

### 常見 DNS 記錄類型

| 類型 | 用途 |
|------|------|
| A | 網域 → IPv4 |
| AAAA | 網域 → IPv6 |
| CNAME | 別名（alias）→ 另一個網域 |
| MX | 郵件伺服器 |
| TXT | 驗證、SPF、DKIM |

### TTL（Time To Live）
DNS 記錄的快取時間。TTL 短 → 更新快但查詢多；TTL 長 → 快取久但切換慢。

## English Version

DNS (Domain Name System) is the internet's "phone book" — it translates human-readable domain names (e.g., `google.com`) into machine-readable IP addresses (e.g., `142.250.80.46`).

### Resolution Flow

```
Browser enters google.com
    ↓
1. Check local cache (browser / OS)
    ↓ miss
2. Ask Recursive Resolver (ISP or 8.8.8.8)
    ↓ miss
3. Ask Root Name Server (knows where .com lives)
    ↓
4. Ask TLD Name Server (knows where google.com lives)
    ↓
5. Ask Authoritative Name Server → returns IP
    ↓
6. Recursive Resolver caches and returns IP to browser
```

### Common Record Types

| Type | Purpose |
|------|---------|
| A | Domain → IPv4 |
| AAAA | Domain → IPv6 |
| CNAME | Alias → another domain |
| MX | Mail server |
| TXT | Verification, SPF, DKIM |

### TTL (Time To Live)
How long a DNS record is cached. Short TTL → faster propagation but more queries; Long TTL → fewer queries but slower failover.
