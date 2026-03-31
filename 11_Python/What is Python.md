# What is Python?

## Single-threaded vs Multi-threaded vs Multi-process

**Is Python single-threaded?**
Not exactly. Python supports multi-threading (`threading`), but due to the **GIL (Global Interpreter Lock)**, only one thread can execute Python bytecode at a time.

| | Description | Best for |
|---|---|---|
| Single-threaded | Default mode, one task at a time | Simple scripts |
| Multi-threaded (`threading`) | GIL prevents true CPU parallelism | I/O-bound (network, file I/O) |
| Multi-process (`multiprocessing`) | Each process has its own GIL, true parallelism | CPU-bound (computation heavy) |
| Async (`asyncio`) | Single-threaded event loop, coroutine switching | High-concurrency I/O-bound |

**GIL impact:**
- CPU-bound multi-threading → can be slower (lock contention overhead)
- I/O-bound multi-threading → effective, GIL is released while waiting for I/O

---

## Strongly Typed vs Weakly Typed / Static vs Dynamic

| | Description |
|---|---|
| **Dynamically typed** | Variable types are determined at runtime, no declaration needed |
| **Strongly typed** | No implicit conversion between incompatible types, `"1" + 1` raises TypeError |

```python
x = 10       # int, type determined at runtime
x = "hello"  # can be reassigned to a different type

"1" + 1      # TypeError: strongly typed, no auto conversion
str(1) + "1" # "11": explicit conversion required
```

Comparison:
- JavaScript → dynamic + **weakly typed** (`"1" + 1 = "11"` auto-converts)
- Java → static + strongly typed (checked at compile time)
- Python → dynamic + **strongly typed**

---

## Other Python Characteristics

**Interpreted**
- Source code → bytecode (`.pyc`) → executed by CPython VM
- No compilation to machine code; faster development, slower execution than C/Java

**Everything is an object**
- Functions, classes, modules are all objects and can be passed as arguments

**Duck Typing**
- "If it walks like a duck and quacks like a duck, it's a duck"
- Type doesn't matter — only behavior does
```python
def process(obj):
    obj.run()  # works for any obj that has a run() method
```

**Memory Management**
- Automatic GC using **reference counting** as the primary mechanism
- Object is freed immediately when reference count hits 0
- Cyclic GC handles circular references

---
---

# Python 是什麼？

## 單線程 vs 多線程 vs 多進程

**Python 是單線程語言嗎？**
不完全是。Python 支援多線程（`threading`），但因為 **GIL（Global Interpreter Lock）** 的存在，同一時間只有一個 thread 可以執行 Python bytecode。

| | 說明 | 適合場景 |
|---|---|---|
| 單線程 | 預設執行模式，一次執行一個任務 | 簡單腳本 |
| 多線程 (`threading`) | 有 GIL，無法真正並行 CPU 運算 | I/O-bound（網路請求、檔案讀寫） |
| 多進程 (`multiprocessing`) | 各自有獨立 GIL，可真正並行 | CPU-bound（計算密集） |
| 非同步 (`asyncio`) | 單線程事件迴圈，協程切換 | 大量 I/O-bound，高並發 |

**GIL 的影響：**
- CPU-bound 多線程 → 效能不增反降（lock 競爭 overhead）
- I/O-bound 多線程 → 有效，因為等待 I/O 時 GIL 會釋放

---

## 強型別 vs 弱型別 / 靜態 vs 動態

| | 說明 |
|---|---|
| **動態型別** | 變數型別在執行時決定，不需宣告 |
| **強型別** | 不會隱式轉換不兼容的型別，`"1" + 1` 會報錯 |

```python
x = 10       # int，執行時才決定型別
x = "hello"  # 可重新賦值為不同型別

"1" + 1      # TypeError：強型別，不自動轉換
str(1) + "1" # "11"：需明確轉換
```

對比：
- JavaScript → 動態 + **弱型別**（`"1" + 1 = "11"` 自動轉換）
- Java → 靜態 + 強型別（編譯時檢查）
- Python → 動態 + **強型別**

---

## 其他 Python 特性

**直譯式（Interpreted）**
- 原始碼 → bytecode（`.pyc`）→ CPython VM 執行
- 不需編譯成機器碼，開發快，執行速度比 C/Java 慢

**一切皆物件（Everything is an object）**
- 函式、類別、模組都是 object，可以作為參數傳遞

**鴨子型別（Duck Typing）**
- 不看型別，只看行為：「如果它走起來像鴨子，叫起來像鴨子，它就是鴨子」
```python
def process(obj):
    obj.run()  # 不管 obj 是什麼型別，只要有 run() 就能執行
```

**記憶體管理**
- 自動 GC，使用**引用計數（reference counting）**為主
- 引用計數歸零時立即釋放；循環引用由 cyclic GC 處理
