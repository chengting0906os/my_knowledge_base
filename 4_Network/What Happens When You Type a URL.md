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

2. TCP

3. TLS

4. Request

5. Response

---

## Reference

- [What happens when you type an URL in the browser and press enter?](https://medium.com/@maneesha.wijesinghe1/what-happens-when-you-type-an-url-in-the-browser-and-press-enter-bb0aa2449c1a)
