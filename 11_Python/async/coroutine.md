# Python Async 概念

## Coroutine

Coroutine 是一種可以**主動暫停自己、把控制權讓出去**的函式。

不像一般函式跑完才返回，coroutine 可以在 `await` 處暫停，讓 event loop 去執行其他工作，等 I/O 完成後再從暫停點繼續執行。底層建立在 generator 機制之上，`await` 會呼叫物件的 `__await__()` 取得 iterator，行為類似 `yield from`，但並不完全等價。

這讓單一執行緒能在等待 I/O 期間切換去處理其他任務，實現高效的並發，而不需要開多個 thread。

---

## Coroutine 白話解釋

### 先對比一般函式

```python
def normal_func():
    data = requests.get("https://api.example.com")  # 卡在這等，什麼都不能做
    return data
```

一般函式就像**打電話給客服，然後一直拿著電話等，不能做任何事**，直到對方接起來。

---

### Coroutine 的不同之處

```python
async def coroutine_func():
    data = await aiohttp.get("https://api.example.com")  # 暫停，先去做別的
    return data
```

遇到 `await` 就像**跟客服說「你等下回電給我」，然後掛掉電話去做其他事**，等客服打回來再繼續。

---

### 底層是怎麼運作的

```python
# await 會呼叫物件的 __await__() 取得 iterator
# 底層行為類似 yield from，但不完全等價

async def foo():
    await bar()

# 概念上接近（但不是完全等同）：
def foo():
    yield from bar().__await__()
```

`await` 要求右側物件實作 `__await__()`，回傳一個 iterator；coroutine 本身也是透過 generator 的 `yield` 機制來實現暫停與恢復的。

> ⚠️ 說「await 是 yield from 的語法糖」會被進階面試官追問。安全說法是：**await 建立在 generator 機制之上，行為類似 yield from，但透過 `__await__()` 協定運作。**

---

### Event Loop 的角色

```
Event Loop 就像一個「任務調度員」

① 執行 Task A → 遇到 await（等 I/O）→ 暫停 A
② 切換去執行 Task B → 遇到 await → 暫停 B
③ 切換去執行 Task C → 跑完了
④ I/O 完成通知來了 → 恢復 Task A，繼續跑
```

整個過程**只有一個 thread**，靠「主動讓出控制權」來切換任務。

---

### 和 Thread 的關鍵差異

| | Thread | Coroutine |
|---|---|---|
| 切換時機 | OS 強制切換（搶佔式） | 自己主動讓出（協作式） |
| 切換成本 | 高（context switch） | 極低 |
| 適合場景 | CPU 密集運算 | I/O 密集（網路、資料庫） |
| 競態條件風險 | 有，需要加鎖 | 幾乎沒有（單執行緒） |

---

### 一句話總結

> Coroutine 是「**自願暫停**」的函式，在等 I/O 的空檔把 CPU 讓給其他任務用，用單一 thread 模擬出並發的效果。
> Thread 是「**被迫暫停**」，由 OS 決定什麼時候切換。
