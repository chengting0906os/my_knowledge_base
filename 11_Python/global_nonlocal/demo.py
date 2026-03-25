"""
global vs nonlocal 教學

核心概念：
- global   → 在函式內宣告「我要修改的是 Global 層的變數」
- nonlocal → 在巢狀函式內宣告「我要修改的是 Enclosing 層的變數」
"""


# ============================================================
# Part 1：為什麼需要 global？
# ============================================================

count = 0

def increment_bad():
    count += 1    # UnboundLocalError！Python 看到賦值，把 count 標記為 Local

try:
    increment_bad()
except UnboundLocalError as e:
    print(f"錯誤：{e}")
# Python 在「編譯」函式時，看到 count += 1（等同 count = count + 1）
# 就把整個函式的 count 標記為 Local
# 執行時讀取 Local count，但它還沒賦值 → 報錯


# ============================================================
# Part 2：global — 正確修改全域變數
# ============================================================

print("\n=== global ===")

count = 0

def increment():
    global count    # 明確宣告：我要操作 Global 的 count
    count += 1

increment()
increment()
increment()
print(count)        # 3


# ============================================================
# Part 3：global 可以「建立」全域變數
# ============================================================

print("\n=== global 建立新變數 ===")

def create_global():
    global new_var
    new_var = 42    # 函式執行後，new_var 會出現在全域

create_global()
print(new_var)      # 42（函式外也能存取）


# ============================================================
# Part 4：為什麼需要 nonlocal？
# ============================================================

print("\n=== nonlocal 問題 ===")

def make_counter():
    count = 0

    def increment():
        count += 1    # UnboundLocalError！same 原因，count 被標記為 Local

    try:
        increment()
    except UnboundLocalError as e:
        print(f"錯誤：{e}")

make_counter()


# ============================================================
# Part 5：nonlocal — 正確修改 Enclosing 變數
# ============================================================

print("\n=== nonlocal ===")

def outer():
    x = 5

    def inner():
        nonlocal x    # 明確宣告：我要操作 Enclosing 的 x
        x += 1
        return x

    return inner()

print(outer())        # 6


# ============================================================
# Part 6：nonlocal 典型用法 — 閉包計數器
# ============================================================

print("\n=== 閉包計數器 ===")

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment    # 回傳函式本身（不是呼叫它）

counter = make_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3
# 每個 counter 有自己獨立的 count，不互相干擾

counter2 = make_counter()
print(counter2())  # 1  ← 從頭開始，與 counter 無關


# ============================================================
# Part 7：nonlocal 無法用在全域變數
# ============================================================

# x = 5
#
# def func():
#     nonlocal x  # ❌ SyntaxError: no binding for nonlocal 'x' found
#     x += 1
#
# nonlocal 只能往「Enclosing 函式」找，不能跨到 Global 層
# 要修改全域變數，必須用 global


# ============================================================
# Part 8：global vs nonlocal 對比
# ============================================================
#
# | 關鍵字   | 目標層級     | 使用情境                     |
# |---------|------------|----------------------------|
# | global  | Global (G)  | 函式內修改模組層級變數           |
# | nonlocal| Enclosing (E)| 巢狀函式內修改外層函式的變數    |
#
# 選擇原則：
# - 需要修改模組層級的變數 → global
# - 需要在閉包內修改外層函式的變數 → nonlocal
# - 兩者都不建議濫用，優先考慮用回傳值或 class 封裝狀態
