# Mutable vs Immutable Objects

---

## 核心概念

| 類型 | 說明 | 範例 |
|------|------|------|
| **Immutable** | 建立後不能修改內容，修改會建立新物件 | `int`、`float`、`str`、`tuple`、`bool`、`bytes` |
| **Mutable** | 建立後可以直接修改內容，不建立新物件 | `list`、`dict`、`set`、`bytearray`、自訂 class |

---

## Part 1：Immutable — 修改就是建立新物件

```python
x = "hello"
print(id(x))         # e.g. 140234567

x += " world"
print(id(x))         # 不同的 id！建立了新 str 物件

# int 也一樣
a = 1000
print(id(a))
a += 1
print(id(a))         # 不同 id
```

**重點：** `x += ...` 對 immutable 物件來說，是 `x = x + ...`，`x` 指向新物件。

---

## Part 2：Mutable — 原地修改，id 不變

```python
lst = [1, 2, 3]
print(id(lst))       # e.g. 140234999

lst.append(4)
print(id(lst))       # 相同 id！同一個物件被修改

lst += [5]           # list 的 += 是 extend，原地修改
print(id(lst))       # 還是相同 id
```

---

## Part 3：函式傳參 — pass by object reference

Python 既不是 pass by value，也不是 pass by reference，而是 **pass by object reference**（傳的是物件的參考）。

```python
# Immutable：函式內重新賦值，外部不受影響
def modify_int(n):
    n += 1      # n 指向新物件，外部的 x 不變
    print(f"inside: {n}")

x = 10
modify_int(x)
print(f"outside: {x}")   # 10，不變


# Mutable：函式內原地修改，外部跟著變
def modify_list(lst):
    lst.append(99)   # 原地修改，外部的 my_list 跟著變

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)            # [1, 2, 3, 99]


# Mutable：函式內重新賦值，外部不受影響
def reassign_list(lst):
    lst = [100, 200]  # lst 指向新物件，外部的 my_list 不受影響

my_list = [1, 2, 3]
reassign_list(my_list)
print(my_list)            # [1, 2, 3]，不變
```

---

## Part 4：Tuple 是 immutable，但內層可以是 mutable

```python
t = ([1, 2], [3, 4])

# t[0] = [99]   # ❌ TypeError：tuple 本身不可修改
t[0].append(99) # ✅ tuple 儲存的是 list 的參考，list 本身可以修改

print(t)        # ([1, 2, 99], [3, 4])
```

**重點：** tuple 的 immutable 指的是「不能換掉裡面的參考」，不是說裡面的物件不能變。

---

## Part 5：Immutable 為什麼可以當 dict key / set 元素？

dict key 和 set 元素需要是 **hashable**，即：
1. 有 `__hash__` 方法
2. `hash` 值在生命週期內不變
3. 可以用 `==` 比較

Immutable 物件滿足這些條件；mutable 物件（`list`、`dict`、`set`）不行。

```python
d = {}
d[(1, 2)] = "ok"      # ✅ tuple 是 hashable
# d[[1, 2]] = "bad"   # ❌ TypeError: unhashable type: 'list'

s = {1, "hello", (1, 2)}    # ✅
# s = {[1, 2]}               # ❌
```

---

## Part 6：String Interning & Integer Caching

Python 為了效能，會快取部分 immutable 物件：

**Integer Caching：** `-5` 到 `256` 的整數預先建立，`is` 比較為 `True`
```python
a = 256; b = 256
print(a is b)   # True（快取範圍內）

a = 257; b = 257
print(a is b)   # False（超出快取範圍，各自新建）
```

**String Interning：** 符合「identifier 規則」（只含字母、數字、底線）的字串會被 intern
```python
a = "hello"; b = "hello"
print(a is b)         # True（interned）

a = "hello world"; b = "hello world"
print(a is b)         # False（有空格，不保證 interned）
```

---

## 快速記憶

```
Immutable（不可變）→ int、float、str、tuple、bool、bytes
Mutable（可變）    → list、dict、set、bytearray

傳進函式：
  - Immutable → 改了不影響外部（因為重新賦值 = 指向新物件）
  - Mutable   → 原地修改（append/update）會影響外部
               重新賦值（lst = [...]）不影響外部
```
