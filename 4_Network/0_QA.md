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

12. What is `304 Not Modified`, and how does it relate to cache validation?  
    `304 Not Modified` 是什麼？和快取有什麼關係？

13. What are ETag and Last-Modified, and how do they work with conditional requests?  
    ETag 與 Last-Modified 是什麼？如何配合條件式請求？

14. What is DNS, and why is it required before connecting to a website?  
    什麼是 DNS？為什麼連網站前一定要先做 DNS 解析？

15. Walk through DNS resolution from cache to Root -> TLD -> Authoritative.  
    請描述 DNS 從快取到 Root -> TLD -> Authoritative 的流程。

16. Where is recursive query used, and where is iterative query used in DNS resolution?  
    DNS 哪裡用遞迴查詢？哪裡用迭代查詢？

17. What is the difference between a recursive resolver and an authoritative nameserver?  
    Recursive resolver 和 Authoritative nameserver 差異是什麼？

18. What are common DNS record types (A, AAAA, CNAME, MX, TXT, NS)?  
    常見 DNS record（A/AAAA/CNAME/MX/TXT/NS）各做什麼？

19. What is TTL in DNS, and how does it affect propagation and caching?  
    DNS 的 TTL 是什麼？對快取與生效時間有何影響？

20. What is TCP, and what makes it reliable?  
    什麼是 TCP？它為什麼可靠？

21. Explain TCP three-way handshake and why sequence/ack numbers matter.  
    解釋 TCP 三向交握，sequence/ack number 的意義是什麼？

22. How do flow control and congestion control differ in TCP?  
    TCP 的 flow control 與 congestion control 差在哪？

23. What are the key differences between TCP and UDP?  
    TCP 與 UDP 的核心差異是什麼？

24. What is the OSI model, and what does each layer do?  
    什麼是 OSI Model？七層各自負責什麼？

25. How does the 4-layer TCP/IP model map to the 7-layer OSI model?  
    四層 TCP/IP 模型如何對應到七層 OSI？

26. What is encapsulation/de-encapsulation in networking?  
    什麼是封裝與解封裝（encapsulation / de-encapsulation）？

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
