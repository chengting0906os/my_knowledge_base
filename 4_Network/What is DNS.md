# 什麼是 DNS

## DNS 是什麼

DNS（Domain Name System）是網際網路的「電話簿」。
它把人類好記的網域名稱（例如 `www.example.com`）轉成機器連線要用的 IP 位址（例如 `93.184.216.34`）。

## 為什麼重要

- 使用者不用記 IP，只要記網域名稱。
- 服務可換機器或換 IP，但網域名稱不必改。
- 可做流量分流、容錯、地區導流（搭配 CDN / DNS 策略）。

## DNS 解析流程（高頻面試題）

1. 使用者輸入 `www.example.com`
2. 先查快取（browser -> OS -> router -> ISP resolver）
   - ISP = Internet Service Provider（網際網路服務供應商）
   - ISP resolver = 由 ISP 提供的 DNS 遞迴解析器
   - 例子：中華電信、台灣大哥大、遠傳等業者的 DNS
3. 若快取 miss，遞迴解析器（recursive resolver）去查：
   - Root DNS：告訴你 `.com` 在哪
   - TLD (Top-Level Domain) DNS（`.com`）：告訴你 `example.com` 權威 DNS 在哪
   - Authoritative DNS：回覆最終紀錄（A/AAAA/CNAME 等）
4. 解析器把結果回給客戶端，並依 TTL 快取一段時間

## 遞迴查詢 vs 迭代查詢（哪裡發生）

- 遞迴查詢（Recursive Query）發生在：
  - Client -> Recursive Resolver
  - 你只問一次：「`www.example.com` 的 IP 是多少？」
  - Resolver 先查自己的快取：
    - 有快取：直接回你答案
    - 沒快取：再去幫你往外查（Root -> TLD -> Authoritative）
  - 對 Client 來說，你不用自己一層一層問，Resolver 會把最終答案（或失敗）回給你。

- 迭代查詢（Iterative Query）發生在：
  - Recursive Resolver -> Root/TLD/Authoritative DNS
  - 每一站如果不知道最終答案，就只回「下一站要問誰」。
  - 例如：
    - Root：去問 `.com` TLD
    - TLD：去問 `example.com` 的 authoritative DNS
    - Authoritative：回最終 IP

簡化記法：

- 使用者對 Resolver：遞迴（要 final answer）
- Resolver 對 DNS 階層：迭代（一步一步問）

## Cloudflare 常見講法：4 個 DNS 角色

- DNS Recursor（遞迴解析器）
- Root Nameserver
- TLD (Top-Level Domain) Nameserver
- Authoritative Nameserver

你可以把它理解成：Recursor 幫你一路問到底，Root/TLD 一層一層指路，最後由 Authoritative 回最終答案。

## 8 Steps（無快取時）

1. Client 把 `example.com` 查詢送給 recursive resolver
2. Resolver 問 root nameserver
3. Root 回覆 `.com` TLD 的位置
4. Resolver 問 `.com` TLD
5. TLD 回覆 `example.com` authoritative nameserver 的位置
6. Resolver 問 authoritative nameserver
7. Authoritative 回覆 IP（A/AAAA 記錄）
8. Resolver 回覆 client，client 才能去發 HTTP/HTTPS 請求

補充：如果快取命中，這些步驟會被大幅縮短。

## Recursive vs Authoritative

- Recursive Resolver（遞迴解析器）：
  - 幫客戶端一路查到底
  - 會做快取（常見是 ISP DNS、8.8.8.8、1.1.1.1）
- Authoritative DNS（權威 DNS）：
  - 擁有某個網域的最終資料
  - 回覆該網域「正確答案」

## 常見 DNS Record 類型

- `A`：網域 -> IPv4
- `AAAA`：網域 -> IPv6
- `CNAME`：別名 -> 另一個網域名稱
- `MX`：郵件伺服器
- `TXT`：文字紀錄（常見 SPF/DKIM/驗證用途）
- `NS`：該網域的名稱伺服器

## TTL 與快取

- TTL（Time To Live）是 DNS 紀錄可被快取多久（秒）。
- TTL 高：
  - 優點：查詢量小、效能好
  - 缺點：異動生效慢
- TTL 低：
  - 優點：異動生效快
  - 缺點：查詢量增加

## 常見問題

- DNS Propagation（傳播延遲）：
  - 改完紀錄後，不同地區/ISP 可能要一段時間才看到新結果。
- DNS Cache 汙染或舊快取：
  - 可能導致使用者連到舊 IP。
- 設定錯誤：
  - NS、A、CNAME 錯配會直接導致網站無法解析。


## 30 秒面試版

DNS 是把網域名稱轉成 IP 的分散式系統。解析時會先查快取，miss 才由 recursive resolver 逐層查 Root -> TLD -> Authoritative。常見紀錄有 A/AAAA/CNAME/MX/TXT/NS。TTL 決定快取時間，影響生效速度與查詢量。

## Ref

- https://www.cloudflare.com/learning/dns/what-is-dns/
