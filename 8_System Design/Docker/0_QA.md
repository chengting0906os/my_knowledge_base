# Docker Interview Q&A

---

## Core Concepts

1. What is the difference between a container and a virtual machine?
   Container 和虛擬機器的差異是什麼？
   <details>
   <summary>Answer</summary>

   |           | Container                            | Virtual Machine            |
   | --------- | ------------------------------------ | -------------------------- |
   | Isolation | Process-level (namespaces + cgroups) | Full OS-level (hypervisor) |
   | OS        | Shares host kernel                   | Has its own guest OS       |
   | Startup   | Milliseconds                         | Minutes                    |
   | Size      | MBs                                  | GBs                        |
   | Overhead  | Near-zero                            | Significant (CPU, RAM)     |

   Containers are lighter and faster but share the host kernel, so kernel-level isolation is weaker than a VM.

   Container 更輕量、啟動更快，但與 VM 共享 host kernel，因此 kernel 層級的隔離性較弱。

   </details>

2. What is the difference between an image and a container?
   Image 和 Container 的差異是什麼？
   <details>
   <summary>Answer</summary>
   - **Image**: read-only, layered filesystem snapshot — the blueprint
   - **Container**: a running (or stopped) instance of an image — image + writable layer on top
   - Multiple containers can be started from the same image independently

   ***
   - **Image**：唯讀的分層檔案系統快照，是藍圖
   - **Container**：Image 的執行（或停止）實例，等於 image 加上最上層可寫入的容器層
   - 同一個 image 可以同時啟動多個獨立的 container

   </details>

3. How does Docker's layered filesystem work?
   Docker 的分層檔案系統是如何運作的？
   <details>
   <summary>Answer</summary>
   - Each `RUN`, `COPY`, `ADD` instruction in a Dockerfile creates an immutable layer
   - Layers are stacked and shared across images (Union FS / overlay2)
   - When a container writes to a file from a lower layer, CoW (Copy-on-Write) copies it to the writable container layer first
   - Shared layers are cached → faster builds and less disk usage

   ***
   - Dockerfile 中每個 `RUN`、`COPY`、`ADD` 指令都會建立一個不可變的 layer
   - 各層疊加，並透過 Union FS / overlay2 在不同 image 之間共用
   - Container 要修改下層的檔案時，CoW（Copy-on-Write）會先將該檔案複製到最上層可寫入的容器層再修改
   - 共用的 layer 可被快取，加速 build 並節省磁碟空間

   </details>

4. What is a Docker registry?
   什麼是 Docker Registry？
   <details>
   <summary>Answer</summary>

   A storage and distribution system for Docker images.
   - **Public**: Docker Hub, GitHub Container Registry, Quay.io
   - **Private**: self-hosted with `registry:2` or cloud-managed (ECR, GCR, ACR)
   - `docker pull` fetches from registry; `docker push` uploads to it

   ***

   Docker image 的儲存與分發系統。
   - **公開**：Docker Hub、GitHub Container Registry、Quay.io
   - **私有**：自架 `registry:2` 或使用雲端托管（ECR、GCR、ACR）
   - `docker pull` 從 registry 下載；`docker push` 上傳至 registry

   </details>

5. What are namespaces and cgroups in the context of Docker?
   Namespace 和 cgroup 在 Docker 中扮演什麼角色？
   <details>
   <summary>Answer</summary>
   - **Namespaces** (isolation): each container gets its own view of PID, network, mount, UTS, IPC, user → processes in different containers can't see each other
   - **cgroups** (resource limits): enforce CPU, memory, I/O quotas per container → prevents one container from starving others

   ***
   - **Namespace**（隔離）：每個 container 擁有獨立的 PID、network、mount、UTS、IPC、user 視角 → 不同 container 的程序互相看不見
   - **cgroup**（資源限制）：對每個 container 設定 CPU、記憶體、I/O 配額 → 防止某個 container 吃光所有資源

   </details>

---

## Dockerfile

1. What is the difference between `CMD` and `ENTRYPOINT`?
   `CMD` 和 `ENTRYPOINT` 的差異是什麼？
   <details>
   <summary>Answer</summary>

   |                     | ENTRYPOINT                    | CMD                                   |
   | ------------------- | ----------------------------- | ------------------------------------- |
   | Purpose             | Defines the executable        | Provides default arguments            |
   | Override at runtime | `--entrypoint` flag           | Any extra args at end of `docker run` |
   | Typical use         | Fixed binary (e.g., `python`) | Default flags / subcommand            |

   Combined: `ENTRYPOINT ["python"]` + `CMD ["app.py"]` → runs `python app.py`; user can override to `python debug.py`.

   ***

   |            | ENTRYPOINT                  | CMD                              |
   | ---------- | --------------------------- | -------------------------------- |
   | 用途       | 定義執行的主程式            | 提供預設參數                     |
   | 執行時覆寫 | 用 `--entrypoint` flag      | 在 `docker run` 最後加上參數即可 |
   | 典型用法   | 固定的執行檔（如 `python`） | 預設旗標 / 子命令                |

   合併使用：`ENTRYPOINT ["python"]` + `CMD ["app.py"]` → 執行 `python app.py`；使用者可覆寫為 `python debug.py`。

   </details>

2. What is the difference between `COPY` and `ADD`?
   `COPY` 和 `ADD` 的差異是什麼？
   <details>
   <summary>Answer</summary>
   - **COPY**: plain file/directory copy — simple and predictable
   - **ADD**: superset of COPY — also auto-extracts `.tar` archives and accepts URLs
   - Best practice: always use `COPY` unless you specifically need the extra features of `ADD`

   ***
   - **COPY**：單純複製檔案或目錄，行為簡單可預期
   - **ADD**：COPY 的超集，額外支援自動解壓縮 `.tar` 壓縮檔及接受 URL
   - 最佳實踐：除非明確需要 `ADD` 的額外功能，否則一律用 `COPY`

   </details>

3. What is the difference between `RUN`, `CMD`, and `ENTRYPOINT`?
   `RUN`、`CMD`、`ENTRYPOINT` 各自的用途是什麼？
   <details>
   <summary>Answer</summary>
   - **RUN**: executes at **build time** — installs packages, compiles code; result is baked into a new layer
   - **CMD**: default command to run at **container start** — can be overridden
   - **ENTRYPOINT**: main executable at **container start** — harder to override, intended to be the app itself

   ***
   - **RUN**：在 **build 階段**執行，安裝套件、編譯程式碼，結果寫入新的 layer
   - **CMD**：**container 啟動時**執行的預設指令，可被覆寫
   - **ENTRYPOINT**：**container 啟動時**執行的主程式，較難被覆寫，代表應用程式本體

   </details>

4. What is a multi-stage build and why is it useful?
   什麼是 multi-stage build？有什麼優點？
   <details>
   <summary>Answer</summary>

   Multiple `FROM` statements in one Dockerfile, each a separate stage. You build in one stage (with all build tools) and copy only the final artifact to a minimal runtime stage.

   ```dockerfile
   FROM golang:1.22 AS builder
   COPY . .
   RUN go build -o app

   FROM alpine:3.19
   COPY --from=builder /app /app
   CMD ["/app"]
   ```

   - Eliminates build tools, source code, and intermediate files from the final image
   - Result: much smaller, more secure production image

   ***

   在同一個 Dockerfile 中使用多個 `FROM`，每個代表一個獨立階段。在 build 階段使用完整工具鏈編譯，再將最終產出物複製到最小化的 runtime 階段。
   - 最終 image 不含編譯工具、原始碼與中間產物
   - 結果：image 更小、更安全

   </details>

5. What are best practices for writing a Dockerfile?
   撰寫 Dockerfile 有哪些最佳實踐？
   <details>
   <summary>Answer</summary>
   - Use a minimal base image (e.g., `alpine`, `distroless`)
   - Order layers from least-changed to most-changed to maximize cache reuse (e.g., install dependencies before copying source)
   - Combine `RUN` commands with `&&` to reduce layer count
   - Use multi-stage builds to keep final image small
   - Run as a non-root user (`USER`)
   - Use `.dockerignore` to exclude unnecessary files
   - Pin base image versions for reproducibility

   ***
   - 使用最小化 base image（如 `alpine`、`distroless`）
   - 將最少變動的指令排在前面，最常變動的排在後面，以最大化 cache 命中率（例如先安裝套件再複製原始碼）
   - 用 `&&` 合併 `RUN` 指令，減少 layer 數量
   - 使用 multi-stage build 縮小最終 image
   - 以非 root 使用者執行（`USER`）
   - 使用 `.dockerignore` 排除不必要的檔案
   - 固定 base image 版本以確保可重現性

   </details>

6. Why should you avoid creating too many layers in a Dockerfile?
   為什麼不應該在 Dockerfile 中產生過多 layer？
   <details>
   <summary>Answer</summary>

   每個 `RUN` 都是一個獨立的 layer，且每個 layer 都是**不可變的快照**。
   即使後續的 `RUN` 刪除了前一層的檔案，那些位元組仍然存在於舊 layer 中，最終 image 仍然包含它們。

   **壞寫法（3 個 layer，cache 沒有真正刪除）：**

   ```dockerfile
   FROM ubuntu:22.04
   RUN apt-get update                      # layer 1：下載 package 清單
   RUN apt-get install -y curl             # layer 2：安裝套件
   RUN rm -rf /var/lib/apt/lists/*         # layer 3：試圖清除 cache
   ```

   Layer 1 和 Layer 2 的 `/var/lib/apt/lists/` 內容**仍然存在於 image 中**，只是在 layer 3 被「遮蓋」了。
   Pull image 時這些 byte 還是要傳輸，image 並沒有變小。

   **好寫法（1 個 layer，cache 真正消失）：**

   ```dockerfile
   FROM ubuntu:22.04
   RUN apt-get update && \
       apt-get install -y curl && \
       rm -rf /var/lib/apt/lists/*         # 同一層清除，cache 不寫入任何 layer
   ```

   三個動作在同一個 layer 完成，cache 從未存入任何持久層，image 更小。

   **影響整理：**

   | 問題       | 說明                                        |
   | ---------- | ------------------------------------------- |
   | Image 變大 | 刪除動作只遮蓋舊 layer，不真正釋放空間      |
   | Build 變慢 | layer 越多，每次 push/pull 需傳輸的中繼資料越多 |
   | Cache 失效 | 過細的 layer 拆分讓 cache miss 範圍更廣     |

   ***

   Every `RUN` creates an immutable snapshot. Deleting files in a later `RUN` hides them from the filesystem view but doesn't remove their bytes from the earlier layer — they still bloat the image. Combine related commands in a single `RUN` with `&&` so cleanup happens in the same layer and is never persisted.

   </details>

7. What is `.dockerignore` and why should you use it?
   `.dockerignore` 是什麼？為什麼需要它？
   <details>
   <summary>Answer</summary>

   Similar to `.gitignore` — lists files/dirs to exclude from the build context sent to the Docker daemon.
   - Speeds up builds (smaller context sent over socket)
   - Prevents accidental inclusion of secrets, `.git`, `node_modules`, local config files in the image

   ***

   類似 `.gitignore`，列出不需要傳送給 Docker daemon 的檔案或目錄。
   - 減少 build context 大小，加快 build 速度
   - 防止 secrets、`.git`、`node_modules`、本地設定檔等意外被打包進 image

   </details>

7. What does `EXPOSE` do?
   `EXPOSE` 指令的作用是什麼？
   <details>
   <summary>Answer</summary>

   Documents which port the container's application listens on — it is **metadata only** and does not actually publish the port.
   To publish: `docker run -p 8080:80 myimage` maps host port 8080 → container port 80.

   ***

   只是**文件性質的元資料**，聲明 container 內應用程式監聽的 port，並不會真正發布 port。
   真正發布需用：`docker run -p 8080:80 myimage`，將 host 的 8080 對應到 container 的 80。

   </details>

---

## Networking

1. What are Docker's network drivers?
   Docker 有哪些網路模式？
   <details>
   <summary>Answer</summary>

   | Driver    | Description                                                                                   |
   | --------- | --------------------------------------------------------------------------------------------- |
   | `bridge`  | Default; isolated virtual network on host, containers communicate by name within same network |
   | `host`    | Container shares the host's network stack (no isolation, best performance)                    |
   | `none`    | No network — fully isolated                                                                   |
   | `overlay` | Multi-host networking for Docker Swarm / Kubernetes                                           |
   | `macvlan` | Assigns a MAC address, appears as physical device on the network                              |

   ***

   | Driver    | 說明                                                               |
   | --------- | ------------------------------------------------------------------ |
   | `bridge`  | 預設模式；host 上的隔離虛擬網路，同網路內的 container 可用名稱互通 |
   | `host`    | Container 直接共用 host 的網路堆疊（無隔離，效能最佳）             |
   | `none`    | 無網路，完全隔離                                                   |
   | `overlay` | 跨主機網路，用於 Docker Swarm / Kubernetes                         |
   | `macvlan` | 分配 MAC 位址，container 在網路上看起來像實體裝置                  |

   </details>

2. How do two containers on the same bridge network communicate?
   同一個 bridge network 上的兩個 container 如何互相通訊？
   <details>
   <summary>Answer</summary>

   Docker's embedded DNS resolves container names to IP addresses within a user-defined network.
   - `container_a` can reach `container_b` at `http://container_b:8080` by name
   - This does NOT work on the default `bridge` network (must use IPs or `--link`); always use user-defined networks

   ***

   Docker 內建的 DNS 會在使用者自定義網路中將 container 名稱解析成 IP。
   - `container_a` 可直接用名稱 `http://container_b:8080` 存取 `container_b`
   - 預設的 `bridge` 網路**不支援**名稱解析（須用 IP 或 `--link`）；請一律使用自定義網路

   </details>

3. What is the difference between `-p` and `--network host`?
   `-p` 和 `--network host` 的差異是什麼？
   <details>
   <summary>Answer</summary>
   - `-p 8080:80`: publishes container port 80 to host port 8080 via NAT — container keeps its own network namespace
   - `--network host`: container shares host's network namespace entirely — no NAT, no port mapping, container listens directly on host interface (Linux only; not supported on Mac/Windows Docker Desktop)

   ***
   - `-p 8080:80`：透過 NAT 將 container 的 80 port 發布到 host 的 8080 port，container 保有自己的 network namespace
   - `--network host`：container 完全共用 host 的 network namespace，無 NAT、無 port mapping，直接監聽 host 介面（僅限 Linux，Mac/Windows Docker Desktop 不支援）

   </details>

---

## Volumes & Storage

1. What is the difference between a bind mount and a volume?
   Bind mount 和 volume 的差異是什麼？
   <details>
   <summary>Answer</summary>

   |             | Volume                          | Bind Mount                |
   | ----------- | ------------------------------- | ------------------------- |
   | Managed by  | Docker                          | Host OS                   |
   | Path        | `/var/lib/docker/volumes/…`     | Any host path             |
   | Portability | High (Docker manages lifecycle) | Low (host-specific path)  |
   | Use case    | Production data persistence     | Dev (live code reloading) |

   Volumes are preferred for production because Docker handles backup, migration, and permissions.

   ***

   |          | Volume                      | Bind Mount               |
   | -------- | --------------------------- | ------------------------ |
   | 管理方   | Docker                      | Host OS                  |
   | 路徑     | `/var/lib/docker/volumes/…` | 任意 host 路徑           |
   | 可攜性   | 高（Docker 管理生命週期）   | 低（依賴 host 特定路徑） |
   | 使用場景 | Production 資料持久化       | 開發（即時同步程式碼）   |

   Production 建議用 volume，因為備份、遷移與權限管理都由 Docker 負責。

   </details>

2. What is a tmpfs mount?
   什麼是 tmpfs mount？
   <details>
   <summary>Answer</summary>

   Mounts data into the container's memory (RAM) only — nothing is written to disk. Data is lost when the container stops.
   Use case: sensitive data (credentials, session tokens) that should never touch disk.

   ***

   將資料掛載到 container 的記憶體（RAM）中，不寫入磁碟。Container 停止後資料即消失。
   使用場景：敏感資料（憑證、session token）不應寫入磁碟時。

   </details>

3. How do you persist data in a Docker container?
   如何讓 Docker Container 的資料持久化？
   <details>
   <summary>Answer</summary>

   Three options:
   1. **Named volume**: `docker run -v mydata:/app/data` — Docker manages the volume
   2. **Bind mount**: `docker run -v /host/path:/app/data` — host directory mounted into container
   3. **External storage**: mount NFS, cloud object storage (e.g., S3 via FUSE), or managed DB outside the container

   ***

   三種方式：
   1. **具名 volume**：`docker run -v mydata:/app/data`，由 Docker 管理 volume 生命週期
   2. **Bind mount**：`docker run -v /host/path:/app/data`，直接掛載 host 目錄
   3. **外部儲存**：掛載 NFS、雲端物件儲存（如 S3 via FUSE）或在 container 外使用受管理的資料庫

   </details>

---

## Docker Compose

1. What is Docker Compose and when would you use it?
   什麼是 Docker Compose？什麼情況下使用？
   <details>
   <summary>Answer</summary>

   A tool for defining and running multi-container applications via a `docker-compose.yml` file.
   - Declare services, networks, volumes in one file
   - `docker compose up` starts everything; `docker compose down` tears it down
   - Ideal for local development and simple multi-service setups (app + db + cache)
   - Not designed for production multi-host orchestration (use Kubernetes or Swarm for that)

   ***

   透過 `docker-compose.yml` 定義並執行多 container 應用程式的工具。
   - 在單一檔案中宣告所有 service、network 和 volume
   - `docker compose up` 一鍵啟動；`docker compose down` 一鍵關閉
   - 適合本地開發和簡單的多服務架構（app + db + cache）
   - 不適合跨主機 production 編排（請用 Kubernetes 或 Swarm）

   </details>

2. What is the difference between `docker compose up` and `docker compose start`?
   `docker compose up` 和 `docker compose start` 的差異是什麼？
   <details>
   <summary>Answer</summary>
   - `up`: creates and starts containers (also builds images if needed); recreates changed services
   - `start`: starts **existing** stopped containers — does not create or recreate

   ***
   - `up`：建立並啟動 container（必要時也會 build image），若 service 有變更會重新建立
   - `start`：只啟動**已存在**但停止的 container，不建立也不重新建立

   </details>

3. How do you make one service wait for another to be ready in Docker Compose?
   如何讓一個 service 等待另一個 service 準備好後再啟動？
   <details>
   <summary>Answer</summary>
   - `depends_on` ensures start **order**, but does not wait for the service to be _healthy_
   - Add a `healthcheck` to the dependency, then use `depends_on: condition: service_healthy`

   ```yaml
   depends_on:
     db:
       condition: service_healthy
   ```

   - Alternative: use a wait script (e.g., `wait-for-it.sh`) or retry logic in the app itself

   ***
   - `depends_on` 只保證啟動**順序**，不等待服務真正就緒（healthy）
   - 在相依的 service 加上 `healthcheck`，再用 `depends_on: condition: service_healthy`

   ```yaml
   depends_on:
     db:
       condition: service_healthy
   ```

   - 替代方案：使用 wait script（如 `wait-for-it.sh`）或在應用程式本身加入重試邏輯

   </details>

4. What does `docker compose down -v` do?
   `docker compose down -v` 會做什麼？
   <details>
   <summary>Answer</summary>

   Stops and removes containers, networks, **and named volumes** defined in the Compose file.
   Without `-v`, volumes are preserved (data survives). With `-v`, all data in managed volumes is deleted — useful for a clean reset in dev.

   ***

   停止並移除 container、網路，**以及** Compose 檔案中定義的具名 volume。
   不加 `-v` 時，volume 會保留（資料不消失）；加了 `-v` 後，所有受管理 volume 的資料都會刪除，適合開發時做乾淨的重置。

   </details>

---

## Security

1. What are the security risks of running containers as root?
   以 root 執行 container 有哪些安全風險？
   <details>
   <summary>Answer</summary>
   - If an attacker escapes the container, they get root on the host
   - Container root maps to host UID 0 by default (without user namespaces)
   - Best practice: add `USER nonroot` in Dockerfile; use `--user` flag at runtime
   - Further harden with `--read-only`, `--cap-drop ALL`, `--security-opt no-new-privileges`

   ***
   - 若攻擊者逃脫 container，即可取得 host 的 root 權限
   - 預設情況下（未啟用 user namespace），container 的 root 對應到 host 的 UID 0
   - 最佳實踐：在 Dockerfile 加入 `USER nonroot`；執行時使用 `--user` 旗標
   - 進一步強化：`--read-only`、`--cap-drop ALL`、`--security-opt no-new-privileges`

   </details>

2. What is Docker Content Trust (DCT)?
   什麼是 Docker Content Trust？
   <details>
   <summary>Answer</summary>

   A mechanism to verify the authenticity and integrity of Docker images using cryptographic signatures (Notary/TUF framework).
   Enable with `DOCKER_CONTENT_TRUST=1` — `docker pull` and `push` will only work with signed images.
   Prevents pulling tampered or unofficial images.

   ***

   透過密碼學簽章（Notary/TUF 框架）驗證 Docker image 真實性與完整性的機制。
   設定 `DOCKER_CONTENT_TRUST=1` 後，`docker pull` 和 `push` 只接受已簽署的 image。
   可防止拉取被竄改或非官方的 image。

   </details>

3. How do you avoid storing secrets in a Docker image?
   如何避免將 secrets 存入 Docker image？
   <details>
   <summary>Answer</summary>
   - **Environment variables** at runtime: `docker run -e DB_PASSWORD=...` (not in Dockerfile)
   - **Docker secrets** (Swarm/Compose): mounted as files in `/run/secrets/`
   - **Secret managers**: Vault, AWS Secrets Manager — app fetches at startup
   - **BuildKit secrets**: `RUN --mount=type=secret` for build-time secrets without leaking into layers
   - Never `COPY .env` or hardcode credentials in a Dockerfile

   ***
   - **執行時環境變數**：`docker run -e DB_PASSWORD=...`（不寫在 Dockerfile 裡）
   - **Docker secrets**（Swarm/Compose）：以檔案形式掛載於 `/run/secrets/`
   - **Secret 管理工具**：Vault、AWS Secrets Manager，應用程式啟動時自行取得
   - **BuildKit secrets**：`RUN --mount=type=secret`，build 時使用 secret 且不寫入任何 layer
   - 絕對不要 `COPY .env` 或在 Dockerfile 中寫死憑證

   </details>

---

## Runtime & Debugging

1. How do you inspect a running container?
   如何檢查一個正在執行的 container？
   <details>
   <summary>Answer</summary>
   - `docker logs <container>` — stdout/stderr logs
   - `docker exec -it <container> sh` — open interactive shell inside
   - `docker inspect <container>` — full JSON metadata (IP, mounts, env, etc.)
   - `docker stats` — live CPU, memory, network, I/O usage
   - `docker top <container>` — processes running inside

   ***
   - `docker logs <container>`：查看 stdout/stderr 日誌
   - `docker exec -it <container> sh`：進入 container 開啟互動式 shell
   - `docker inspect <container>`：完整 JSON 元資料（IP、掛載、環境變數等）
   - `docker stats`：即時 CPU、記憶體、網路、I/O 使用狀況
   - `docker top <container>`：查看 container 內正在執行的程序

   </details>

2. How do you reduce Docker image size?
   如何減少 Docker image 的大小？
   <details>
   <summary>Answer</summary>
   - Use minimal base: `alpine`, `distroless`, or `scratch`
   - Multi-stage builds — copy only final artifacts
   - Combine `RUN` steps to avoid intermediate layers
   - Clean up package manager caches in the same `RUN` step: `apt-get clean && rm -rf /var/lib/apt/lists/*`
   - Use `.dockerignore` to exclude build artifacts, docs, tests
   - Remove unused dependencies

   ***
   - 使用最小化 base image：`alpine`、`distroless` 或 `scratch`
   - Multi-stage build，只複製最終產出物
   - 合併 `RUN` 步驟，避免產生多餘的中間 layer
   - 在同一個 `RUN` 步驟清除套件管理快取：`apt-get clean && rm -rf /var/lib/apt/lists/*`
   - 使用 `.dockerignore` 排除 build 產出物、文件、測試檔
   - 移除未使用的相依套件

   </details>

3. What happens when you run `docker run`?
   執行 `docker run` 時，Docker 做了哪些事？
   <details>
   <summary>Answer</summary>
   1. Check if image exists locally; if not, pull from registry
   2. Create a new container layer (writable) on top of the image layers
   3. Allocate network interface, assign IP
   4. Set up namespaces (PID, net, mount, UTS, IPC) and cgroup limits
   5. Execute the `ENTRYPOINT` / `CMD` process as PID 1 inside the container

   ***
   1. 確認 image 是否存在於本地，若無則從 registry 下載
   2. 在 image 各層之上建立新的可寫入容器層
   3. 配置網路介面並分配 IP
   4. 建立 namespace（PID、net、mount、UTS、IPC）並設定 cgroup 資源限制
   5. 在 container 內以 PID 1 執行 `ENTRYPOINT` / `CMD` 所指定的程序

   </details>

4. What is the difference between `docker stop` and `docker kill`?
   `docker stop` 和 `docker kill` 的差異是什麼？
   <details>
   <summary>Answer</summary>
   - `docker stop`: sends `SIGTERM` → waits (default 10s) for graceful shutdown → sends `SIGKILL` if not stopped
   - `docker kill`: sends `SIGKILL` immediately (or a specified signal) — no grace period
   - Prefer `stop` to allow the application to clean up connections and flush data

   ***
   - `docker stop`：先發送 `SIGTERM` → 等待（預設 10 秒）讓程序優雅關閉 → 若仍未停止則發送 `SIGKILL`
   - `docker kill`：立即發送 `SIGKILL`（或指定的訊號），不給緩衝時間
   - 建議用 `stop`，讓應用程式有機會關閉連線、清空緩衝資料

   </details>

5. What is Docker BuildKit and why is it better?
   什麼是 Docker BuildKit？有什麼優點？
   <details>
   <summary>Answer</summary>

   BuildKit is the modern build engine (default since Docker 23.0):
   - **Parallel** execution of independent build stages
   - **Better caching** (cache mounts for package managers: `--mount=type=cache`)
   - **Secret mounts** at build time without leaking into layers
   - **SSH forwarding** for private repos during build
   - Produces smaller images with improved layer diffing

   ***

   BuildKit 是現代化的 build 引擎（Docker 23.0 起預設啟用）：
   - **平行執行**獨立的 build stage
   - **更好的快取**（套件管理快取掛載：`--mount=type=cache`）
   - **Build 階段 secret 掛載**，不洩漏至任何 layer
   - Build 時支援 **SSH forwarding** 存取私有 repo
   - 透過改良的 layer diff 產生更小的 image

   </details>

---

## Orchestration & Production

1. What is the difference between Docker Swarm and Kubernetes?
   Docker Swarm 和 Kubernetes 的差異是什麼？
   <details>
   <summary>Answer</summary>

   |            | Docker Swarm                    | Kubernetes                           |
   | ---------- | ------------------------------- | ------------------------------------ |
   | Setup      | Simple, built into Docker       | Complex, requires separate setup     |
   | Scaling    | Basic                           | Advanced (HPA, VPA)                  |
   | Ecosystem  | Small                           | Huge (Helm, operators, service mesh) |
   | Networking | Built-in overlay                | CNI plugins (Calico, Flannel…)       |
   | Use case   | Small teams, simple deployments | Large-scale, production-grade        |

   ***

   |          | Docker Swarm        | Kubernetes                           |
   | -------- | ------------------- | ------------------------------------ |
   | 設定     | 簡單，內建於 Docker | 複雜，需獨立安裝設定                 |
   | 擴展能力 | 基本                | 進階（HPA、VPA）                     |
   | 生態系   | 小                  | 龐大（Helm、operator、service mesh） |
   | 網路     | 內建 overlay        | CNI 插件（Calico、Flannel…）         |
   | 適用場景 | 小型團隊、簡單部署  | 大規模、production 等級              |

   </details>

2. What is a health check in Docker and why is it important?
   Docker 的 health check 是什麼？為什麼重要？
   <details>
   <summary>Answer</summary>

   A command Docker runs periodically to determine if a container is healthy:

   ```dockerfile
   HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
     CMD curl -f http://localhost/health || exit 1
   ```

   - Container reports `healthy` / `unhealthy` / `starting`
   - Orchestrators (Swarm, Compose with `service_healthy`) use this to route traffic only to healthy instances and restart unhealthy ones

   ***

   Docker 定期執行的指令，用來判斷 container 是否健康：

   ```dockerfile
   HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
     CMD curl -f http://localhost/health || exit 1
   ```

   - Container 會回報 `healthy` / `unhealthy` / `starting` 狀態
   - 編排系統（Swarm、Compose 的 `service_healthy`）依此判斷是否將流量導入，並自動重啟不健康的 container

   </details>

3. How does Docker handle logging in production?
   Docker 在 production 環境如何處理 logging？
   <details>
   <summary>Answer</summary>
   - Default driver: `json-file` — logs written to host disk, can grow unbounded → set `--log-opt max-size` and `max-file`
   - Production alternatives: `fluentd`, `awslogs`, `gelf`, `splunk` log drivers — forward logs to a centralized system
   - Best practice: app writes to stdout/stderr; Docker/orchestrator forwards to log aggregator (ELK, CloudWatch, Datadog)

   ***
   - 預設驅動：`json-file`，日誌寫入 host 磁碟，可能無限增長 → 設定 `--log-opt max-size` 和 `max-file` 限制大小
   - Production 替代方案：`fluentd`、`awslogs`、`gelf`、`splunk` 等日誌驅動，將日誌轉送至集中式系統
   - 最佳實踐：應用程式輸出至 stdout/stderr；由 Docker 或編排系統轉送至日誌聚合平台（ELK、CloudWatch、Datadog）

   </details>
