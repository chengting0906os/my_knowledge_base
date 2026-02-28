# What is OSI Model

## OSI 是什麼

OSI（Open Systems Interconnection）是把網路通訊拆成 7 層的參考模型。  
它的核心價值是把複雜網路問題分層，讓設計、溝通、除錯都有共同語言。

## OSI 七層（由上到下）

| Layer | 名稱         | 主要職責                               | 常見例子                    |
| ----- | ------------ | -------------------------------------- | --------------------------- |
| 7     | Application  | 與應用程式直接互動，定義應用層通訊行為 | HTTP, DNS, SMTP             |
| 6     | Presentation | 資料格式轉換、編碼、加解密、壓縮       | TLS/SSL, JSON, JPEG         |
| 5     | Session      | 建立/維持/結束會話，管理對話狀態       |                             |
| 4     | Transport    | 端到端傳輸、分段、可靠性與流量控制     | TCP, UDP                    |
| 3     | Network      | 邏輯位址與路由選擇                     | IP, ICMP, Router            |
| 2     | Data Link    | 同一網段內傳輸、MAC、frame、錯誤偵測   | Ethernet, Wi-Fi MAC, Switch |
| 1     | Physical     | bits 在實體媒介上的傳送                | Cable, Fiber, Radio         |

## 生活比喻

| Layer | 生活比喻（速記） |
| --- | --- |
| 7 Application | 打開 App 傳訊息（你開始「要做什麼」） |
| 6 Presentation | 翻譯/壓縮/加密（把資料變成對方看得懂） |
| 5 Session | 打電話時接通、維持、掛斷（管理會話） |
| 4 Transport | 快遞分箱與重組（確保資料送達與順序） |
| 3 Network | 地圖規劃路線（找路由與目的地） |
| 2 Data Link | 大樓門牌與住戶編號（同網段定位 MAC） |
| 1 Physical | 網路線、光纖、Wi-Fi 訊號（實際傳 bits） |


## OSI 模型中的通訊如何進行

OSI 的精神是把複雜通訊拆層，讓每層只關心自己的責任，並透過標準介面與上下層溝通。  
因此，應用程式不需要直接理解底層線路或封包細節，也能與遠端系統交換資料。

通訊流程如下：

1. 傳送端 L7（Application）先產生資料。
2. 資料往下經過每一層時，該層會加入自己的控制資訊（header；部分層也可能有 trailer）。
3. 資料一路往下到 L1（Physical），轉為 bit 在實體媒介上傳輸。
4. 接收端從 L1 往上處理，每一層根據該層控制資訊進行解析。
5. 接收端逐層解封裝，最終在 L7 還原為應用程式可用資料。

一句話：傳送端是封裝（top-down），接收端是解封裝（bottom-up）。

## 資料怎麼在各層流動（封裝 / 解封裝）

- 傳送端：資料從 L7 往 L1 走，每層加上自己的控制資訊（header / trailer）。
- 接收端：資料從 L1 往 L7 走，逐層拆掉控制資訊並交給上層。

簡化記法：

- Send = top-down（封裝）
- Receive = bottom-up（解封裝）

## Session Layer（L5）與 Presentation Layer（L6）補充

- L5（Session）重點是「會話管理」：建立、維持、終止通訊會話。
- L6（Presentation）重點是「資料表示」：格式/編碼轉換、加解密、壓縮。
- 在現代 TCP/IP 實作中，L5/L6/L7 常被合併看待；很多能力由應用框架或函式庫承擔。

## OSI vs TCP/IP

TCP/IP 四層模型在實作上更常見：

- TCP/IP Application ≈ OSI L7-L5
- TCP/IP Transport ≈ OSI L4
- TCP/IP Internet ≈ OSI L3
- TCP/IP Network Access (Link) ≈ OSI L2-L1

## Ref

- https://www.cloudflare.com/zh-tw/learning/ddos/glossary/open-systems-interconnection-model-osi/
- https://aws.amazon.com/tw/what-is/osi-model/
- https://realnewbie.com/posts/understanding-osi-7-layer-model-with-everyday-analogies
- https://www.skycloud.com.tw/article/knowledge/osi
