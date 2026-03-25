"""
LEGB 規則教學

Python 查找變數名稱的順序：
L → Local     目前函式的作用域
E → Enclosing 外層函式的作用域（閉包）
G → Global    模組層級
B → Built-in  Python 內建（len、print、range...）
"""


# ============================================================
# Part 1：基本查找順序
# ============================================================

x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)   # Local（L 找到就停）

    inner()
    print(x)       # Enclosing

outer()
print(x)           # Global


# ============================================================
# Part 2：找不到就往外層走
# ============================================================

name = "Global name"

def func():
    # 這裡沒有定義 name，往外找
    print(name)    # Global name（L 沒有 → G 找到）

func()


# ============================================================
# Part 3：Built-in 是最後一層
# ============================================================

print("\n=== Built-in ===")
print(len([1, 2, 3]))   # len 是 B 層的內建函式

# 如果你在 G 層定義了同名的 len，會蓋掉 built-in（不建議這樣做）
def len(x):
    return "我蓋掉了 built-in len"

print(len([1, 2, 3]))   # 我蓋掉了 built-in len

# 刪掉後恢復正常
del len
print(len([1, 2, 3]))   # 3


# ============================================================
# Part 4：global 關鍵字 — 在函式內修改 Global 變數
# ============================================================

print("\n=== global ===")

count = 0

def increment():
    global count       # 宣告要修改的是 Global 的 count
    count += 1

increment()
increment()
print(count)           # 2

# 不加 global 會怎樣？
count = 0

def increment_bad():
    count += 1         # UnboundLocalError！

try:
    increment_bad()
except UnboundLocalError as e:
    print(f"錯誤：{e}")
# Python 看到函式內有對 count 賦值，就認定 count 是 Local 變數
# 但執行 += 時 Local 的 count 還沒被賦值，所以報錯


# ============================================================
# Part 5：nonlocal 關鍵字 — 在閉包內修改 Enclosing 變數
# ============================================================

print("\n=== nonlocal ===")

def make_counter():
    count = 0

    def increment():
        nonlocal count   # 宣告要修改的是 Enclosing 的 count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3


# ============================================================
# Part 6：LEGB 查找失敗 → NameError
# ============================================================

print("\n=== NameError ===")

def func():
    print(undefined_var)   # L、E、G、B 都找不到

try:
    func()
except NameError as e:
    print(f"錯誤：{e}")


# ============================================================
# Part 7：常見陷阱 — 函式內有賦值，整個函式的該變數都視為 Local
# ============================================================

print("\n=== 常見陷阱 ===")

x = "global"

def tricky():
    print(x)   # 想印 global，但下面有 x = ...
    x = "local"

try:
    tricky()
except UnboundLocalError as e:
    print(f"錯誤：{e}")
# Python 在「編譯」函式時，看到 x = "local"，就把整個函式裡的 x 都標記為 Local
# 所以第一行 print(x) 試圖讀取還未賦值的 Local x，報錯
