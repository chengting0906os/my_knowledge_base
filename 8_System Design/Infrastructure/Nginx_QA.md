# Nginx Interview Q&A

1. What is Nginx, and what are its main roles?
   Nginx 是什麼？主要扮演哪些角色？
   <details>
   <summary>Answer</summary>

   Nginx 是高效能的 HTTP server，常見角色：

   | 角色 | 說明 |
   |------|------|
   | **Reverse Proxy** | 接收 client 請求，轉發給後端服務，隱藏後端細節 |
   | **Load Balancer** | 把流量分散到多個後端實例 |
   | **Static File Server** | 直接 serve HTML/CSS/JS/image，不經過 app server |
   | **HTTP Cache** | 快取後端回應，減少後端壓力 |
   | **TLS Termination** | 在 Nginx 層處理 HTTPS，後端只跑 HTTP |
   | **API Gateway** | 限流、認證、路由（搭配 Lua / OpenResty） |
   </details>

2. What is the difference between a Reverse Proxy and a Forward Proxy?
   Reverse Proxy 和 Forward Proxy 差在哪？
   <details>
   <summary>Answer</summary>

   | | Forward Proxy | Reverse Proxy |
   |---|---|---|
   | 代理誰 | **Client** | **Server** |
   | Client 是否知道後端 server？ | 知道 | 不知道（只看到 proxy） |
   | 典型用途 | VPN、翻牆、企業內網出口 | 負載均衡、隱藏後端、TLS termination |

   - Forward Proxy：幫 client 出去，server 看到的是 proxy 的 IP
   - Reverse Proxy：幫 server 接進來，client 看到的是 proxy 的 IP
   </details>

3. What load balancing algorithms does Nginx support?
   Nginx 支援哪些負載均衡演算法？
   <details>
   <summary>Answer</summary>

   | 演算法 | 說明 | 適合場景 |
   |--------|------|----------|
   | **Round Robin**（預設） | 依序輪流 | 請求處理時間相近 |
   | **Least Connections** | 轉發到目前連線數最少的 | 請求處理時間不均 |
   | **IP Hash** | 依 client IP hash，同一 IP 永遠打同一後端 | 需要 sticky session |
   | **Weighted** | 為每個後端設定權重 | 機器規格不一致 |

   IP Hash 是解決 session 問題的簡單方式，但更建議用集中式 session（Redis）取代。
   </details>

4. How does Nginx handle concurrency? Why is it more efficient than Apache?
   Nginx 如何處理並發？為什麼比 Apache 更高效？
   <details>
   <summary>Answer</summary>

   - **Nginx**：Event-driven + 非阻塞 I/O（epoll/kqueue），少量執行緒處理大量連線，每個連線不佔一個 thread
   - **Apache**（prefork/worker 模式）：每個連線分配一個 thread 或 process，連線數增加時記憶體與 context switch 成本急速上升

   Nginx 用 `worker_processes`（通常等於 CPU 核心數）+ `worker_connections` 的模型，理論上可處理數萬個並發連線，記憶體消耗很低。
   </details>

5. What is TLS termination, and why do it at Nginx instead of the app server?
   什麼是 TLS Termination？為什麼在 Nginx 做而不是 app server？
   <details>
   <summary>Answer</summary>

   TLS Termination：在 Nginx 層解密 HTTPS，後端服務只接收明文 HTTP。

   **優點：**
   - 後端服務不需要處理 TLS 憑證與加解密，簡化部署
   - 加解密集中在 Nginx，可用硬體加速
   - 後端可以專注業務邏輯，效能更好
   - 內網通訊（Nginx ↔ app server）通常在同一 VPC，明文 HTTP 可接受

   **流程：**
   ```
   Client ──HTTPS──▶ Nginx ──HTTP──▶ App Server
                  (TLS termination)
   ```
   </details>

6. What is the difference between `proxy_pass` and `try_files` in Nginx config?
   `proxy_pass` 和 `try_files` 差在哪？
   <details>
   <summary>Answer</summary>

   - **`proxy_pass`**：把請求轉發給另一個 server（反向代理），適合 API 請求

   ```nginx
   location /api/ {
       proxy_pass http://backend:8000;
   }
   ```

   - **`try_files`**：在本地依序嘗試找檔案，找不到才 fallback，適合 SPA 靜態檔案

   ```nginx
   location / {
       try_files $uri $uri/ /index.html;
   }
   ```
   → 先找實際檔案，找不到就回傳 `index.html`（讓前端 router 處理）
   </details>

7. How does Nginx HTTP caching work?
   Nginx HTTP 快取如何運作？
   <details>
   <summary>Answer</summary>

   Nginx 可以快取後端的回應（`proxy_cache`），下次同樣請求直接回傳快取，不打後端。

   **快取控制由後端回應的 header 決定：**
   - `Cache-Control: max-age=3600` → 快取 1 小時
   - `Cache-Control: no-store` → 不快取
   - `ETag` / `Last-Modified` → 條件式快取驗證（304 Not Modified）

   **Nginx 設定範例：**
   ```nginx
   proxy_cache_path /tmp/cache levels=1:2 keys_zone=my_cache:10m;

   location /api/ {
       proxy_cache my_cache;
       proxy_cache_valid 200 1h;
       proxy_pass http://backend;
   }
   ```

   適合快取：靜態資源、不常變動的 API 回應
   不適合快取：使用者相關資料、即時性高的 API
   </details>

8. How would you configure Nginx for a typical backend deployment (reverse proxy + static files)?
   實務上如何設定 Nginx 同時處理靜態檔案與反向代理後端 API？
   <details>
   <summary>Answer</summary>

   ```nginx
   server {
       listen 443 ssl;
       server_name example.com;

       ssl_certificate     /etc/nginx/ssl/cert.pem;
       ssl_certificate_key /etc/nginx/ssl/key.pem;

       # 靜態檔案
       location / {
           root /var/www/html;
           try_files $uri $uri/ /index.html;
       }

       # API 反向代理
       location /api/ {
           proxy_pass http://backend:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }
   }
   ```

   `proxy_set_header X-Real-IP`：讓後端能拿到 client 真實 IP（否則只看到 Nginx IP）
   </details>

9. How do you implement rate limiting in Nginx?
   如何在 Nginx 實作限流？
   <details>
   <summary>Answer</summary>

   Nginx 用 `limit_req_zone` + `limit_req` 實作 Token Bucket 限流：

   ```nginx
   # 定義限流 zone：以 client IP 為 key，每秒 10 個請求
   limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;

   server {
       location /api/ {
           limit_req zone=api_limit burst=20 nodelay;
           proxy_pass http://backend;
       }
   }
   ```

   - `rate=10r/s`：每秒允許 10 個請求
   - `burst=20`：允許短暫突發最多 20 個請求排隊
   - `nodelay`：burst 內的請求不延遲，直接處理（超出 burst 才拒絕）

   超出限制回傳 `503 Service Unavailable`。
   </details>

10. What is the difference between Nginx and a cloud Load Balancer (e.g., AWS ALB)?
    Nginx 和雲端 Load Balancer（如 AWS ALB）差在哪？
    <details>
    <summary>Answer</summary>

    | | Nginx | AWS ALB |
    |---|---|---|
    | 管理方式 | 自己維護、設定、升級 | 全托管，AWS 負責 HA 與擴展 |
    | 路由能力 | 靈活（正則、header、Lua 自定義） | 基於 path / host / header |
    | TLS 憑證 | 手動管理或 Let's Encrypt | AWS ACM 自動管理 |
    | WAF 整合 | 需自行設定（ModSecurity） | 原生支援 AWS WAF |
    | 成本 | 需要 EC2 instance | 按流量計費，無固定基礎成本 |
    | 適合場景 | 自建機房、需要複雜路由、已有 Nginx 技術棧 | 雲端部署、不想管 infra |

    實務上：ALB 做第一層（對外），Nginx 做 app 層內部的反向代理與靜態檔案服務是常見組合。
    </details>
