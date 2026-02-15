# Event Loop

![Event Loop 流程圖](./image/event%20loop.png)

## ASCII 圖（Main Thread 包含 Event Loop）

```text
+------------------------------------------------------+
|                   Main Thread                        |
|                                                      |
|  +-----------------------------------------------+   |
|  |                  Event Loop                   |   |
|  |                                               |   |
|  |  [Ready Queue] --> run Task --> await I/O     |---+----> OS I/O Notifier
|  |         ^                         |           |   |
|  |         |                         v           |   |
|  |   re-queue <----- I/O done callback ----------+<--+
|  +-----------------------------------------------+   |
+------------------------------------------------------+
```

## 什麼是 Event Loop

Event loop 是 `asyncio` 用來達成單執行緒並發的核心排程器。  
重點不是同時平行執行多段 Python bytecode，而是遇到 I/O 等待時先切換去跑其他任務，等 I/O 完成再回來續跑。

## Event Loop（直覺版）

在 `asyncio` 裡，幾乎所有事情都圍繞 `event loop` 運作。  
它像指揮家：自己不一定做每件事，但負責安排誰先跑、誰暫停、誰接著跑。

技術上，`event loop` 會維護一批待執行工作（jobs）。有些工作是你直接提交的，有些是 `asyncio` 間接加入的。  
每一輪它會挑一個工作交出控制權讓它執行；當工作暫停（例如遇到 `await`）或完成後，控制權回到 `event loop`，再換下一個工作。  
你可以把這批工作大致想成佇列：工作被加入後，通常會依序被處理（但不保證永遠嚴格 FIFO）。

這個循環會持續進行；當暫時沒有可執行工作時，`event loop` 會休眠等待，不會白白耗 CPU。  
整體效率的前提是所有工作要合作：如果某個工作長時間不讓出控制權，就會讓其他工作飢餓，整個模型就失去意義。

## 三層概念（coroutine / task / event loop）

第一層：`coroutine`（執行 function 的內容）  
第二層：`task`（並發排程單位）  
第三層：`event loop`（排程器；同一時間一個 thread 只能有一個 running event loop）

一個 event loop 可以管理很多個 task。

以下依序介紹：

1. `Coroutine`
   > a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time

- 在 Python 通常由 `async def` 產生。
- 重點是「可暫停、可恢復」，不會一口氣跑到 `return`。
- 當 coroutine 遇到 `await`，會先把控制權交還給 event loop。

2. `Task`

- task 是把 coroutine 包成可被 event loop 排程的執行單位。
- 你可以把 coroutine 想成「工作內容」，task 想成「被排程的工作實例」。
- 一個 event loop 可以同時管理很多個 task，輪流推進它們。

3. `Event Loop`

- event loop 是跑在 thread 裡的 while loop 排程器。
- 它會拿 ready task 來執行；遇到等待（I/O 或 timer）就先暫停該 task，改跑其他 task。
- 當 OS 通知 I/O 完成（或 timer 到期），再把對應 task 放回 ready queue 繼續執行。

## I/O 寫檔範例機制

以寫檔為例，阻塞點通常在「等待 I/O 完成」：

1. 程式把寫檔請求送給作業系統。
2. OS 接手執行實際 I/O。
3. I/O 完成後，OS 通知程式可繼續。

等待通知期間，event loop 可以去執行其他就緒任務。

## OS 事件通知機制

| OS      | Event Notification System    |
| ------- | ---------------------------- |
| Linux   | `epoll`                      |
| Windows | `I/O completion port (IOCP)` |
| macOS   | `kqueue`                     |

## Event Loop 的循環流程

1. Main thread 把 coroutine/task 提交到 Event Loop 的 task queue。
2. Event Loop 取出就緒 task 執行。
3. task 遇到 `await`（例如網路/檔案 I/O）時暫停，控制權交回 Event Loop。
4. Event Loop 把 I/O 交給 OS 的事件通知機制處理。
5. OS 完成 I/O 後通知 Event Loop，Event Loop 把對應 task 重新放回就緒佇列。
6. Event Loop 繼續執行被喚醒的 task，直到所有 task 完成。

## CPython 原始碼重點

`asyncio` 的 event loop 在 CPython 裡，核心就是 `run_forever()` 的 while loop：

來源：<https://github.com/python/cpython/blob/3.12/Lib/asyncio/base_events.py#L627>

```python
def run_forever(self):
    ...
    while True:
        self._run_once()
        if self._stopping:
            break
```

而 `_run_once()` 每輪會做三件事：

1. 計算這輪 `select` timeout。
2. 用 `self._selector.select(timeout)` 等待/取得 I/O 事件。
3. 把 ready callbacks 從 queue 取出並執行。

來源：<https://github.com/python/cpython/blob/3.12/Lib/asyncio/base_events.py#L1910>

## 版本補充

Python 3.7 之後通常用 `asyncio.run()` 啟動程式，會自動建立與管理 event loop。  
因此大多數情境不需要手動操作低階 loop API。

## 簡答

Event Loop 是運行在某個執行緒(通常是 main thread)中的 while loop 排程器。`async def` 定義的函式會產生 coroutine 物件,透過 `asyncio.run()` 或 `create_task()` 包裝成 `Task` 後納入排程。

當 Task 執行到 `await`(特別是 I/O 操作)時會暫停並讓出控制權,Event Loop 將該 I/O 操作註冊到 OS 的事件監聽機制(如 Linux 的 epoll)。當 I/O 就緒時,OS 會主動通知 Event Loop,再將對應的 Task 放回 ready queue 等待執行。

整個過程中,Event Loop 持續從 ready queue 取出可執行的 Task 推進;當沒有就緒任務時會阻塞等待 OS 事件通知,有事件時才喚醒對應任務。因此它是事件驅動的機制,而非 CPU busy polling,這也是非同步 I/O 高效的關鍵原因。

## Reference

- https://docs.python.org/3/howto/a-conceptual-overview-of-asyncio.html
- https://www.pythontutorial.net/python-concurrency/python-event-loop/
- https://jimmy-huang.medium.com/python-asyncio-%E5%8D%94%E7%A8%8B-%E4%BA%8C-e717018bb984
