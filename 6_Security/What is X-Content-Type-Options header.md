# X-Content-Type-Options: nosniff

## Overview

`X-Content-Type-Options` 是一個 HTTP Response Header，常見且實務上幾乎固定設為：

```http
X-Content-Type-Options: nosniff
```

它的目的：告訴瀏覽器「不要做 MIME type sniffing（內容嗅探）」。

## Why It Matters

若沒有 `nosniff`，瀏覽器有時會「猜測」檔案型別。  
這可能導致：

- 原本應該是非腳本資源，被當成 JavaScript 執行
- `Content-Type` 標示錯誤時，增加 XSS/資源注入風險

加上 `nosniff` 後，瀏覽器會更嚴格依照伺服器宣告的 `Content-Type` 處理資源。

## Typical Example

如果一個回應內容其實是 JS，但 `Content-Type` 被錯誤設成 `text/plain`：

- 沒有 `nosniff`：某些瀏覽器可能仍嘗試解析/執行
- 有 `nosniff`：瀏覽器會拒絕把它當 script/style 使用

## What It Does Not Replace

- 不能取代 CSP
- 不能取代輸入驗證與輸出編碼
- 不能單獨防所有 XSS

實務上是「基礎防護 header」之一，應與 CSP、`HttpOnly`、`Secure`、`SameSite` 一起使用。

## Django Configuration Example

在 Django 中，通常用 `SecurityMiddleware` + `SECURE_CONTENT_TYPE_NOSNIFF`。

### 1. 確認有啟用 SecurityMiddleware

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # ...
]
```

### 2. 在 `settings.py` 設定

```python
SECURE_CONTENT_TYPE_NOSNIFF = True
```

啟用後，Django 會在回應加上：

```http
X-Content-Type-Options: nosniff
```

## Verify It

部署後可用：

```bash
curl -I https://your-domain.com
```

確認回應 header 內有：

```http
X-Content-Type-Options: nosniff
```

## Interview Version (30s)

`X-Content-Type-Options: nosniff` 用來禁止瀏覽器做 MIME sniffing，避免把錯誤型別的回應當成可執行資源，降低資源注入與 XSS 風險。Django 可透過 `SecurityMiddleware` 搭配 `SECURE_CONTENT_TYPE_NOSNIFF = True` 開啟，並用 `curl -I` 驗證 header 是否存在。
