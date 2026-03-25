"""
@wraps 教學

問題：decorator 會「偷走」被包裝函式的身份
解法：用 functools.wraps 把 metadata 複製回來
"""

from functools import wraps


# ============================================================
# Part 1：不加 @wraps 的問題
# ============================================================

def timer_bad(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@timer_bad
def greet():
    """Say hello to someone."""
    pass


print("=== 不加 @wraps ===")
print(greet.__name__)   # wrapper   ← 應該是 greet
print(greet.__doc__)    # None      ← 文件消失了
print(greet)            # <function timer_bad.<locals>.wrapper ...>


# ============================================================
# Part 2：加上 @wraps 修正
# ============================================================

def timer_good(func):
    @wraps(func)          # 把 func 的 __name__、__doc__ 等複製給 wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@timer_good
def greet():
    """Say hello to someone."""
    pass


print("\n=== 加上 @wraps ===")
print(greet.__name__)   # greet         ✓
print(greet.__doc__)    # Say hello...  ✓
print(greet)            # <function greet ...>  ✓


# ============================================================
# Part 3：@wraps 實際複製了哪些 metadata？
# ============================================================

print("\n=== @wraps 複製的 metadata ===")

def show_metadata(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@show_metadata
def calculate(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y


print(calculate.__name__)       # calculate
print(calculate.__doc__)        # Add two numbers.
print(calculate.__annotations__)# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
print(calculate.__module__)     # __main__
print(calculate.__wrapped__)    # <function calculate ...>  ← 原始函式，@wraps 額外加的


# ============================================================
# Part 4：多層 decorator 疊加時更重要
# ============================================================

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@log
@retry
def fetch_data():
    """Fetch data from API."""
    pass


print("\n=== 多層 decorator ===")
print(fetch_data.__name__)  # fetch_data（若其中一層沒有 @wraps 就會出錯）
fetch_data()                # calling fetch_data


# ============================================================
# Part 5：__wrapped__ 讓你能存取原始函式
# ============================================================

print("\n=== __wrapped__ 存取原始函式 ===")

original = fetch_data.__wrapped__   # 剝掉最外層 @log，拿到 @retry 包的版本
print(original.__name__)            # fetch_data

# 可以一直往下剝
innermost = fetch_data.__wrapped__.__wrapped__
print(innermost.__name__)           # fetch_data（原始函式）
