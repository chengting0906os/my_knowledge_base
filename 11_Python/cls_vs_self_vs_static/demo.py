"""
cls vs self vs static 教學

三種方法的差異：
- self    → instance method，操作實例本身
- cls     → class method，操作類別本身
- static  → 不需要 self 也不需要 cls，邏輯上屬於這個 class 但獨立運作
"""


# ============================================================
# Part 1：三種方法的基本語法
# ============================================================

class Demo:

    class_var = "我是 class 變數"

    def __init__(self, value):
        self.value = value          # instance 變數

    def instance_method(self):
        """self → 拿到實例，可以存取 instance 變數和 class 變數"""
        print(f"instance_method: self.value = {self.value}")
        print(f"instance_method: class_var  = {self.class_var}")

    @classmethod
    def class_method(cls):
        """cls → 拿到類別本身，可以存取 class 變數，無法存取 instance 變數"""
        print(f"class_method: class_var = {cls.class_var}")
        # print(self.value)  ← 沒有 self，無法存取 instance 變數

    @staticmethod
    def static_method():
        """沒有 self 也沒有 cls，完全獨立"""
        print("static_method: 我不依賴任何 instance 或 class 狀態")


d = Demo("hello")
d.instance_method()   # 用實例呼叫
Demo.class_method()   # 用類別呼叫（也可以用 d.class_method()）
Demo.static_method()  # 用類別呼叫（也可以用 d.static_method()）


# ============================================================
# Part 2：cls 常見用途 — 追蹤 class 層級的狀態
# ============================================================

print("\n=== class 變數 vs instance 變數 ===")

class Counter:
    count = 0              # class 變數，所有實例共用

    def __init__(self):
        Counter.count += 1 # 修改 class 變數

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)  # 3  ← class 變數
print(c1.count)       # 3  ← 找不到 instance 變數，往上找到 class 變數


# ============================================================
# Part 3：self.count += 1 vs Counter.count += 1 的差異
# ============================================================

print("\n=== self.count vs Counter.count ===")

class CounterBad:
    count = 0

    def __init__(self):
        self.count += 1    # 注意：這行會建立 instance 變數，不是修改 class 變數

cb1 = CounterBad()
cb2 = CounterBad()

print(CounterBad.count)  # 0  ← class 變數沒有被修改
print(cb1.count)         # 1  ← cb1 自己的 instance 變數
print(cb2.count)         # 1  ← cb2 自己的 instance 變數

# 為什麼？
# self.count += 1  等同  self.count = self.count + 1
# 右邊 self.count 先讀 class 變數（0），+1 後賦值給 instance 變數
# 從此 cb1.count 是 instance 變數（1），和 class 變數脫鉤


# ============================================================
# Part 4：cls 另一個常見用途 — 工廠方法（alternative constructor）
# ============================================================

print("\n=== classmethod 工廠方法 ===")

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data: dict):
        """從 dict 建立 User，不需要先建立實例"""
        return cls(data["name"], data["age"])

    @classmethod
    def from_string(cls, s: str):
        """從 'name,age' 格式建立"""
        name, age = s.split(",")
        return cls(name, int(age))

    def __repr__(self):
        return f"User({self.name}, {self.age})"


u1 = User.from_dict({"name": "Alice", "age": 30})
u2 = User.from_string("Bob,25")
print(u1)   # User(Alice, 30)
print(u2)   # User(Bob, 25)


# ============================================================
# Part 5：staticmethod 用途 — 工具函式，邏輯上屬於這個 class
# ============================================================

print("\n=== staticmethod ===")

class PasswordValidator:
    MIN_LENGTH = 8

    def __init__(self, password):
        if not self.is_valid(password):   # 可以透過 self 呼叫 staticmethod
            raise ValueError("密碼不符合規則")
        self.password = password

    @staticmethod
    def is_valid(password: str) -> bool:
        """驗證邏輯不需要任何 instance 或 class 狀態"""
        return len(password) >= 8 and any(c.isdigit() for c in password)


print(PasswordValidator.is_valid("abc123"))       # False（太短）
print(PasswordValidator.is_valid("abcdefg1"))     # True
print(PasswordValidator.is_valid("abcdefgh"))     # False（沒有數字）


# ============================================================
# Part 6：三者比較
# ============================================================
#
# | 方法類型        | 第一個參數 | 能存取 instance 變數？ | 能存取 class 變數？ |
# |----------------|-----------|----------------------|------------------|
# | instance method | self      | ✅                   | ✅               |
# | class method    | cls       | ❌                   | ✅               |
# | static method   | 無        | ❌                   | ❌（只能硬寫）     |
#
# 選擇原則：
# - 需要存取或修改 instance 狀態 → instance method（self）
# - 需要存取或修改 class 狀態，或作為工廠方法 → class method（cls）
# - 邏輯上屬於這個 class，但不依賴任何狀態 → static method
