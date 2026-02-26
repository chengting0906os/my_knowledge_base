# Same Origin Policy

## Overview

同源政策（Same-Origin Policy, SOP）是瀏覽器的核心安全機制。  
它限制「一個網頁中的 JavaScript」去讀取其他來源的資料，避免惡意網站偷看你在別站的敏感資訊。

兩個 URL 要算「同源」，必須同時相同：

- Protocol（協定），例如 `https`
- Host（網域），例如 `example.com`
- Port（埠號），例如 `443`

只要其中一個不同，就屬於跨來源（cross-origin），瀏覽器就會套用額外限制。

Same-Origin Policy (SOP) is a core browser security rule.  
It restricts JavaScript on one page from reading data from another origin, helping prevent data theft across sites.

Two URLs are considered the same origin only if all three match:

- Protocol (e.g., `https`)
- Host (e.g., `example.com`)
- Port (e.g., `443`)

If any one of them differs, it is cross-origin and browser restrictions apply.

## How to allow cross-origin access

Use CORS to allow controlled cross-origin access.  
CORS lets the server explicitly tell the browser which origins are allowed to read the response.

## Cross-origin Network Access (Casual Version)

你可以把跨來源互動想成三件事：寫、嵌入、讀。

- 寫（write）通常可以：像點連結跳轉、form submit、redirect，大多都能送出去（有些請求會先 preflight）。
- 嵌入（embed）通常也可以：像放 `<img>`、`<script>`、`<iframe>`，瀏覽器通常會讓你載入。
- 讀（read）通常不行：JS 不能直接把別站回應內容讀出來。但有時會從「嵌入行為」側漏一些資訊，例如圖片尺寸、script 有沒有成功執行、資源是否存在。

English (casual):
Think of cross-origin access in 3 buckets: write, embed, and read.

- Write is usually allowed: links, redirects, and form submits can usually be sent (some requests trigger preflight).
- Embed is usually allowed: resources like `<img>`, `<script>`, or `<iframe>` can usually be loaded.
- Read is usually blocked: JavaScript normally cannot read cross-origin response data directly. But some signals may still leak through embedding behavior, like image size, whether a script executed, or whether a resource exists.

## Common Cross-origin Embedding Examples

下面這些資源通常可以「跨來源嵌入」：

- JavaScript：`<script src="..."></script>`  
  但語法錯誤的詳細資訊通常只有同源腳本才看得到。
- CSS：`<link rel="stylesheet" href="...">`  
  跨來源 CSS 對 `Content-Type` 比較嚴格；MIME type 不對時，瀏覽器可能直接擋下。
- 圖片：`<img>`
- 影音：`<video>`、`<audio>`
- 外部物件：`<object>`、`<embed>`
- 字型：`@font-face`  
  不同瀏覽器政策不完全一致，有些可跨來源，有些要求同源或 CORS。
- iframe：`<iframe>`  
  目標網站可用 `X-Frame-Options`（或 CSP `frame-ancestors`）禁止被跨站嵌入。

English:
These resources are commonly embeddable across origins:

- JavaScript via `<script src="..."></script>`  
  Detailed syntax error info is usually only available for same-origin scripts.
- CSS via `<link rel="stylesheet" href="...">`  
  Cross-origin stylesheets are stricter about `Content-Type`; browsers may block invalid MIME types.
- Images via `<img>`
- Media via `<video>` and `<audio>`
- External resources via `<object>` and `<embed>`
- Fonts via `@font-face`  
  Browser behavior differs; some allow cross-origin fonts, others require same-origin/CORS.
- Content via `<iframe>`  
  Sites can block cross-origin framing with `X-Frame-Options` (or CSP `frame-ancestors`).

## Interview Version (30s)

中文：
Same-Origin Policy 是瀏覽器的安全機制，限制前端 JavaScript 只能讀取同源資源。所謂同源，必須 protocol、host、port 三者都相同；任一不同就是 cross-origin。跨來源需求通常用 CORS，由伺服器透過 `Access-Control-Allow-*` 標頭明確告訴瀏覽器哪些來源可以讀取回應。

English:
Same-Origin Policy is a browser security rule that prevents frontend JavaScript from reading data across origins. Two URLs are same-origin only when protocol, host, and port all match. If cross-origin access is needed, the server uses CORS headers (`Access-Control-Allow-*`) to explicitly allow specific origins.

https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy
