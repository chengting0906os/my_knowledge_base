## 中文版

### 結論（Bottom Line）
沒有萬用冠軍，只有適合你場景的工具。

- **REST（資源導向）**
  - 核心是對資源做操作（例如 `GET /users/1`、`POST /orders`）。
  - 穩定、成熟、易除錯，HTTP 快取與 CDN 友善。
  - 不確定怎麼選時，通常先從 REST 開始。

- **GraphQL（欄位導向）**
  - 核心是前端可以指定要哪些欄位，避免 over-fetch / under-fetch。
  - 適合前端頁面資料組合複雜、需求變動快的場景。
  - 代價是後端複雜度提高（resolver、N+1、查詢成本控制）。
  - REST 也可能有 N+1；但 GraphQL 因為是欄位逐層執行 resolver，且 client 可自由要求巢狀資料，常變成先查清單 1 次、再對每筆資料各查 1 次（1+N），所以更容易出現，通常要用 DataLoader 或批次查詢解決。

- **gRPC（RPC / 契約導向）**
  - 核心是先用 `.proto` 定義服務與欄位（schema），再由雙方產生 client/server 程式碼。
  - 資料會用 Protobuf 序列化成二進位傳輸（通常跑在 HTTP/2），強型別且效能佳。
  - 對外部公開 API 或瀏覽器直連場景通常不如 REST/GraphQL 直覺。

## English Version

### Bottom Line
There is no universal winner, only the right tool for your specific context.

- **REST (Resource-oriented)**
  - Operate on resources (e.g., `GET /users/1`, `POST /orders`).
  - Stable, mature, and easy to debug; friendly to HTTP caching and CDNs.
  - If you are unsure, REST is usually the safest starting point.

- **GraphQL (Field-oriented)**
  - Clients request exactly the fields they need, reducing over-fetch/under-fetch.
  - Great for frontend-heavy products with complex data composition and fast-changing requirements.
  - Trade-off: higher backend complexity (resolvers, N+1 issues, query cost control).
  - REST can also suffer from N+1, but GraphQL is more prone to it because resolvers run per field and clients can request nested shapes, often leading to 1 list query plus N child queries (1+N); DataLoader/batched queries are common mitigations.

- **gRPC (RPC / Contract-oriented)**
  - Define Proto contracts first, then enable efficient service-to-service calls.
  - Strong typing + binary protocol + high performance, ideal for internal microservice communication.
  - Usually less intuitive than REST/GraphQL for public APIs or direct browser clients.
