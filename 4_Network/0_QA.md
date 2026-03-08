# Network Interview Q&A List

1.  What is HTTP, and what does it define in a request and response?  
    什麼是 HTTP？它在 request / response 中定義了哪些內容？
     <details>
     <summary>Answer</summary>
     - HTTP 是應用層協議，定義 client 與 server 的通訊格式
     - 特性：無狀態（stateless），每個 request 獨立
     - Request：method、URL、headers、body
     - Response：status code、headers、body
     </details>

2.  What are the key differences between HTTP and HTTPS?  
    HTTP 和 HTTPS 的核心差異是什麼？
    <details>
    <summary>Answer</summary>
    HTTPS = HTTP + TLS，加入加密、資料完整性驗證、身份驗證
    - 瀏覽器會檢查憑證是否由受信任的 CA（Certificate Authority）簽發
    - HTTP 明文傳輸，沒有加密，容易被竊聽或篡改
    </details>

3.  What does TLS add on top of HTTP?  
    TLS 在 HTTP 之上多提供了哪些能力？
    <details>
    <summary>Answer</summary>
    - 加密：用非對稱加密交換 session key，之後改對稱加密傳輸
    - 完整性驗證：用 MAC（Message Authentication Code）確保資料沒被篡改
    - 身份驗證：server 出示 TLS 憑證，由 CA（Certificate Authority）簽發，防止中間人冒充
    </details>

4.  What is the difference between HTTP/1.0, HTTP/1.1, HTTP/2, and HTTP/3?
    HTTP/1.0, HTTP/1.1、HTTP/2、HTTP/3 的差異是什麼？
    <details>
    <summary>Answer</summary>
    - HTTP/1.0：每個 request 都要重新建立 TCP 連線，效率差
    - HTTP/1.1：預設持久連線（keep-alive），多個 request 共用同一條 TCP 連線，但同一連線同時只能處理一個 request，有 HOL blocking（Head-of-Line blocking，隊頭阻塞）；瀏覽器用開 6 條 TCP 連線來繞過限制
    - HTTP/2：二進制傳輸、多路復用（Multiplexing，同一連線併發多個 stream），解決 HTTP 層 HOL，但底層 TCP 丟包仍會卡住所有 stream
    - HTTP/3：改用 QUIC（Quick UDP Internet Connections，基於 UDP），每個 stream 獨立，單一丟包不影響其他 stream，消除 TCP 層 HOL blocking
    </details>

5.  Why can HTTP/3 reduce TCP-level head-of-line blocking effects?  
    為什麼 HTTP/3 可以降低 TCP 層 HOL 影響？
    <details>
     <summary>Answer</summary>
     - TCP 是 byte stream，丟一個封包整條連線都要等重傳，所有 stream 一起卡
     - QUIC 的每個 stream 各自有序號且獨立傳輸
     </details>

6.  What is 0-RTT in HTTP/3/QUIC, and what is the replay-risk caveat?
    HTTP/3/QUIC 的 0-RTT 是什麼？有哪些 replay 風險？
    <details>
    <summary>Answer</summary>
    - 正常 TLS 建連需 1 RTT 握手才能送資料；若 client 曾連過此 server，可用上次的 session ticket，連線時直接帶資料送出，RTT = 0
    - Replay 風險：0-RTT 資料在握手前送出，server 無法辨別是新 request 還是攻擊者重放的
    - 因此 0-RTT 只適合冪等操作（如 GET），POST/PUT 等有副作用的操作不應使用
    - RFC 8470 標準解法：proxy 轉發時加 `Early-Data: 1` header；server 判斷不安全則回 `425 Too Early`，要求 client 等握手完成後重試
    </details>

7.  What are common HTTP methods, and how do PUT, POST, and PATCH differ?  
    常見 HTTP Method 有哪些？PUT、POST、PATCH 差在哪？
    <details>
    <summary>Answer</summary>
    - POST 建立資源，可能有副作用
    - PUT 完整替換資源，有冪等性
    - PATCH 部分更新資源，不保證冪等性
    </details>

8.  What does idempotent mean in HTTP?  
    HTTP 裡的冪等性（idempotent）是什麼意思？
    <details>
    <summary>Answer</summary>
    每次操作結果相同，不管呼叫幾次，server 的最終狀態都一樣
    </details>

9.  What are the differences between status code classes 1xx, 2xx, 3xx, 4xx, and 5xx?  
    1xx、2xx、3xx、4xx、5xx 狀態碼各代表什麼？

10. In practice, when would you return 200 vs 201 vs 204?  
    實務上什麼時候回 200、201、204？

11. What is `301 Moved Permanently`, and when should you use it?
    `301 Moved Permanently` 什麼情況會用？
    <details>
    <summary>Answer</summary>
    - 資源永久移到新 URL，瀏覽器會快取此重定向，之後直接去新 URL
    - 用在網站搬家、URL 改版（如 http → https）
    </details>

12. What is `304 Not Modified`, and how does it relate to cache validation?
    `304 Not Modified` 是什麼？和快取有什麼關係？
    <details>
    <summary>Answer</summary>
    - server 告訴瀏覽器「你快取的還是最新版，直接用」，不回傳 body，省頻寬
    - 搭配 ETag（If-None-Match）或 Last-Modified（If-Modified-Since）使用
    </details>

13. What are ETag and Last-Modified, and how do they work with conditional requests?
    ETag 與 Last-Modified 是什麼？如何配合條件式請求？
    <details>
    <summary>Answer</summary>
    - 都是快取驗證機制，讓瀏覽器問 server「我快取的東西還有效嗎？」
    - Last-Modified：資源最後修改時間；下次請求帶 `If-Modified-Since`，沒改則回 `304`
    - ETag：資源的版本識別碼（hash）；下次請求帶 `If-None-Match`，一樣則回 `304`
    - ETag 更精確：Last-Modified 精度只到秒，同一秒改兩次會失效；ETag 基於內容
    </details>

14. What is DNS, and why is it required before connecting to a website?  
    什麼是 DNS？為什麼連網站前一定要先做 DNS 解析？
    <details>
    <summary>Answer</summary>
    根據網址做 DNS 解析出 IP
    </details>

15. Walk through DNS resolution from cache to Root -> TLD -> Authoritative.
    請描述 DNS 從快取到 Root -> TLD -> Authoritative 的流程。
    <details>
    <summary>Answer</summary>
    1. **瀏覽器 cache** — 先查瀏覽器自己的快取
    2. **OS cache** — 查作業系統 DNS cache（含 `/etc/hosts`）
    3. **Router cache** — 查家用路由器的 DNS 快取
    4. **Recursive Resolver**（ISP, Internet Service Provider / `8.8.8.8`）— 有快取直接回傳
    5. **Root Nameserver** — 回答「去問 `.com` TLD server」
    6. **TLD Nameserver**（Top-Level Domain，`.com`）— 回答「去問 `google.com` Authoritative server」
    7. **Authoritative Nameserver** — 回傳最終 IP（如 `142.250.80.46`）
    8. **回傳 + 快取** — Resolver 快取結果（TTL 秒數），並回傳給用戶端

    ```
    Browser cache
      → OS cache
        → Router cache
          → Recursive Resolver (ISP / 8.8.8.8)
            → Root NS:       "問 .com TLD"
            → TLD NS (.com): "問 google.com NS"
            → Authoritative: "IP = 142.250.80.46"
        ← 快取並回傳
      ← 拿到 IP，建立 TCP 連線
    ```

    - 前三層命中就不往下查
    - Root server 全球 13 組（anycast，實際幾百台）
    - Authoritative server 是最終答案來源
    </details>

16. Where is recursive query used, and where is iterative query used in DNS resolution?
    DNS 哪裡用遞迴查詢？哪裡用迭代查詢？
    <details>
    <summary>Answer</summary>
    - **遞迴查詢（Recursive Query）**：用戶端 → Recursive Resolver
      - 用戶端把問題丟給 Resolver，等 Resolver 幫你查完回傳最終答案
      - 用戶端不需要自己跑流程，全部交給 Resolver 處理
    - **迭代查詢（Iterative Query）**：Recursive Resolver → Root → TLD → Authoritative
      - Resolver 每次問一個 server，對方不直接給答案，而是「轉介」下一個 server
      - Resolver 自己一步一步往下問，直到拿到最終 IP

    ```
    用戶端  →（recursive）→  Resolver
                              ↓（iterative）
                           Root NS → "去問 TLD"
                              ↓
                           TLD NS → "去問 Authoritative"
                              ↓
                           Authoritative → IP
    ```

    </details>

17. What is the difference between a recursive resolver and an authoritative nameserver?
    Recursive resolver 和 Authoritative nameserver 差異是什麼？
    <details>
    <summary>Answer</summary>

    |          | Recursive Resolver            | Authoritative Nameserver         |
    | -------- | ----------------------------- | -------------------------------- |
    | 角色     | 代理人，幫用戶端查詢          | 最終來源，擁有域名的真實記錄     |
    | 資料來源 | 無自己的資料，向外查詢        | 直接存有 DNS records（A、MX 等） |
    | 快取     | 會快取查詢結果（TTL）         | 不快取，直接回傳權威答案         |
    | 例子     | `8.8.8.8`、`1.1.1.1`、ISP DNS | Google 自己的 NS、Cloudflare NS  |
    - Recursive Resolver 是「中間人」，負責跑流程
    - Authoritative Nameserver 是「終點」，負責給出最終答案
    </details>

18. What are common DNS record types (A, AAAA, CNAME, MX, TXT, NS)?
    常見 DNS record（A/AAAA/CNAME/MX/TXT/NS）各做什麼？
    <details>
    <summary>Answer</summary>

    | Record    | 用途                                         | 範例                               |
    | --------- | -------------------------------------------- | ---------------------------------- |
    | **A**     | 域名 → IPv4                                  | `google.com → 142.250.80.46`       |
    | **AAAA**  | 域名 → IPv6                                  | `google.com → 2404:6800::...`      |
    | **CNAME** | 域名 → 另一個域名（別名）                    | `www.example.com → example.com`    |
    | **MX**    | 指定收信的郵件伺服器                         | `example.com → mail.example.com`   |
    | **TXT**   | 存放任意文字，常用於驗證                     | SPF、DKIM、Google 網站驗證         |
    | **NS**    | 指定該域名由哪個 Authoritative Nameserver 管 | `example.com → ns1.cloudflare.com` |
    - CNAME(Canonical Name) 不能用在根域名（`example.com`），只能用在子域名（`www.example.com`）
    - MX 有優先權數字，數字越小優先級越高
    </details>

19. What is TTL in DNS, and how does it affect propagation and caching?
    DNS 的 TTL 是什麼？對快取與生效時間有何影響？
    <details>
    <summary>Answer</summary>

    **TTL（Time To Live）** 是 DNS record 上設定的數字（單位：秒），告訴 Resolver 這筆記錄可以快取多久。
    - TTL = 300 → Resolver 快取 5 分鐘，5 分鐘後才重新查詢
    - TTL 到期前，即使你改了 DNS record，用戶端仍會拿到舊的快取結果

    **對快取的影響：**
    - TTL 大（如 86400，一天）→ 快取久，查詢少，但改動生效慢
    - TTL 小（如 60，一分鐘）→ 快取短，改動生效快，但查詢頻率高

    **實務應用：**
    - 計劃做 DNS 切換（換 IP、換 CDN）前，提前把 TTL 調小（如 300），讓舊快取快點過期
    - 切換完成後再把 TTL 調回大值，減少查詢壓力
    </details>

20. What is TCP, and what makes it reliable?  
    什麼是 TCP？它為什麼可靠？

21. Explain TCP three-way handshake and why sequence/ack numbers matter.
    解釋 TCP 三向交握，sequence/ack number 的意義是什麼？
    <details>
    <summary>Answer</summary>

    **三向交握流程：**

    ```
    Client                        Server
      |  SYN (seq=x)                |
      | --------------------------→ |  第一次：Client 發起連線，x 是隨機產生的初始序號（ISN, Initial Sequence Number）
      |                             |
      |  SYN-ACK (seq=y, ack=x+1)  |
      | ←-------------------------- |  第二次：Server 同意，帶自己的 seq，並確認 x+1
      |                             |
      |  ACK (ack=y+1)              |
      | --------------------------→ |  第三次：Client 確認 y+1，連線建立
    ```

    **Sequence Number（seq）：**
    - 初始值是隨機產生的 ISN（Initial Sequence Number），避免被猜測或與舊連線混淆
    - seq 是**資料流的 byte 偏移量**，不是封包編號
    - 標記「這段資料在整個資料流裡從第幾個 byte 開始」
    - 讓接收方能把亂序到達的封包依偏移量重新排列，並偵測遺失封包（發現 seq 有缺口就要求重傳）

    **Acknowledgment Number（ack）：**
    - ack 也是**資料流的 byte 偏移量**，指向「下一個期望收到的 byte 位置」
    - `ack = 對方的 seq + 收到的 byte 數`
    - 告訴對方「0 ~ ack-1 我都收到了，請從 ack 繼續送」
    - 用於確認收到、偵測遺失封包

    **為什麼需要三次？**
    - 一次：只有 Client 確認 Server 在線
    - 兩次：只有 Server 確認 Client 在線
    - 三次：雙方都確認對方能收能送，連線才算可靠建立
    </details>

22. How do flow control and congestion control differ in TCP?
    TCP 的 flow control 與 congestion control 差在哪？
    <details>
    <summary>Answer</summary>

    |      | Flow Control                                                   | Congestion Control                                              |
    | ---- | -------------------------------------------------------------- | --------------------------------------------------------------- |
    | 目的 | 防止 sender 送太快，**接收方**來不及處理                       | 防止 sender 送太快，**網路**（路由器）來不及處理                |
    | 針對 | 端對端（sender ↔ receiver）                                    | sender 與網路之間                                               |
    | 機制 | Receiver 在 ack 裡帶 **Window Size**，告訴 sender 最多能送多少 | sender 維護 **Congestion Window（cwnd）**，偵測到封包遺失就縮小 |
    - **Flow Control**：receiver 說「我 buffer 只剩 X bytes，你最多送 X」
    - **Congestion Control**：sender 自己偵測網路壅塞（封包遺失、延遲增加），主動降速
    </details>

23. What are the key differences between TCP and UDP?
    TCP 與 UDP 的核心差異是什麼？
    <details>
    <summary>Answer</summary>

    |                         | TCP                             | UDP                                   |
    | ----------------------- | ------------------------------- | ------------------------------------- |
    | 連線                    | 需要三向交握建立連線            | 無連線，直接送                        |
    | 可靠性                  | 保證送達、有序、不重複          | 不保證送達，可能亂序、遺失            |
    | 速度                    | 較慢（有 overhead）             | 較快（低延遲）                        |
    | Flow/Congestion Control | 有                              | 無                                    |
    | Header 大小             | 20 bytes                        | 8 bytes                               |
    | 使用場景                | HTTP、SMTP、FTP（需要可靠傳輸） | DNS、影音串流、線上遊戲（需要低延遲） |
    - TCP 用在「資料不能遺失」的場景
    - UDP 用在「寧可掉包也要低延遲」的場景（如視訊通話掉幾幀比卡頓好）
    </details>

24. What is the OSI model, and what does each layer do?
    什麼是 OSI Model？七層各自負責什麼？
    <details>
    <summary>Answer</summary>

    OSI（Open Systems Interconnection）是網路通訊的七層參考模型，由上到下：

    | 層  | 名稱                    | 負責                             | 代表協議        |
    | --- | ----------------------- | -------------------------------- | --------------- |
    | 7   | Application（應用層）   | 使用者直接互動的網路服務         | HTTP、DNS、SMTP |
    | 6   | Presentation（表示層）  | 資料格式轉換、加密、壓縮         | TLS/SSL、JPEG   |
    | 5   | Session（會話層）       | 建立、管理、終止會話             | RPC             |
    | 4   | Transport（傳輸層）     | 端對端傳輸、可靠性、流量控制     | TCP、UDP        |
    | 3   | Network（網路層）       | 路由、定址、跨網路傳輸           | IP、ICMP        |
    | 2   | Data Link（資料連結層） | 同一網路內節點間傳輸、MAC 定址   | Ethernet、Wi-Fi |
    | 1   | Physical（實體層）      | 實際的位元傳輸（電、光、無線電） | 網路線、光纖    |

    記憶口訣（由下到上）：**Please Do Not Throw Sausage Pizza Away**
    </details>

25. How does the 4-layer TCP/IP model map to the 7-layer OSI model?
    四層 TCP/IP 模型如何對應到七層 OSI？
    <details>
    <summary>Answer</summary>

    ```
    OSI（7層）                    TCP/IP（4層）
    ┌─────────────────┐
    │ 7. Application  │
    │ 6. Presentation │  →  Application（應用層）
    │ 5. Session      │
    ├─────────────────┤
    │ 4. Transport    │  →  Transport（傳輸層）
    ├─────────────────┤
    │ 3. Network      │  →  Internet（網路層）
    ├─────────────────┤
    │ 2. Data Link    │
    │ 1. Physical     │  →  Network Access（網路存取層）
    └─────────────────┘
    ```

    - TCP/IP 把 OSI 上面三層合併為 Application
    - TCP/IP 把 OSI 下面兩層合併為 Network Access
    - 實務上用 TCP/IP 模型，OSI 是理論參考框架
    </details>

26. What is encapsulation/de-encapsulation in networking?
    什麼是封裝與解封裝（encapsulation / de-encapsulation）？
    <details>
    <summary>Answer</summary>

    **封裝（Encapsulation）**：資料從上層往下層傳，每一層加上自己的 header（有時加 trailer）

    ```
    Application  →  Data
    Transport    →  [TCP header | Data]           (Segment)
    Network      →  [IP header  | Segment]        (Packet)
    Data Link    →  [MAC header | Packet | FCS]   (Frame)
    Physical     →  實際位元傳輸
    ```

    **解封裝（De-encapsulation）**：接收方從下層往上層，每一層剝掉自己的 header

    ```
    Physical  →  收到位元
    Data Link →  剝掉 MAC header，取出 Packet
    Network   →  剝掉 IP header，取出 Segment
    Transport →  剝掉 TCP header，取出 Data
    Application → 拿到原始資料
    ```

    每一層只看自己的 header，不管上下層的內容，這讓各層可以獨立替換（如把 TCP 換成 UDP）。
    </details>

27. What is URI vs URL?  
    URI 和 URL 的差異是什麼？

28. What is the difference between Cookie and Session?  
    Cookie 和 Session 差異是什麼？

29. What is the difference between cookie, sessionStorage, and localStorage?  
    Cookie、sessionStorage、localStorage 差異是什麼？

30. CDN vs Reverse Proxy vs Load Balancer: how are they different and how do they work together?  
    CDN、Reverse Proxy、Load Balancer 各自做什麼？如何一起工作？

31. What is RTT vs latency vs bandwidth vs throughput?  
    RTT、latency、bandwidth、throughput 差異是什麼？

32. Why can high bandwidth still feel slow in user experience?  
    為什麼高頻寬不一定代表體感速度快？

33. What happens when you type a URL in the browser (high-level end-to-end flow)?  
    從輸入 URL 到頁面顯示，整體流程是什麼？

34. What is ARP (Address Resolution Protocol), and why is it needed in a local network?  
    ARP（Address Resolution Protocol，位址解析協定）是什麼？為什麼在同一個區網內需要它？

35. Why does IPv6 use NDP instead of ARP?  
    為什麼 IPv6 不是用 ARP，而是用 NDP？

36. In TCP, what does byte-stream mean, and why can one send become multiple receives (or vice versa)?  
    TCP 的 byte-stream 是什麼意思？為什麼一次 send 可能變多次 recv（或反過來）？

37. In UDP, what is a datagram boundary, and what are practical risks when packet size is too large?  
    UDP 的 datagram 邊界是什麼？封包太大在實務上有什麼風險？

38. In OSI, what is the difference between Session layer and Presentation layer?  
    在 OSI 中，Session layer 和 Presentation layer 差在哪？

39. What are the protocol data unit (PDU, Protocol Data Unit) names across layers (segment / packet / frame / bits)?  
    各層 PDU（Protocol Data Unit，協定資料單元）名稱是什麼（segment / packet / frame / bits）？

40. How is HTTP version selected in real systems (server policy + client negotiation, e.g., ALPN)?  
    實務上 HTTP 版本如何決定（伺服器策略 + 客戶端協商，例如 ALPN）？

41. Why is HTTP/3 not always significantly faster than HTTP/2 in benchmarks?  
    為什麼基準測試中 HTTP/3 不一定明顯快於 HTTP/2？

42. What is ICMP used for, and what is an ICMP flood attack?  
    ICMP 主要用途是什麼？什麼是 ICMP flood 攻擊？

43. How would you troubleshoot a network issue layer by layer (L1 -> L7)?  
    你會如何用 L1 -> L7 的方式逐層排查網路問題？

44. What is `101 Switching Protocols`, and when is it used (e.g., WebSocket upgrade)?  
    `101 Switching Protocols` 是什麼？什麼情境會用到（例如 WebSocket 升級）？
