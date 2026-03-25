"""
Lazy Evaluation 教學：用 list vs generator 對比說明

核心概念：
- List comprehension：「現在就把所有結果算出來」存進記憶體（eager）
- Generator：「等你要的時候才算下一個」（lazy）
"""

import sys


# ============================================================
# Part 1：語法差異，一個符號的差別
# ============================================================

# list comprehension：用 []
nums_list = [x * 2 for x in range(10)]
print("list:", nums_list)         # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print("type:", type(nums_list))   # <class 'list'>

# generator expression：用 ()
nums_gen = (x * 2 for x in range(10))
print("\ngenerator:", nums_gen)   # <generator object ...>  ← 還沒算！
print("type:", type(nums_gen))    # <class 'generator'>


# ============================================================
# Part 2：Lazy 的意思 — 不呼叫就不計算
# ============================================================

def slow_compute(x):
    """模擬耗時計算"""
    print(f"  computing {x}...")
    return x * 2


print("\n=== list：建立時就全部算完 ===")
result_list = [slow_compute(x) for x in range(3)]
print("建立完成，還沒使用")
# 輸出：
#   computing 0...
#   computing 1...
#   computing 2...
#   建立完成，還沒使用

print("\n=== generator：建立時完全不算 ===")
result_gen = (slow_compute(x) for x in range(3))
print("建立完成，還沒使用")
# 輸出：
#   建立完成，還沒使用  ← 什麼都沒算

print("\n=== generator：呼叫 next() 才算一個 ===")
print(next(result_gen))   # computing 0...  → 0
print(next(result_gen))   # computing 1...  → 2
print("只拿了兩個，第三個還沒算")


# ============================================================
# Part 3：記憶體差異
# ============================================================

N = 1_000_000

# list：一次把 100 萬個數字存進記憶體
list_size = sys.getsizeof([x for x in range(N)])

# generator：不管 N 多大，只存「目前的狀態」
gen_size = sys.getsizeof(x for x in range(N))

print(f"\n=== 記憶體比較（N={N:,}）===")
print(f"list:      {list_size:>10,} bytes  ({list_size / 1024 / 1024:.1f} MB)")
print(f"generator: {gen_size:>10,} bytes  ({gen_size} bytes，幾乎不佔記憶體)")


# ============================================================
# Part 4：generator 只能走一次
# ============================================================

gen = (x for x in range(3))

print("\n=== 第一次迭代 ===")
print(list(gen))   # [0, 1, 2]

print("=== 第二次迭代（已耗盡）===")
print(list(gen))   # []  ← 空的！generator 耗盡就沒了

# list 可以重複使用
lst = [x for x in range(3)]
print("\n=== list 可以重複使用 ===")
print(list(lst))   # [0, 1, 2]
print(list(lst))   # [0, 1, 2]  ← 還在


# ============================================================
# Part 5：yield — 用函式寫 generator
# ============================================================

def count_up(n):
    """每次 next() 才執行到下一個 yield"""
    print("start")
    for i in range(n):
        print(f"  before yield {i}")
        yield i                        # 暫停，把 i 交出去
        print(f"  after yield {i}")    # 下次 next() 才繼續
    print("done")


print("\n=== yield 執行流程 ===")
gen = count_up(3)
print("generator 建立，什麼都沒跑")

val = next(gen)
print(f"拿到: {val}")
# start
# before yield 0
# 拿到: 0

val = next(gen)
print(f"拿到: {val}")
# after yield 0
# before yield 1
# 拿到: 1


# ============================================================
# Part 6：什麼時候用 generator？
# ============================================================
#
# ✅ 用 generator：
#   - 資料量大，不想一次載入記憶體（讀大檔案、串接 API 分頁）
#   - 只需要迭代一次
#   - pipeline 處理（一步一步 transform，不建中間 list）
#
# ✅ 用 list：
#   - 需要重複使用（多次 iterate）
#   - 需要 indexing（result[3]）
#   - 需要 len()
#   - 資料量小，效能差異不重要

print("\n=== 大檔案讀取的實際應用 ===")

def read_lines_lazy(filepath):
    """不一次把整個檔案載入，一行一行讀"""
    with open(filepath) as f:
        for line in f:
            yield line.strip()

# 對比：
# lines = open(filepath).readlines()  # 整個檔案進記憶體
# lines = read_lines_lazy(filepath)   # 每次只拿一行
