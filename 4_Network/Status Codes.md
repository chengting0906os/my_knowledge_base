# HTTP Status Codes (Common Interview Set)

## Status Code Classes (1xx-5xx)

- `1xx` Informational: Request received, continue process.
- `2xx` Success: Request succeeded.
- `3xx` Redirection: Further action needed (usually follow another URL or use cache result).
- `4xx` Client Error: Request has an issue on client side (input/auth/path/method, etc.).
- `5xx` Server Error: Server failed to handle a valid request.

## 1xx Informational

- `100 Continue`: Client can continue sending request body.
- `101 Switching Protocols`: Server accepts protocol upgrade (common example: HTTP -> WebSocket).

## 2xx Success

- `200 OK`: Request succeeded (typical for `GET`, `PUT`, `PATCH`, `DELETE` with response body).
- `201 Created`: Resource created successfully (common for `POST`).
- `202 Accepted`: Request accepted for async processing (not finished yet).
- `204 No Content`: Request succeeded, no response body (common for `DELETE`/`PUT`/`PATCH`).

## 3xx Redirection

- `301 Moved Permanently`: Permanent redirect.
  - Meaning: The resource URL has permanently changed.
  - Browser behavior: Usually caches the redirect and goes to the new URL directly next time.
  - SEO impact: Search engines treat this as permanent move and transfer ranking signals.
  - Common use cases:
    - Domain migration (`old.com` -> `new.com`)
    - Subdomain migration (`blog.example.com` -> `www.example.com/blog`)
    - Permanent URL/path change
    - Enforcing canonical URL structure
  - Example redirects:
    - `https://old.com/pricing` -> `https://new.com/pricing`
    - `https://m.example.com/product/123` -> `https://www.example.com/product/123`
    - `http://example.com` -> `https://www.example.com`
  - Typical response header: `Location: https://new-url`

- `304 Not Modified`: Reuse cached resource (no response body).
  - Meaning: Resource has not changed since the client cache version.
  - Sent after conditional request headers like:
    - `If-None-Match` (with `ETag`)
    - `If-Modified-Since` (with `Last-Modified`)
  - Common static resource cases:
    - CSS (`/static/app.css`)
    - JavaScript (`/static/app.js`)
    - Images (`/static/logo.png`)
    - Fonts (`/static/font.woff2`)
  - Benefit: Saves bandwidth and reduces response time.
  - Typical flow:
    - Client asks: "Has this changed?"
    - Server replies `304` -> client uses local cache.

## 4xx Client Errors

- `400 Bad Request`: Invalid request syntax/format/parameters.
- `401 Unauthorized`: Authentication required or invalid credentials.
- `403 Forbidden`: Authenticated but not allowed.
- `404 Not Found`: Resource does not exist.
- `405 Method Not Allowed`: Method not supported for this resource.
- `409 Conflict`: State conflict (for example, duplicate resource or version conflict).
- `422 Unprocessable Content`: Syntax is valid, but semantic validation fails.
- `429 Too Many Requests`: Rate limit exceeded.

## 5xx Server Errors

- `500 Internal Server Error`: Generic server-side failure.
- `502 Bad Gateway`: Upstream service returned invalid response.
- `503 Service Unavailable`: Service temporarily unavailable/overloaded/maintenance.
- `504 Gateway Timeout`: Upstream service did not respond in time.

## Quick REST Mapping

- Create: `POST` -> `201 Created`
- Read: `GET` -> `200 OK`
- Update: `PUT`/`PATCH` -> `200 OK` or `204 No Content`
- Delete: `DELETE` -> `204 No Content` (or `200 OK` if returning a body)

## Interview Pitfalls

- `401` vs `403`: `401` means "not authenticated", `403` means "authenticated but forbidden".
- `404` vs `403`: Some systems return `404` intentionally to hide resource existence.
- `500` vs `502/503/504`: `500` is your app error, others are often gateway/upstream related.

## 30s Interview Version

- `2xx` means success, `3xx` means redirect, `4xx` means client error, `5xx` means server error.

## Ref

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
