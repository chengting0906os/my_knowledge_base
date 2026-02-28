# Network Interview Q&A List

1. What is HTTP, and what does it define in a request and response?  
   什麼是 HTTP？它在 request / response 中定義了哪些內容？

2. What are the key differences between HTTP and HTTPS?  
   HTTP 和 HTTPS 的核心差異是什麼？

3. What does TLS add on top of HTTP?  
   TLS 在 HTTP 之上多提供了哪些能力？

4. What is the difference between HTTP/1.1, HTTP/2, and HTTP/3?  
   HTTP/1.1、HTTP/2、HTTP/3 的差異是什麼？

5. Why can HTTP/3 reduce TCP-level head-of-line blocking effects?  
   為什麼 HTTP/3 可以降低 TCP 層 HOL 影響？

6. What is 0-RTT in HTTP/3/QUIC, and what is the replay-risk caveat?  
   HTTP/3/QUIC 的 0-RTT 是什麼？有哪些 replay 風險？

7. What are common HTTP methods, and how do PUT, POST, and PATCH differ?  
   常見 HTTP Method 有哪些？PUT、POST、PATCH 差在哪？

8. What does idempotent mean in HTTP?  
   HTTP 裡的冪等性（idempotent）是什麼意思？

9. What are the differences between status code classes 1xx, 2xx, 3xx, 4xx, and 5xx?  
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
