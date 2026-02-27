# Content-Security-Policy (CSP)

## Overview

CSP（Content-Security-Policy，內容安全策略）是一種瀏覽器安全機制，通常透過 HTTP Response Header 設定。  
核心概念是「白名單」：明確允許哪些來源可載入資源，其餘一律拒絕。  
主要目標是降低 XSS、資料注入與資源被惡意替換的風險。

## Why It Matters

- 限制腳本來源，降低惡意 JavaScript 被執行的機會
- 限制 CSS、圖片、iframe、字型等資源來源，減少資料外洩面
- 讓前端資源載入行為更可控、可監控

## Common Setup Methods

### 1 HTTP Header（建議）

```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://apis.example.com
```

### 2 HTML meta（備用）

```html
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self'; script-src 'self' https://apis.example.com"
/>
```

通常優先用 HTTP Header；`meta` 比較適合無法改後端 header 的情境。

## Common Directives

- `default-src`: 預設資源來源規則
- `script-src`: JavaScript 來源規則（最重要）
- `style-src`: CSS 來源規則
- `img-src`: 圖片來源規則
- `frame-src`: iframe 載入來源規則

## Rollout Strategy (Practical)

1. 先用 `Content-Security-Policy-Report-Only` 上線觀察，不先阻擋
2. 在 DevTools / 報告中找出被擋的必要資源
3. 逐步收斂白名單，確認功能不壞
4. 再切成正式 `Content-Security-Policy`

## Best Practices

- 盡量不要用 `unsafe-inline`
- 需要內嵌腳本時，優先用 `nonce` 或 `hash`
- 把第三方來源縮到最小，避免過寬白名單
- 持續監控違規報告，定期調整規則

## Interview Version (30s)

CSP 是用 HTTP header 定義前端資源白名單的安全機制。它可限制 script、style、img、iframe 等載入來源，重點在降低 XSS 和資源注入風險。實務上會先用 `Report-Only` 蒐集違規，再逐步收斂政策，最後切到正式阻擋；另外應避免 `unsafe-inline`，改用 `nonce` 或 `hash`。

# ref

- https://realnewbie.com/posts/beginner-guide-understanding-content-security-policy-csp-and-web-security
