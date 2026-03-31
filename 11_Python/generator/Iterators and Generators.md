# Iterators and Generators

## Iterator

An object that implements the **iterator protocol**:
- `__iter__()` → returns itself
- `__next__()` → returns the next value, raises `StopIteration` when exhausted

```python
nums = [1, 2, 3]
it = iter(nums)   # calls nums.__iter__()
next(it)          # 1
next(it)          # 2
next(it)          # 3
next(it)          # StopIteration
```

Custom iterator:
```python
class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        self.current += 1
        return self.current

for n in Counter(3):
    print(n)  # 1 2 3
```

---

## Generator

A function that uses `yield` to produce values **lazily** — values are generated one at a time, only when requested.

```python
def count_up(stop):
    current = 1
    while current <= stop:
        yield current
        current += 1

gen = count_up(3)
next(gen)  # 1
next(gen)  # 2
next(gen)  # 3
next(gen)  # StopIteration
```

A generator function automatically implements `__iter__` and `__next__` — no boilerplate needed.

---

## yield vs return

| | `return` | `yield` |
|---|---|---|
| Exits function | Yes, permanently | Suspends and resumes |
| Returns | One value | One value per call |
| State preserved | No | Yes (local variables kept) |
| Type | regular value | generator object |

---

## Why use generators?

**Memory efficient** — values are produced on demand, not stored all at once.

```python
# List: creates all 1M numbers in memory at once
nums = [x * 2 for x in range(1_000_000)]

# Generator: computes one at a time
nums = (x * 2 for x in range(1_000_000))
```

**Use cases:**
- Reading large files line by line
- Infinite sequences (e.g., Fibonacci)
- Pipelines / data streaming

---

## Infinite generator example

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(8):
    print(next(gen))  # 0 1 1 2 3 5 8 13
```

---

## Complexity

| | List | Generator |
|---|---|---|
| Memory | O(n) | O(1) |
| Access | Random (index) | Sequential only |
| Reusable | Yes | No (exhausted after one pass) |

---

## 中文摘要

- **Iterator**：實作 `__iter__` 和 `__next__` 的物件，手動控制取值
- **Generator**：用 `yield` 的函式，自動成為 iterator，狀態在每次 `yield` 後暫停保留
- **優點**：Lazy evaluation，記憶體效率高（O(1) vs O(n)）
- **缺點**：只能順序讀取，用完即廢（不可重複迭代）
