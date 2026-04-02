# Python Tricky Questions

專門收集 Python 面試中常見的陷阱題與觀念題。

---

## 1. Class Attribute vs Instance Attribute

**Q: 這段程式碼的輸出是什麼？請解釋 Class Attribute 和 Instance Attribute 的差異。**

```python
class C:
    attr1 = 5

    def __init__(self):
        self.attr2 = 4

obj1 = C()
obj2 = C()
C.attr1 = 10
obj1.attr1 = 99

print(obj1.attr1)
print(obj2.attr1)
print(C.attr1)
```

---

## 2. Default Mutable Argument

**Q: 為什麼 Test 2 的輸出不是 `["John"]`？如何修改 `create_array` 讓三個測試都通過？**

```python
def create_array(name, arr=[]):
    arr.append(name)
    return arr

# Test 1
arr = create_array("nancy")
print(arr)

# Test 2
arr = create_array("nancy")
arr = create_array("John")
print(arr)

# Test 3
temp = ["nancy"]
arr = create_array("John", temp)
print(arr)
```

預期輸出：
- Test 1 → `["nancy"]`
- Test 2 → `["John"]`
- Test 3 → `["nancy", "John"]`

---

## 3. Late Binding Closure

**Q: 這段程式碼的輸出是什麼？為什麼不是 `[0, 1, 2]`？如何修正？**

```python
functions = []
for i in range(3):
    functions.append(lambda: i)

print([f() for f in functions])
```

---

## 4. is vs ==

**Q: `is` 和 `==` 有什麼差異？以下三個 print 的輸出分別是什麼？**

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)
```

---

## 5. Integer Caching

**Q: 為什麼兩個 `is` 比較的結果不同？Python 的 Integer Caching 機制是什麼？**

```python
x = 256
y = 256
print(x is y)

x = 257
y = 257
print(x is y)
```

---

## 6. List Multiplication Trap

**Q: 這段程式碼的輸出是什麼？為什麼不是 `[[1, 0, 0], [0, 0, 0], [0, 0, 0]]`？**

```python
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)
```

---

## 7. Global vs Local (UnboundLocalError)

**Q: 執行這段程式碼會發生什麼事？為什麼？如何修正？**

```python
x = 10

def foo():
    print(x)
    x = 20

foo()
```

---

## 8. Mutable Class Attribute

**Q: `d1.items` 的輸出是什麼？為什麼不是 `[1]`？**

```python
class D:
    items = []

    def __init__(self):
        self.items.append(1)

d1 = D()
d2 = D()
print(d1.items)
```

---

## 9. String Interning

**Q: 三個 `is` 比較的結果分別是什麼？Python 的 String Interning 規則是什麼？**

```python
a = "hello"
b = "hello"
print(a is b)

a = "hello world"
b = "hello world"
print(a is b)

a = "hello_world"
b = "hello_world"
print(a is b)
```

---

## 10. Single Element Tuple

**Q: `a` 和 `b` 的型別分別是什麼？如何正確建立只有一個元素的 tuple？**

```python
a = (1)
b = (1,)

print(type(a))
print(type(b))
```

---

## 11. Dict Modification During Iteration

**Q: 執行這段程式碼會發生什麼事？如何安全地在迭代時刪除 dict 元素？**

```python
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    if key == 'b':
        del d[key]

print(d)
```

---

## 12. Finally Block Execution

**Q: `foo()` 的回傳值是什麼？`finally` block 中的 return 有什麼特殊行為？**

```python
def foo():
    try:
        return 1
    finally:
        return 2

print(foo())
```

---

## 13. Multiple Inheritance (MRO)

**Q: `d.foo()` 會印出什麼？請解釋 Python 的 Method Resolution Order (MRO)。**

```python
class A:
    def foo(self):
        print("A")

class B(A):
    def foo(self):
        print("B")

class C(A):
    def foo(self):
        print("C")

class D(B, C):
    pass

d = D()
d.foo()
print(D.__mro__)
```

---

## 14. Unpacking with *

**Q: `a`, `b`, `c` 的值分別是什麼？**

```python
a, *b, c = [1, 2, 3, 4, 5]

print(a)
print(b)
print(c)
```

---

## 15. Walrus Operator Scope

**Q: 兩個 `print(n)` 都會正常執行嗎？Walrus operator 的變數作用域是什麼？**

```python
if (n := len([1, 2, 3])) > 2:
    print(n)

print(n)  # outside if block
```

---

## 16. Short-Circuit Evaluation

**Q: 這段程式碼會印出什麼？`foo()` 會被呼叫嗎？為什麼？**

```python
def foo():
    print("foo called")
    return True

def bar():
    print("bar called")
    return False

result = bar() and foo()
print(result)
```

---

## 17. __new__ vs __init__

**Q: `s1 is s2` 和 `s2.value` 的輸出分別是什麼？請解釋 `__new__` 和 `__init__` 的差異。**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = 0

s1 = Singleton()
s1.value = 5
s2 = Singleton()

print(s1 is s2)
print(s2.value)
```

---

## 18. Decorator Order

**Q: 呼叫 `hello()` 會印出什麼？多個 decorator 的執行順序是什麼？**

```python
def decorator1(func):
    def wrapper():
        print("1 before")
        func()
        print("1 after")
    return wrapper

def decorator2(func):
    def wrapper():
        print("2 before")
        func()
        print("2 after")
    return wrapper

@decorator1
@decorator2
def hello():
    print("hello")

hello()
```

---

## 19. Generator Exhaustion

**Q: 兩個 `list(gen)` 的輸出分別是什麼？為什麼？**

```python
gen = (x for x in range(3))

print(list(gen))
print(list(gen))
```

---

## 20. Generator StopIteration

**Q: 第四個 `next(g)` 會發生什麼事？為什麼？**

```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
```

---

## 21. Tuple Immutability

**Q: 執行這段程式碼會發生什麼事？為什麼？**

```python
a = (1, 2, 3)
a[0] = 10
print(a)
```

---

## 22. Shallow Copy vs Deep Copy

**Q: `shallow[0][0]` 和 `deep[0][0]` 的值分別是什麼？請解釋淺拷貝和深拷貝的差異。**

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99

print(shallow[0][0])
print(deep[0][0])
```


---

## 23. LEGB — Import 與 Global Scope 的綁定時機

> 參考檔案：
> - `11_Python/LEGB/ball.py`
> - `11_Python/LEGB/tennis.py`

**Q: 執行 `tennis.py` 後，四個 print 的輸出分別是什麼？**

---

## 24. Method Overloading

> 參考檔案：`11_Python/OOP/method_overloading.py`

**Q: 執行這段程式碼會發生什麼事？**

```python
class Fighter:
    def attack(self):
        print("punch")

    def attack(self, weapon):
        print(f"attack with {weapon}")


f = Fighter()
f.attack()
f.attack("sword")
```

---

## 25. `__str__` vs `__repr__`

> 參考檔案：`11_Python/OOP/str_vs_repr.py`

**Q: 四個 print 的輸出分別是什麼？`__str__` 和 `__repr__` 各在什麼時候被呼叫？**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"


p = Point(1, 2)
print(p)
print(repr(p))
print(f"{p}")
print([p])
```

---

## 26. `@property` Without Setter

> 參考檔案：`11_Python/OOP/property_no_setter.py`

**Q: 執行這段程式碼會發生什麼事？`@property` 和一般 attribute 有什麼差異？**

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2


c = Circle(5)
print(c.radius)
print(c.area)
c.radius = 10
```

---

## 27. `__eq__` Kills `__hash__`

> 參考檔案：`11_Python/OOP/eq_hash.py`

**Q: `print(a == b)` 和 `print(hash(a))` 的輸出是什麼？`{a, b}` 那行會發生什麼事？為什麼定義 `__eq__` 會影響 hashability？**

```python
class Card:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


a = Card(1)
b = Card(1)

print(a == b)
print(hash(a))
my_set = {a, b}
```

---

## 28. `isinstance` vs `type`

> 參考檔案：`11_Python/OOP/isinstance_vs_type.py`

**Q: 四個 print 的輸出分別是什麼？`isinstance` 和 `type ==` 有什麼差異？**

```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(type(d) == Animal)
print(type(d) == Dog)
print(isinstance(d, Animal))
print(isinstance(d, Dog))
```