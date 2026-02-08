- You type `https://www.gamer.com.tw/` into the address bar of your browser.

1. DNS / Find IP
   - The browser checks the cache for a DNS record to find the corresponding IP address.
     - browser cache
     - OS cache
     - host file
     - router cache
     - ISP(Internet Service Provider(e.g. Chunghwa Telecom)) DNS Resolver checks its cache.
       If all caches miss, the same resolver performs iterative queries:
       - Root → TLD → Second-level → Authoritative DNS

> **TLD (Top-Level Domain):** the last part of a domain name.
> e.g. `.com`, `.org`, `.io`, `.tw`
>
> ```
> www.gamer.com.tw
> │    │     │   │
> │    │     │   └─ TLD (.tw)
> │    │     └───── Second-level (.com.tw)
> │    └─────────── Domain name (gamer)
> └──────────────── Subdomain (www)
> ```
>
> **DNS resolution path:**
>
> - **Root DNS** — "Here is the DNS server for `.tw`"
> - **TLD DNS (.tw)** — "Here is the DNS server for `.com.tw`"
> - **.com.tw DNS** — "Here is the Authoritative server for `gamer.com.tw`"
> - **Authoritative DNS** — "`www.gamer.com.tw`'s IP is 60.x.x.x"

2. TCP - The browser initiates a TCP connection with the server.

- 1. Client sends SYN, seq = ISN_client (random initial sequence number)
- 2. Server returns SYN-ACK, seq = ISN_server, ack = ISN_client + 1
- 3. Client sends ACK, seq = ISN_client + 1, ack = ISN_server + 1
- Then a TCP connection is established for data transmission!

> **ISN (Initial Sequence Number):** a random starting number picked by each side.
>
> - Prevents old packets from previous connections being mistaken as new
> - Harder for attackers to guess and hijack the connection

3. TLS Handshake - Since the URL uses `https://`, the browser performs a TLS handshake to establish a secure connection.

- 1. Client Hello — Client sends highest supported TLS version, supported cipher suites, and a random number
- 2. Server Hello — Server picks a cipher suite, sends its SSL certificate and a random number
- 3. Certificate Verification — Client verifies the certificate with a Certificate Authority (CA)
- 4. Key Exchange — Both sides generate a shared session key (using asymmetric encryption)
- 5. Secure Connection — All further data is encrypted with the session key (symmetric encryption)

> **Cipher Suite** — a "security contract" negotiated during the TLS handshake.
>
> Format: `TLS_<KeyExchange>_<Authentication>_WITH_<Encryption>_<Integrity>`
>
> | Stage | Purpose | Example |
> |---|---|---|
> | Key Exchange | Securely negotiate a symmetric key | ECDHE (provides Forward Secrecy — past sessions stay safe even if private key leaks) |
> | Authentication | Server proves its identity | RSA (digital signature verification) |
> | Encryption | Encrypt the actual data | AES_256_GCM (256-bit AES in GCM mode) |
> | Integrity | Detect data tampering | SHA384 (generates MAC/Tag to verify data integrity) |

> **Why both asymmetric and symmetric?**
> - Asymmetric (RSA) is slow but secure — used only for exchanging the key
> - Symmetric (AES) is fast — used for encrypting all actual data

4. HTTP Request - The browser sends an HTTP request to the server.

- Method: GET, POST, PUT, DELETE, etc.
- Headers: Host, User-Agent, Cookie, Accept, etc.
- Body: (for POST/PUT requests)

```
GET https://www.gamer.com.tw/ HTTP/1.1
Accept: text/html, application/xhtml+xml, [...]
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) [...]
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
Host: www.gamer.com.tw
Cookie: ckBAHAD=1; ckBIDE=1; [...]
```

5. HTTP Response - The server processes the request and sends back a response.

- Status Code: 200 OK, 301 Redirect, 404 Not Found, 500 Server Error, etc.
- Headers: Content-Type, Set-Cookie, Cache-Control, etc.
- Body: HTML, JSON, etc.

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Cache-Control: no-cache
Set-Cookie: session_id=abc123; HttpOnly; Secure

{
  "status": "success",
  "data": {
    "title": "Gamer Forum",
    "posts": [...]
  }
}
```

6. Browser Rendering - The browser renders the page.

- Parses HTML → builds DOM tree
- Parses CSS → builds CSSOM tree
- Combines DOM + CSSOM → Render tree
- Layout → calculates position and size
- Paint → draws pixels on the screen

---

## Quiz

1. What is the full DNS cache lookup order before a query is made?
2. What is the difference between an ISP DNS Resolver and an Authoritative DNS server?
3. Explain the three-way handshake. What does each packet contain?
4. What is ISN and why is it random?
5. What happens during the TLS handshake? List the 5 steps.
6. What is a Cipher Suite? What are its 4 components?
7. Why does TLS use both asymmetric and symmetric encryption?
8. What is the difference between Forward Secrecy and regular key exchange?
9. Name at least 3 HTTP request headers and explain what they do.
10. What are the 5 steps of browser rendering?

---

## Reference

- [What happens when you type an URL in the browser and press enter?](https://medium.com/@maneesha.wijesinghe1/what-happens-when-you-type-an-url-in-the-browser-and-press-enter-bb0aa2449c1a)
- [What happens when...](https://github.com/alex/what-happens-when/)
- [從 SSL 到 TLS 1.3 — 了解 TLS Cipher Suite 與通訊建立傳輸細節](https://medium.com/kiwibyteswalk/%E5%BE%9E-ssl-%E5%88%B0-tls-1-3-%E4%BA%86%E8%A7%A3-tls-cipher-suite-%E8%88%87%E9%80%9A%E8%A8%8A%E5%BB%BA%E7%AB%8B%E5%82%B3%E8%BC%B8%E7%B4%B0%E7%AF%80-fc5213660a4a)
