The main purpose of an Event Loop is to unclog blocking operations and let multiple operations execute in “parallel”.

---

## 比喻：雲端廚房的接單員

你是一個接單員（Event Loop），負責管理所有外送訂單。

**角色對應：**

| 概念 | 雲端廚房比喻 |
|------|------------|
| Event Loop | 接單員（只有一個人） |
| Coroutine | 一張外送訂單 |
| `await` | 「廚房去做，做好通知我」 |
| I/O 等待 | 廚房備餐的時間 |
| 事件觸發 | 廚房按下「備餐完成」按鈕 |

**流程：**

1. 訂單 A 進來 → 丟給廚房，**不等**，繼續接下一張
2. 訂單 B 進來 → 丟給廚房，**不等**，繼續接下一張
3. 廚房通知「A 好了」→ 接單員去處理 A（送出）
4. 廚房通知「B 好了」→ 接單員去處理 B（送出）

**關鍵：**
> 接單員永遠只做一件事，但他**從不乾等廚房**，廚房好了才去拿。

這就是為什麼單執行緒也能同時處理大量 I/O 請求。

---

## Python 實際怎麼實現

Python 透過 `asyncio` 模組提供 Event Loop。

**底層 I/O 通知機制（OS 層）：**

| 系統 | 機制 |
|------|------|
| Linux | `epoll` |
| macOS | `kqueue` |
| Windows | `IOCP` |

Event Loop 把「等待 I/O」的工作交給 OS，具體流程如下：

1. **註冊**：`await` 時，asyncio 用 `epoll_ctl(ADD)` 把 fd 加入 interest list，並掛上 callback（`ep_poll_callback`）
2. **等待**：呼叫 `epoll_wait()`，thread 進入睡眠（`TASK_INTERRUPTIBLE`），CPU 交回 OS
3. **就緒通知**：網卡中斷 → kernel 網路棧處理封包 → 觸發 `ep_poll_callback` → fd 移入 ready list → thread 被喚醒
4. **恢復**：`epoll_wait()` 返回就緒 fd 清單，Event Loop 執行對應 callback，coroutine 重新排入執行佇列

**執行流程：**

```python
import asyncio

async def fetch(name):
    print(f"{name} 開始")
    await asyncio.sleep(1)   # 模擬 I/O，此時 loop 去跑別的
    print(f"{name} 完成")

async def main():
    await asyncio.gather(fetch("A"), fetch("B"))  # 同時跑兩個

asyncio.run(main())  # 啟動 Event Loop
```

輸出：
```
A 開始
B 開始
（等 1 秒）
A 完成
B 完成
```

**關鍵機制：**
- `await` — 暫停當前 coroutine，把控制權還給 Event Loop
- `asyncio.gather()` — 同時排入多個 coroutine
- `asyncio.run()` — 建立 Event Loop 並跑到結束
- Coroutine 底層建立在 generator 機制上，`await` 透過 `__await__()` 協定運作，行為類似 `yield from` 但不完全等價

---

## Event Loop 主迴圈詳細流程

![Event Loop](../image/Build%20Your%20Own%20Event%20Loop%20in%20Python.webp)

```
await → coroutine 暫停，yield 出 Future，控制權回到 event loop

event loop 主迴圈：
  1. 執行 ready queue 裡的 callbacks
  2. 如果 ready queue 為空 → 呼叫 selector.select()
  3. selector.select() 進入阻塞，等待 OS I/O 事件（epoll/kqueue）
     ⚠️ 不是忙碌輪詢（busy polling），而是阻塞等待，不耗 CPU
  4. 當 fd ready，OS 喚醒 event loop 並回傳事件
  5. event loop 找到對應 Future → 呼叫 set_result()
  6. 觸發 Future 的 callback
  7. 將 callback 加入 ready queue
  8. 回到第 1 步，繼續執行
```

| 模式 | 行為 |
|---|---|
| busy polling | 一直問 OS，耗 CPU |
| blocking wait（epoll/kqueue） | 睡著等 OS 喚醒，不耗 CPU ✅ |
| signal/callback（push） | OS 主動呼叫 user space |

> event loop 並不是透過忙碌輪詢來檢查 I/O，而是透過 epoll/kqueue 進行阻塞等待，當 I/O 就緒時由 OS 喚醒，從而高效地處理大量並發連線。

**`await` 那一刻發生什麼：**

```python
result = await some_coroutine()
```

1. `some_coroutine()` 最終 `await` 到某個尚未完成的 `Future`
2. coroutine 暫停，把控制權交回 event loop；event loop 取得並監控這個 `Future`
3. event loop 繼續執行 ready queue 裡的其他工作
4. I/O 完成後，event loop 對 `Future` 呼叫 `set_result()`
5. 觸發 callback → coroutine 重新排入 ready queue → 繼續執行

> `await` 讓 coroutine 暫停並等待一個 Future（或 awaitable）；event loop 監控這個 Future，當它完成時再恢復 coroutine。

---

## fd（file descriptor）是什麼

OS 用一個**整數**來代表任何「可以讀寫的東西」：

| fd | 代表什麼 |
|---|---|
| 0 | stdin（鍵盤輸入） |
| 1 | stdout（螢幕輸出） |
| 2 | stderr（錯誤輸出） |
| 3, 4, 5... | 你開的檔案、socket、pipe... |

在 async 的脈絡裡：

```
建立 TCP 連線 → OS 給你一個 fd（例如 fd=42）
                代表這個 socket 連線

event loop 告訴 OS：「幫我監控 fd 42，它可以讀的時候通知我」

OS：「fd 42 ready 了」→ 喚醒 event loop
```

fd 是 OS 層的「任務 ID」，event loop 用它來對應回 Python 層的 Future 和 coroutine。

---

## OS、Event Loop、Coroutine 各自負責什麼

**OS 只知道 fd，不知道 coroutine 的存在：**

```
OS 知道的：「fd 42 可以讀了」

Event Loop 知道的：「fd 42 對應到 Future X」
                   「Future X 對應到 coroutine A」
```

**完整職責分工：**

| 角色 | 負責 |
|---|---|
| OS | 監控 fd、I/O 完成後喚醒 event loop |
| Event Loop | 管理 fd → Future → coroutine 的對應關係，排程執行 |
| Coroutine | 被 event loop 驅動，自己不會主動執行 |

coroutine 的恢復完全由 event loop 負責，OS 只處理 fd 層級的通知。

---

## Event Loop 自己加入、自己執行

```
初始：
  ready queue：[A, B, C]        ← queue，有序，FIFO
  waiting：    {}                ← dict（fd → coroutine），無序

step 1：取出 A，執行到 await（等 I/O）
  ready queue：[B, C]
  waiting：    {fd_42: A}

step 2：取出 B，執行到 await（等 I/O）
  ready queue：[C]
  waiting：    {fd_42: A, fd_43: B}

step 3：取出 C，跑完，無 await
  ready queue：[]
  waiting：    {fd_42: A, fd_43: B}

step 4：ready queue 空了 → 呼叫 selector.select()，OS 通知 fd 42 ready
        → 查 waiting[fd_42] 找到 A → 移入 ready queue，從 waiting 移除
  ready queue：[A]
  waiting：    {fd_43: B}

step 5：取出 A，從暫停點繼續執行
  ready queue：[]
  waiting：    {fd_43: B}
```

| | Ready Queue | Waiting |
|---|---|---|
| 資料結構 | Queue（有序） | Dict（fd → coroutine） |
| 誰控制順序 | 加入的時間（FIFO） | I/O 完成的時間 |
| Event loop 怎麼用 | 主動取出執行 | 被動查找，收到 OS 通知才動 |

- event loop 是**單執行緒**，同一時間只執行一個 coroutine
- 靠「遇到 `await` 就切換」來模擬並發，不是真的同時執行
- waiting 是「登記表」，不是排隊，誰的 I/O 先完成誰先進 ready queue

**event loop 不主動掃 waiting dict：**

```
❌ 錯誤理解（busy polling）：
   while True:
       for fd in waiting:
           if fd_is_ready(fd):  # 一直問，耗 CPU

✅ 實際行為：
   selector.select()     # 阻塞，什麼都不做，不耗 CPU

   OS：「fd 42 好了」
   event loop：waiting[fd_42]  # 收到通知才查一次，立刻找到對應 coroutine
```

waiting dict 是純粹的對應表，event loop 不會去巡它，只有 OS 通知後才拿 fd 去查一次。

---

## OS 實際上怎麼通知 Event Loop

前面說「OS 通知 event loop」，實際上不是發訊號，而是**喚醒睡著的 thread**。

**第一層：硬體層**
```
網路封包從網卡進來
  → 網卡發出 IRQ（中斷請求）
  → CPU 收到中斷，暫停目前執行的東西
  → 跳去執行 kernel 的中斷處理程序
```
IRQ 是硬體直接插嘴 CPU 的機制，封包一到 CPU 就知道，不需要任何人輪詢。

**第二層：Kernel 層**
```
kernel 中斷處理程序：
  → 把封包從網卡搬進 socket buffer
  → 標記 fd 42 為 ready，加入 epoll ready list
  → 發現有 thread 在睡眠等這個 fd → 喚醒它
```

**第三層：Python 層**
```
thread 被喚醒
  → epoll_wait() 系統呼叫返回
  → 回傳 [(fd_42, EVENT_READ)]
  → event loop 繼續往下執行
```
Python 完全不知道上面發生了什麼，它只看到 `epoll_wait()` 返回了。

**「OS 通知」的真相：**
```
❌ 直覺想像：OS ──傳訊號──→ Python event loop

✅ 實際發生：
   硬體中斷 → kernel 處理 → kernel 喚醒睡眠的 thread
   → thread 自己從 epoll_wait() 醒來繼續跑
```

`epoll_wait()` 讓 thread 進入 `TASK_INTERRUPTIBLE` 狀態——不佔 CPU，等條件滿足由 kernel 叫醒。event loop 等待 I/O 期間，CPU 完全空出來給其他 process 用。

**整條鏈：**
```
封包到達網卡
  → IRQ → kernel 中斷處理
    → socket buffer 填好，fd 42 標記 ready
      → kernel 喚醒 thread
        → epoll_wait() 返回 [(fd_42, EVENT_READ)]
          → event loop 查 waiting dict
            → coroutine A 放進 ready queue
              → 繼續執行
```
