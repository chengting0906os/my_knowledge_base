# Clickjacking

## Overview

Clickjacking（點擊劫持）是攻擊者把受害網站頁面藏在透明或偽裝的 `iframe` 中，誘導使用者點擊看起來無害的按鈕，實際上點到的是受害網站上的敏感操作。

白話：你以為你在點「播放」或「抽獎」，其實你點的是「轉帳」「刪除」「授權」。

## Attack Flow

1. 使用者已登入目標網站（瀏覽器有有效 cookie/session）。
2. 攻擊者網站把目標網站頁面嵌入 `iframe`，並做透明/遮罩處理。
3. 攻擊者放一個假按鈕，引導使用者去點。
4. 使用者實際點到 `iframe` 內的敏感操作。
5. 請求帶著使用者登入狀態送出，造成誤操作。

## Why It Works

- 使用者看不到真正被點擊的 UI。
- 瀏覽器允許頁面被其他網站 `iframe` 嵌入（若未特別防護）。
- 使用者對目標站可能已登入，請求會帶上既有憑證。

## Defenses (MDN Focus)

### 1 CSP `frame-ancestors`（首選）

限制哪些網站可以把你的頁面放進 `iframe`。

```http
Content-Security-Policy: frame-ancestors 'none';
```

```http
Content-Security-Policy: frame-ancestors 'self' https://partner.example;
```

- `'none'`：完全禁止被嵌入
- `'self'`：只允許同源嵌入

### 2 `X-Frame-Options`（相容性防線）

```http
X-Frame-Options: DENY
```

```http
X-Frame-Options: SAMEORIGIN
```

- `DENY`：完全禁止被 frame
- `SAMEORIGIN`：只允許同源 frame
- 若同時設定 `frame-ancestors` 與 `X-Frame-Options`，現代瀏覽器通常以 `frame-ancestors` 為主。

### 3 `SameSite` Cookie（輔助）

設定 `SameSite=Lax/Strict` 可降低跨站 iframe 帶上 cookie 的機會，減少攻擊成功率。  
但它不是 clickjacking 的唯一防線，主力仍是 `frame-ancestors` / `X-Frame-Options`。

## Practical Checklist

- 敏感頁面預設加 `Content-Security-Policy: frame-ancestors 'none'`
- 需要合法嵌入時改為精準白名單
- 補上 `X-Frame-Options` 兼容舊環境
- Session cookie 設定合適 `SameSite`

## Interview Version (30s)

Clickjacking 是把目標網站藏在透明 iframe 裡，誘導使用者誤點敏感操作。防禦重點是禁止或限制頁面被嵌入：首選 CSP `frame-ancestors`，並搭配 `X-Frame-Options` 做相容性防護；`SameSite` cookie 可作為輔助，降低跨站情境下請求帶憑證的機會。

## Reference

- https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Clickjacking
