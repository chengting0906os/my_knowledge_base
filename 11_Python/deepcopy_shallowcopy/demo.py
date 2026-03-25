"""
Shallow Copy vs Deep Copy 教學

核心問題：複製一個物件時，「內層的物件」要不要也一起複製？
"""

import copy


# ============================================================
# Part 1：直接賦值 — 不是複製，是同一個物件
# ============================================================

original = [1, 2, 3]
alias = original          # 不是複製，兩個名字指向同一個 list

alias.append(99)
print("=== 直接賦值 ===")
print(original)           # [1, 2, 3, 99]  ← 跟著變了
print(alias is original)  # True，同一個物件


# ============================================================
# Part 2：Shallow Copy — 複製外層，內層共用
# ============================================================

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
# 也可以用：
# shallow = original[:]
# shallow = list(original)

print("\n=== Shallow Copy ===")
print(shallow is original)      # False，外層是新的
print(shallow[0] is original[0])# True，內層物件共用同一個參考

original[0].append(99)
print(shallow[0])               # [1, 2, 99]  ← 內層共用，跟著變
print(original[0])              # [1, 2, 99]

original.append([5, 6])
print(shallow)                  # [[1,2,99],[3,4]]  ← 外層獨立，不受影響


# ============================================================
# Part 3：Deep Copy — 遞迴複製所有層
# ============================================================

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

print("\n=== Deep Copy ===")
print(deep is original)         # False
print(deep[0] is original[0])   # False，內層也是新的

original[0].append(99)
print(deep[0])                  # [1, 2]  ← 完全獨立，不受影響
print(original[0])              # [1, 2, 99]


# ============================================================
# Part 4：記憶體示意圖
# ============================================================
#
# original = [ ref_A, ref_B ]
#               ↓       ↓
#            [1,2]    [3,4]
#
# 直接賦值：
#   alias  = [ ref_A, ref_B ]  ← 同一個外層 list
#
# shallow copy：
#   shallow = [ ref_A, ref_B ]  ← 新的外層 list，但 ref_A/ref_B 共用
#
# deep copy：
#   deep    = [ ref_C, ref_D ]  ← 全新的外層 + 全新的內層物件
#               ↓       ↓
#            [1,2]    [3,4]     ← 獨立的副本


# ============================================================
# Part 5：什麼時候各用哪個？
# ============================================================
#
# 直接賦值：你就是要兩個名字指向同一個物件（共享狀態）
#
# shallow copy：
#   - 物件只有一層（flat list、dict of primitives）
#   - 效能考量（deep copy 遞迴較慢）
#
# deep copy：
#   - 物件有巢狀結構（list of list、dict of dict）
#   - 需要完全獨立的副本，不希望任何共用

print("\n=== 只有一層時，shallow 就夠了 ===")
flat = [1, 2, 3, 4]
s = copy.copy(flat)
flat.append(99)
print(s)     # [1, 2, 3, 4]  ← 不受影響，因為 int 是 immutable


# ============================================================
# Part 6：Dictionary 的 shallow vs deep copy
# ============================================================

original = {
    "name": "Alice",
    "scores": [90, 85, 78],       # 內層是 mutable list
    "address": {"city": "Taipei"} # 內層是 mutable dict
}

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print("\n=== Dict Shallow Copy ===")
print(shallow is original)                    # False，外層新的
print(shallow["scores"] is original["scores"])# True，內層共用

original["scores"].append(100)
original["address"]["city"] = "Kaohsiung"
original["name"] = "Bob"                      # str 是 immutable，重新賦值

print(shallow["scores"])            # [90, 85, 78, 100]  ← 跟著變
print(shallow["address"]["city"])   # Kaohsiung           ← 跟著變
print(shallow["name"])              # Alice  ← 不變（str immutable，original 是重新賦值）

print("\n=== Dict Deep Copy ===")
original = {
    "name": "Alice",
    "scores": [90, 85, 78],
    "address": {"city": "Taipei"}
}
deep = copy.deepcopy(original)

original["scores"].append(100)
original["address"]["city"] = "Kaohsiung"

print(deep["scores"])               # [90, 85, 78]  ← 完全獨立
print(deep["address"]["city"])      # Taipei         ← 完全獨立

# dict 的 .copy() 等同 shallow copy
print("\n=== dict.copy() 也是 shallow ===")
original = {"tags": ["python", "django"]}
d = original.copy()
original["tags"].append("flask")
print(d["tags"])    # ['python', 'django', 'flask']  ← 內層共用
