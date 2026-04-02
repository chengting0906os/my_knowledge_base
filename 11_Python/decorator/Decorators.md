# Decorators

## 什麼是 decorator？

接收一個 function，回傳一個新 function，在不修改原函式的情況下擴充行為。

```python
@decorator
def foo(): ...

# 等同於
foo = decorator(foo)
```

---

## 基本結構（兩層）

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 前置邏輯
        result = func(*args, **kwargs)
        # 後置邏輯
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}")
```

---

## 帶參數的 decorator（三層）

`@retry(3)` 需要先傳參數，所以多一層：

```python
def retry(n):              # 第一層：接收參數
    def decorator(func):   # 第二層：接收函式
        @wraps(func)
        def wrapper(*args, **kwargs):   # 第三層：實際執行
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
            raise last_exc
        return wrapper
    return decorator

@retry(3)
def unstable(): ...
```

**執行順序：**
```
@retry(3)        → Python 先執行 retry(3)，拿到 decorator
decorator(func)  → 再把 unstable 傳進去，拿到 wrapper
unstable(...)    → 實際呼叫時執行 wrapper
```

### 用 class 實作（另一種寫法）

`retry(max=3)` 回傳 `Wrapper` 這個 class，Python 把 `func` 傳進 `__init__`，
呼叫時執行 `__call__`：

```python
from functools import update_wrapper

def retry(max=1):
    class Wrapper:
        def __init__(self, func):
            self.func = func
            update_wrapper(self, func)   # 等同 @wraps，但 class 裡只能用這個

        def __call__(self, *args, **kwargs):
            retried = 0
            while retried < max:
                try:
                    return self.func(*args, **kwargs)
                except Exception:
                    retried += 1
                    print(f"Failed. Going to try again ({retried})")

    return Wrapper


@retry(max=3)
def get_stock_price():
    raise ValueError


get_stock_price()
```

**執行順序：**
```
@retry(max=3)          → 回傳 Wrapper 這個 class
Wrapper(get_stock_price) → __init__ 被呼叫，self.func = get_stock_price
get_stock_price()      → __call__ 被呼叫，執行 retry 邏輯
```

**vs 閉包寫法的差異：**
- class 寫法：狀態（`retried`）存在 instance 上，結構更清楚
- 閉包寫法：更簡潔，Python 慣用風格
- 兩者功能相同，面試兩種都要會

---

## 常見 decorator 範例

### timer — 計時

```python
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper
```

### logger — 記錄呼叫

```python
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
```

### cache — 簡易 memoize

```python
def cache(func):
    memo = {}
    @wraps(func)
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper

# 標準庫直接用：
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n): ...
```

---

## 多層疊加

```python
@logger
@timer
def fetch():
    ...

# 等同於
fetch = logger(timer(fetch))
# 呼叫順序：logger wrapper → timer wrapper → fetch
```

---

## @wraps 為什麼重要

不加 `@wraps`，decorator 會覆蓋原函式的 metadata：

```python
greet.__name__  # "wrapper"   ← 壞掉了
greet.__doc__   # None        ← 文件消失

# 加上 @wraps(func) 後
greet.__name__  # "greet"     ✓
greet.__doc__   # 原本的文件  ✓
```

詳細見 `wraps.py`。
