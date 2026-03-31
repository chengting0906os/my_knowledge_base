# List Comprehensions vs Generator Expressions

## Syntax

```python
# List comprehension — square brackets
squares_list = [x**2 for x in range(10)]

# Generator expression — parentheses
squares_gen = (x**2 for x in range(10))
```

---

## Key Differences

| | List Comprehension | Generator Expression |
|---|---|---|
| Syntax | `[... for ...]` | `(... for ...)` |
| Returns | `list` | `generator` object |
| Evaluation | **Eager** — all at once | **Lazy** — one at a time |
| Memory | O(n) | O(1) |
| Reusable | Yes | No (exhausted after one pass) |
| Speed (first item) | Slower (builds full list) | Faster |
| Speed (all items) | Faster (already in memory) | Slower (compute per item) |

---

## When to use which

**Use list comprehension when:**
- You need to access elements by index
- You need to reuse the result multiple times
- The dataset is small

```python
words = ["hello", "world"]
upper = [w.upper() for w in words]
print(upper[0])   # random access
print(upper)      # reuse
```

**Use generator expression when:**
- You only iterate once
- The dataset is large
- You're passing to a function that accepts an iterable

```python
total = sum(x**2 for x in range(1_000_000))  # no intermediate list

with open("big.log") as f:
    errors = sum(1 for line in f if "ERROR" in line)
```

---

## Nested comprehension

```python
# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
# [1, 2, 3, 4, 5, 6]
```

---

## dict / set comprehension (bonus)

```python
# dict comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# set comprehension
unique = {x % 3 for x in range(10)}
# {0, 1, 2}
```

---

## 中文摘要

- `[...]` → List comprehension：立即求值，建立完整 list，適合小資料或需要重複使用
- `(...)` → Generator expression：惰性求值，逐個產生，適合大資料或只需迭代一次
- 傳入 `sum()`、`max()`、`any()` 等函式時，**優先用 generator expression**，省記憶體
