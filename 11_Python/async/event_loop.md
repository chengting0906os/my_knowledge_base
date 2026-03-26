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
- Coroutine 底層是用 Python **generator**（`yield`）實作，`await` 就是 `yield from` 的語法糖
