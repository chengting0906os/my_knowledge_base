# Python Interview Q&A

---

1. Python 的 GIL 是什麼？它對多執行緒有什麼影響？
   <details>
   <summary>Answer</summary>

   **GIL（Global Interpreter Lock）** 是 CPython 的一把全域鎖，確保同一時間只有一個 thread 在執行 Python bytecode。

   **影響：**
   - CPU-bound 任務（計算密集）：多執行緒無法真正並行，GIL 輪流切換，效能甚至比單執行緒差
   - I/O-bound 任務（等待網路/檔案）：thread 在等待 I/O 時會釋放 GIL，其他 thread 可以執行，多執行緒仍有效

   **解法：**
   - CPU-bound → 用 `multiprocessing`（每個 process 有自己的 GIL）
   - I/O-bound → 用 `threading` 或 `asyncio`
   - 高效能計算 → 用 NumPy（底層 C extension，運算期間不持有 GIL）

   </details>

---

2. Python 的垃圾回收機制（GC）是怎麼運作的？
   <details>
   <summary>Answer</summary>

   Python 使用兩種機制：

   **1. Reference Counting（主要機制）**
   - 每個物件都有一個 `ob_refcnt` 計數器
   - 每增加一個引用 +1，每減少一個引用 -1
   - 計數歸零時，立即釋放記憶體
   - 缺點：無法處理**循環引用**（A → B → A，兩者 refcnt 都不為 0）

   **2. Cyclic Garbage Collector（補充機制）**
   - 專門處理 Reference Counting 無法回收的**循環引用**
   - 分成三個 generation（0、1、2），新物件在 generation 0
   - 每次 GC 掃描時，從 generation 0 開始，存活夠久的物件晉升到下一代
   - 可用 `gc` 模組手動控制：`gc.collect()`、`gc.disable()`

   ```python
   import gc

   class Node:
       pass

   a = Node()
   b = Node()
   a.ref = b
   b.ref = a   # 循環引用

   del a
   del b
   # refcnt 不為 0，但 gc 會偵測並回收
   gc.collect()
   ```

   **記憶口訣：** Reference Counting 是主力，Cyclic GC 是補丁（專解循環引用）。

   </details>

---

3. `__del__` 方法什麼時候被呼叫？有什麼注意事項？
   <details>
   <summary>Answer</summary>

   `__del__` 是 Python 的 finalizer，在物件被 GC 回收時呼叫。

   **注意事項：**
   - 不保證何時被呼叫（reference counting 時立即觸發；循環引用時由 GC 決定）
   - 循環引用中有 `__del__` 的物件，Python 3.4 以前無法回收（3.4+ 已修復）
   - 不要在 `__del__` 裡做重要的資源釋放邏輯，應改用 **context manager（`with` / `__exit__`）**

   ```python
   class MyResource:
       def __enter__(self):
           return self

       def __exit__(self, *args):
           self.close()   # 保證執行
   ```

   </details>

---

4. `*args` 和 `**kwargs` 的用途是什麼？
   <details>
   <summary>Answer</summary>

   - `*args`：收集所有**位置參數**，打包成 `tuple`
   - `**kwargs`：收集所有**關鍵字參數**，打包成 `dict`

   ```python
   def func(*args, **kwargs):
       print(args)    # (1, 2, 3)
       print(kwargs)  # {'a': 4, 'b': 5}

   func(1, 2, 3, a=4, b=5)
   ```

   **解包用法：**
   ```python
   def add(x, y, z):
       return x + y + z

   nums = [1, 2, 3]
   add(*nums)          # 等同 add(1, 2, 3)

   params = {'x': 1, 'y': 2, 'z': 3}
   add(**params)       # 等同 add(x=1, y=2, z=3)
   ```

   </details>

---

5. decorator 是什麼？請用程式碼說明。
   <details>
   <summary>Answer</summary>

   Decorator 是一個接收函式、回傳函式的 callable，用來在不修改原函式的情況下擴充行為。

   ```python
   from functools import wraps

   def logger(func):
       @wraps(func)
       def wrapper(*args, **kwargs):
           print(f"呼叫 {func.__name__}")
           result = func(*args, **kwargs)
           print(f"結束 {func.__name__}")
           return result
       return wrapper

   @logger
   def greet(name):
       print(f"Hello, {name}")

   greet("Alice")
   # 呼叫 greet
   # Hello, Alice
   # 結束 greet
   ```

   `@wraps(func)` 保留原函式的 `__name__`、`__doc__` 等 metadata，避免 debug 時找不到原始函式名稱。

   </details>

---

6. Python 的 LEGB 規則是什麼？
   <details>
   <summary>Answer</summary>

   Python 查找變數名稱的順序：

   | 層級 | 說明 |
   |------|------|
   | **L** Local | 目前函式內 |
   | **E** Enclosing | 外層函式（閉包）|
   | **G** Global | 模組層級 |
   | **B** Built-in | Python 內建（`len`、`print`...）|

   找到就停，找不到拋 `NameError`。

   **常見陷阱：** 函式內只要有對變數的**賦值**，Python 編譯時就把整個函式的該變數標為 Local，讀取時若還未賦值 → `UnboundLocalError`。

   修正方式：`global` 修改 Global 變數，`nonlocal` 修改 Enclosing 變數。

   </details>

---

7. `is` 和 `==` 的差異？
   <details>
   <summary>Answer</summary>

   - `==`：比較**值**是否相等（呼叫 `__eq__`）
   - `is`：比較**記憶體位址**是否相同（同一個物件）

   ```python
   a = [1, 2, 3]
   b = [1, 2, 3]

   print(a == b)   # True（值相同）
   print(a is b)   # False（不同物件）

   c = a
   print(a is c)   # True（同一個物件）
   ```

   **注意：** Python 有 Integer Caching（-5 ~ 256）和 String Interning，小整數和簡單字串的 `is` 可能為 `True`，但這是實作細節，不應依賴。

   </details>

---

8. shallow copy 和 deep copy 的差異？
   <details>
   <summary>Answer</summary>

   - **直接賦值**：兩個名字指向同一個物件
   - **Shallow copy**：複製外層容器，內層物件仍共用同一份參考
   - **Deep copy**：遞迴複製所有層，完全獨立

   ```python
   import copy

   original = [[1, 2], [3, 4]]
   shallow = copy.copy(original)
   deep = copy.deepcopy(original)

   original[0].append(99)

   print(shallow[0])   # [1, 2, 99]  ← 內層共用，跟著變
   print(deep[0])      # [1, 2]      ← 完全獨立
   ```

   `list[:]`、`list(original)`、`dict.copy()` 都是 shallow copy。

   </details>

---

9. generator 和 list comprehension 的差異？什麼時候用 generator？
   <details>
   <summary>Answer</summary>

   - **List comprehension** `[...]`：立即計算所有結果，存進記憶體（eager）
   - **Generator expression** `(...)`：lazy，每次 `next()` 才算下一個值

   ```python
   import sys

   lst = [x for x in range(1_000_000)]
   gen = (x for x in range(1_000_000))

   print(sys.getsizeof(lst))   # ~8 MB
   print(sys.getsizeof(gen))   # ~200 bytes
   ```

   **用 generator 的時機：**
   - 資料量大，不想一次載入記憶體
   - 只需迭代一次
   - pipeline 處理（避免建立中間 list）

   **注意：** generator 只能走一次，耗盡後 `list(gen)` 回傳 `[]`。

   </details>

---

10. `classmethod`、`staticmethod`、instance method 的差異？
    <details>
    <summary>Answer</summary>

    | 方法類型 | 第一個參數 | 能存取 instance？ | 能存取 class？ |
    |---------|-----------|-----------------|--------------|
    | instance method | `self` | ✅ | ✅ |
    | class method | `cls` | ❌ | ✅ |
    | static method | 無 | ❌ | ❌ |

    - **instance method**：操作實例狀態，最常用
    - **classmethod**：操作 class 狀態，或作為 factory method（alternative constructor）
    - **staticmethod**：邏輯上屬於這個 class，但不依賴任何狀態（純工具函式）

    ```python
    class User:
        @classmethod
        def from_dict(cls, data):      # factory method
            return cls(data["name"], data["age"])

        @staticmethod
        def is_valid_email(email):     # 工具函式
            return "@" in email
    ```

    </details>

---

11. `__new__` 和 `__init__` 的差異？
    <details>
    <summary>Answer</summary>

    - `__new__`：負責**建立**物件（allocate memory），回傳新實例，是 class method
    - `__init__`：負責**初始化**物件（設定屬性），不回傳值，`self` 已是建立好的實例

    執行順序：`__new__` → `__init__`

    **常見用途：** Singleton pattern

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

    print(s1 is s2)    # True（同一個物件）
    print(s2.value)    # 0（__init__ 每次都跑，value 被重設！）
    ```

    </details>

---

12. `__repr__` 和 `__str__` 的差異？
    <details>
    <summary>Answer</summary>

    - `__str__`：給**人**看的，`print()` 和 `str()` 呼叫，強調可讀性
    - `__repr__`：給**開發者/除錯**用，`repr()` 呼叫，強調明確性，理想上能重建物件

    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"          # 人看的

        def __repr__(self):
            return f"Point({self.x}, {self.y})"     # 開發者看的

    p = Point(1, 2)
    print(str(p))    # (1, 2)
    print(repr(p))   # Point(1, 2)
    ```

    若只定義 `__repr__`，`str()` 也會 fallback 到它。

    </details>

---

13. Python 的 `with` 語句和 context manager 是什麼？
    <details>
    <summary>Answer</summary>

    `with` 確保資源在使用完畢後一定會被釋放，即使發生例外也是。

    實作 context manager 需要 `__enter__` 和 `__exit__`：

    ```python
    class ManagedFile:
        def __init__(self, path):
            self.path = path

        def __enter__(self):
            self.file = open(self.path)
            return self.file

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.file.close()
            return False   # 不吞例外

    with ManagedFile("data.txt") as f:
        data = f.read()
    ```

    也可以用 `@contextmanager` decorator 簡化：

    ```python
    from contextlib import contextmanager

    @contextmanager
    def managed_file(path):
        f = open(path)
        try:
            yield f
        finally:
            f.close()
    ```

    </details>

---

14. `list`、`tuple`、`set`、`dict` 的時間複雜度比較？
    <details>
    <summary>Answer</summary>

    | 操作 | list | tuple | set | dict |
    |------|------|-------|-----|------|
    | 查找（by value） | O(n) | O(n) | O(1) | - |
    | 查找（by key/index） | O(1) | O(1) | - | O(1) |
    | 插入 | O(1) amortized | - | O(1) | O(1) |
    | 刪除 | O(n) | - | O(1) | O(1) |
    | `in` 運算子 | O(n) | O(n) | O(1) | O(1)（找 key）|

    `set` 和 `dict` 底層是 hash table，`in` 是 O(1)。
    需要頻繁查找存在性 → 用 `set`，不要用 `list`。

    </details>

---

15. `asyncio` 的 `async/await` 是什麼？和 `threading` 有什麼差異？
    <details>
    <summary>Answer</summary>

    - **threading**：OS-level thread，GIL 限制 CPU-bound，適合 I/O-bound
    - **asyncio**：單執行緒的事件迴圈，cooperative multitasking，`await` 主動讓出控制權

    ```python
    import asyncio

    async def fetch(name, delay):
        print(f"{name} 開始")
        await asyncio.sleep(delay)   # 讓出控制權
        print(f"{name} 完成")

    async def main():
        await asyncio.gather(
            fetch("A", 2),
            fetch("B", 1),
        )
        # B 先完成，總耗時 2 秒（非 3 秒）

    asyncio.run(main())
    ```

    | | threading | asyncio |
    |--|-----------|---------|
    | 切換時機 | OS 決定（preemptive）| 程式主動 `await`（cooperative）|
    | 適用 | I/O-bound | I/O-bound（更輕量）|
    | race condition | 需要 Lock | 單執行緒，較少競爭問題 |

    </details>

---

16. Mutable 和 Immutable 物件各有哪些？兩者在函式傳參時行為有何不同？
    <details>
    <summary>Answer</summary>

    | 類型 | 範例 |
    |------|------|
    | **Immutable** | `int`、`float`、`str`、`tuple`、`bool`、`bytes` |
    | **Mutable** | `list`、`dict`、`set`、`bytearray`、自訂 class |

    Python 傳參是 **pass by object reference**：傳的是物件的參考，不是值的拷貝。

    ```python
    # Immutable：函式內重新賦值，外部不受影響
    def modify(n):
        n += 1      # 指向新物件，外部 x 不變

    x = 10
    modify(x)
    print(x)        # 10

    # Mutable：原地修改，外部跟著變
    def modify(lst):
        lst.append(99)

    my_list = [1, 2, 3]
    modify(my_list)
    print(my_list)  # [1, 2, 3, 99]
    ```

    **記憶點：** mutable 物件若在函式內做**重新賦值**（`lst = [...]`），外部也不受影響——因為只是讓本地變數指向新物件。

    </details>

---

17. 為什麼 `list` 不能當 `dict` 的 key，但 `tuple` 可以？
    <details>
    <summary>Answer</summary>

    dict key 必須是 **hashable**：有穩定的 `hash()` 值，且能用 `==` 比較。

    - `list` 是 mutable，內容可以改變，hash 值不穩定 → 不是 hashable → ❌ 不能當 key
    - `tuple` 是 immutable → hashable → ✅ 可以當 key

    ```python
    d = {}
    d[(1, 2)] = "ok"       # ✅
    # d[[1, 2]] = "bad"    # ❌ TypeError: unhashable type: 'list'
    ```

    **陷阱：** 包含 mutable 物件的 tuple 也不能當 key：
    ```python
    t = ([1, 2], 3)
    # d[t] = "bad"  # ❌ 因為內層 list 不是 hashable
    ```

    </details>

---

18. `tuple` 是 immutable，為什麼這段程式碼可以執行？
    <details>
    <summary>Answer</summary>

    ```python
    t = ([1, 2], [3, 4])
    t[0].append(99)
    print(t)   # ([1, 2, 99], [3, 4])
    ```

    tuple 的 immutable 指的是「**不能換掉 tuple 裡儲存的參考**」，而不是說參考指向的物件不能變。

    - `t[0] = [99]` → ❌ TypeError，換掉參考
    - `t[0].append(99)` → ✅ 修改參考指向的 list 本身

    </details>
