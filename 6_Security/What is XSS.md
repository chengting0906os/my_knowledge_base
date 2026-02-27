# XSS (Cross-Site Scripting)

## Overview

XSS（跨站腳本攻擊）是攻擊者把惡意 JavaScript 注入到網頁中，讓其他使用者的瀏覽器執行。  
一旦成功，攻擊者可能竊取資料、冒用操作、或竄改頁面內容。

關鍵點：XSS 的核心是「讓受害者瀏覽器執行了不該執行的腳本」。

## Common Types

### 1 Stored XSS

- 惡意腳本先被存進資料庫（例如留言、個人簡介）
- 其他使用者開頁面時，腳本被伺服器回傳並執行

### 2 Reflected XSS

- 惡意內容放在 URL / 查詢參數
- 伺服器把輸入原樣反射到回應頁面，導致腳本執行

### 3 DOM-based XSS

- 問題在前端 JavaScript
- 前端把不可信輸入寫進危險 DOM API（如 `innerHTML`），不經後端也可能中招

## Attack Impact

- 竊取敏感資料（如非 `HttpOnly` cookie、token、表單資訊）
- 冒用使用者操作（發送請求、改帳號設定）
- 釣魚或頁面篡改（插入假登入視窗）

## Defenses (Practical)

### 1 Output Encoding（最重要）

- 依輸出位置做正確編碼（HTML / Attribute / URL / JS context）
- 不把使用者輸入直接拼進 HTML 或 script

### 2 Input Validation + Sanitization

- 驗證輸入格式（白名單）
- 需要保留部分 HTML 時，使用可信 sanitizer

### 3 Safe DOM APIs

- 優先用 `textContent` / `innerText`
- 避免把不可信內容放進 `innerHTML`, `document.write`, `eval`

### 4 CSP（Defense in Depth）

- 用 CSP 限制可執行腳本來源
- 避免 `unsafe-inline`，優先 `nonce` / `hash`
 Cookie Hardening

- Session cookie 設 `HttpOnly` + `Secure` + 合理 `SameSite`
- 可降低 XSS 成功後造成的連帶損害

## Quick Checklist

- 模板輸出是否預設 escaping？
- 是否有把 user input 直接塞進 `innerHTML`？
- 是否導入 CSP 並避免 `unsafe-inline`？
- 重要 cookie 是否設 `HttpOnly` / `Secure`？

## Interview Version (30s)

XSS 是把惡意腳本注入網頁，讓受害者瀏覽器執行。常見有 Stored、Reflected、DOM-based 三種。防禦核心是正確輸出編碼與安全 DOM 操作，避免把不可信輸入直接渲染為 HTML；另外再用 CSP、`HttpOnly` cookie 做第二層防護。

## Reference

- https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/XSS
- https://owasp.org/www-community/attacks/xss/
