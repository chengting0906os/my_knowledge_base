# Generator 完整入門

---

## 1. 為什麼需要 generator？

先看沒有 generator 的問題：

```python
def get_numbers(n):
    result = []
    for i in range(n):
        result.append(i)
    return result

nums = get_numbers(1_000_000)  # 一次建立 100 萬個數字在記憶體裡
```

如果 n 很大，記憶體就爆了。

**Generator 的做法：每次只算一個，用一個拿一個。**

```python
def get_numbers(n):
    for i in range(n):
        yield i            # 暫停在這，等人來拿

nums = get_numbers(1_000_000)  # 幾乎不占記憶體
```

---

## 2. yield 怎麼運作？

`yield` 和 `return` 的關鍵差別：

| | `return` | `yield` |
|---|---|---|
| 執行後 | 函式結束 | 函式**暫停**，等下次呼叫 |
| 狀態 | 全部清空 | 區域變數**保留** |

```python
def demo():
    print("A")
    yield 1       # 暫停，回傳 1
    print("B")
    yield 2       # 暫停，回傳 2
    print("C")
                  # 函式結束，raise StopIteration

gen = demo()

next(gen)   # 印 "A"，回傳 1，暫停在 yield 1
next(gen)   # 印 "B"，回傳 2，暫停在 yield 2
next(gen)   # 印 "C"，raise StopIteration
```

**重點：** 每次 `next()` 從上次暫停的地方繼續跑。

---

## 3. for 迴圈自動處理 StopIteration

```python
for n in demo():
    print(n)
# A
# 1
# B
# 2
# C
```

`for` 幫你自動呼叫 `next()`，碰到 `StopIteration` 就停止，不用手動處理。

---

## 4. generator 是 iterator

generator 自動實作了 iterator protocol：
- `__iter__()` → 回傳自己
- `__next__()` → 回傳下一個值，沒有就 raise `StopIteration`

所以任何能用 `for` 迴圈的地方都能放 generator。

---

## 5. yield from

`yield from` 用來「把另一個 iterable 的值全部 yield 出去」：

```python
# 等同寫法：
def gen_a():
    for x in [1, 2, 3]:
        yield x

# 用 yield from 簡化：
def gen_b():
    yield from [1, 2, 3]
```

在遞迴 generator 裡很常用（例如 flatten nested list）：

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # 遞迴展平
        else:
            yield item
```

---

## 6. send() — 雙向溝通

一般 `yield` 只能**輸出**值。但 `yield` 其實也能**接收**值，靠 `send()`。

```python
def accumulator():
    total = 0
    while True:
        value = yield total    # 右邊 yield total（輸出）；左邊接收 send() 傳進來的值
        total += value

gen = accumulator()
next(gen)        # 必須先執行到第一個 yield，回傳 0
gen.send(10)     # value = 10，total = 10，yield 10  → 10
gen.send(20)     # value = 20，total = 30，yield 30  → 30
gen.send(5)      # value = 5， total = 35，yield 35  → 35
```

執行流程：

```
next(gen)
  → 跑到 yield total（total=0）
  → 暫停，回傳 0

gen.send(10)
  → 把 10 塞進 yield 的左側，value = 10
  → 繼續跑：total += 10 → total = 10
  → 跑到下一個 yield total
  → 暫停，回傳 10
```

**注意：** 第一次一定要用 `next(gen)` 或 `gen.send(None)`，
不能直接 `gen.send(10)`，因為 generator 還沒跑到第一個 `yield`，沒有地方接收值。

---

## 7. 常見面試考點整理

| 考點 | 關鍵字 |
|---|---|
| lazy evaluation | `yield`，每次算一個 |
| 無限序列 | `while True` + `yield` |
| 遞迴展開 | `yield from` |
| 雙向溝通 | `send()` + `value = yield result` |
| 記憶體效率 | generator O(1) vs list O(n) |
| 只能走一次 | 用完就空了，不能 rewind |
