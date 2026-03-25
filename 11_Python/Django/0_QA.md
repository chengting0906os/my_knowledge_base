# Django Interview Q&A List

1. Walk through Django's request/response lifecycle from a browser request to the final response.
   從瀏覽器送出 request 到收到 response，Django 的完整生命週期是什麼？
   <details>
   <summary>Answer</summary>

   ```
   Browser
     ↓ HTTP request
   Web Server（nginx / gunicorn）
     ↓
   WSGI / ASGI handler
     ↓
   Django Request object 建立
     ↓
   Middleware（由上往下，process_request）
     ↓
   URL Router（urls.py）→ 找到對應的 view
     ↓
   Middleware（繼續往下，process_view，若有）
     ↓
   View function / class-based view
     ├─ ORM 查詢 DB
     ├─ 呼叫 serializer / form
     └─ 回傳 HttpResponse / JsonResponse
     ↓
   Middleware（由下往上，process_response）
     ↓
   WSGI / ASGI handler
     ↓
   Web Server → Browser
   ```

   **各階段細節：**

   | 階段 | 說明 |
   |------|------|
   | Web Server | nginx 接收 request，轉給 gunicorn（WSGI）或 uvicorn（ASGI） |
   | WSGI handler | 把 HTTP request 轉成 Django 的 `HttpRequest` 物件 |
   | Middleware（request 方向） | 依 `MIDDLEWARE` 設定由上往下執行，可修改 request 或提前回傳 response（例如 `SecurityMiddleware` 強制 HTTPS） |
   | URL routing | `urlpatterns` 比對，找到對應 view；找不到 → 404 |
   | View | 核心業務邏輯，存取 DB、產生資料 |
   | Middleware（response 方向） | 由下往上執行，可修改 response header 或內容（例如 `GZipMiddleware` 壓縮） |

   **Exception 發生時**：Django 的 exception middleware（`process_exception`）會攔截，例如轉為 500 頁面或自訂錯誤處理。
   </details>

2. What is Django's ORM lazy evaluation, and when does a queryset actually hit the database?
   Django ORM 的 lazy evaluation 是什麼？queryset 什麼時候才真正打 DB？
   <details>
   <summary>Answer</summary>

   Queryset 是 lazy 的，建立 queryset 只是「描述」查詢，不會執行 SQL。直到以下操作才會真正打 DB：

   - **Iteration**：`for obj in queryset:`
   - **Slicing with step / 轉 list**：`list(queryset)`、`queryset[0:10]`
   - **len()**：`len(queryset)`
   - **bool()**：`if queryset:`
   - **repr()**：在 shell 印出 queryset
   - **Cache 已存在**：第一次執行後結果會被 cache，再次使用不打 DB

   ```python
   users = User.objects.filter(is_active=True)   # 不打 DB
   users = users.filter(age__gte=18)              # 不打 DB
   users = users.order_by('name')                 # 不打 DB
   result = list(users)                           # 這裡才打 DB（一次 SQL）
   print(len(result))                             # 不打 DB（用 cache）
   ```
   </details>

2. What is the N+1 problem, and how do `select_related` and `prefetch_related` solve it differently?
   什麼是 N+1 問題？`select_related` 和 `prefetch_related` 各如何解決？差別是什麼？
   <details>
   <summary>Answer</summary>

   **N+1 問題**：查詢 N 筆主資料後，對每筆再各打一次 DB 查關聯資料，共 N+1 次 SQL。

   ```python
   # N+1 示範（1 次查 books + N 次查 author）
   books = Book.objects.all()
   for book in books:
       print(book.author.name)  # 每次都打一次 DB
   ```

   **select_related**：用 SQL JOIN，一次取回主資料和關聯資料，適合 ForeignKey / OneToOne。
   ```python
   books = Book.objects.select_related('author').all()
   # 一次 SQL：SELECT book.*, author.* FROM book JOIN author ...
   ```

   **prefetch_related**：打兩次 SQL（分開查），在 Python 層做合併，適合 ManyToMany 或反向關聯。
   ```python
   authors = Author.objects.prefetch_related('books').all()
   # SQL 1：SELECT * FROM author
   # SQL 2：SELECT * FROM book WHERE author_id IN (1, 2, 3, ...)
   # Python 層合併
   ```

   | | select_related | prefetch_related |
   |---|---|---|
   | SQL 筆數 | 1 次（JOIN） | 2 次（分開查） |
   | 適用關係 | ForeignKey、OneToOne | ManyToMany、反向 FK |
   | 記憶體 | JOIN 可能有重複列 | 各自獨立，較乾淨 |
   </details>

3. How does Django's `atomic()` work, and what is the difference between `atomic()` and `select_for_update()`?
   `atomic()` 如何運作？它和 `select_for_update()` 差在哪？
   <details>
   <summary>Answer</summary>

   **`atomic()`**：將一段程式碼包成一個 DB transaction，任何 exception 都會 rollback。
   ```python
   from django.db import transaction

   with transaction.atomic():
       account_a.balance -= 100
       account_a.save()
       account_b.balance += 100
       account_b.save()
       # 若上面任一行出錯，兩個 save 都不會生效
   ```

   **`select_for_update()`**：在 SELECT 時加上 `FOR UPDATE` lock，防止其他 transaction 同時修改同一筆資料。

   ```python
   with transaction.atomic():
       account = Account.objects.select_for_update().get(id=1)
       # 其他 transaction 嘗試 select_for_update 同一筆時會等待
       account.balance -= 100
       account.save()
   ```

   | | atomic() | select_for_update() |
   |---|---|---|
   | 解決 | 多個操作的原子性（全成功或全失敗） | 並發寫入的 race condition |
   | 機制 | Transaction | Row-level lock（FOR UPDATE） |
   | 使用情境 | 任何需要一致性的多步驟操作 | 讀取後立刻修改（如扣款、搶票） |

   `select_for_update()` 必須在 `atomic()` 內使用。
   </details>

4. What is Django Middleware, and in what order does it execute for requests vs responses?
   Django Middleware 是什麼？request 和 response 的執行順序各是什麼方向？
   <details>
   <summary>Answer</summary>

   Middleware 是 Django request/response 流程中的「插件層」，每個 request 和 response 都會依序通過。

   **執行順序**：
   - **Request**：從 MIDDLEWARE 清單**由上往下**依序執行
   - **Response**：從 view 返回後，**由下往上**依序執行

   ```
   Request  →  MW1 → MW2 → MW3 → View
   Response ←  MW1 ← MW2 ← MW3 ←
   ```

   **自訂 Middleware 結構**：
   ```python
   class TimingMiddleware:
       def __init__(self, get_response):
           self.get_response = get_response  # 只在啟動時執行一次

       def __call__(self, request):
           # request 進來時執行（往下傳之前）
           start = time.time()

           response = self.get_response(request)  # 呼叫下一層

           # response 返回時執行（往上傳之前）
           duration = time.time() - start
           response['X-Duration'] = str(duration)
           return response
   ```
   </details>

5. What are Django Signals? What is `post_save`, and what is a common gotcha?
   什麼是 Django Signal？`post_save` 是什麼？有哪個常見陷阱？
   <details>
   <summary>Answer</summary>

   Signal 是 Django 的**發布/訂閱機制**，讓解耦的元件在事件發生時互相通知，不需要直接呼叫。

   **`post_save`**：model 執行 `save()` 後觸發。

   ```python
   from django.db.models.signals import post_save
   from django.dispatch import receiver

   @receiver(post_save, sender=User)
   def create_user_profile(sender, instance, created, **kwargs):
       if created:  # 區分新建 vs 更新
           Profile.objects.create(user=instance)
   ```

   **常見陷阱：`bulk_create` 不觸發 signal**

   ```python
   User.objects.bulk_create([User(...), User(...)])
   # post_save 不會被觸發！
   ```

   因為 `bulk_create` 直接打 SQL，跳過 Django 的 `save()` 方法。
   同樣的，`queryset.update()` 也不觸發 `post_save`。

   解法：手動迭代呼叫 `save()`，或在 `bulk_create` 後自己發送 signal。
   </details>

6. What is the difference between `F()` and `Q()` expressions?
   `F()` 和 `Q()` 各有什麼用途？
   <details>
   <summary>Answer</summary>

   **`F()`**：在 SQL 層直接引用欄位值，避免先讀到 Python 再寫回，防止並發 race condition。

   ```python
   # 危險：讀到 Python 再 -1，高並發下可能覆蓋其他人的修改
   product = Product.objects.get(id=1)
   product.stock -= 1
   product.save()

   # 安全：SQL 直接 UPDATE stock = stock - 1，原子操作
   Product.objects.filter(id=1).update(stock=F('stock') - 1)
   ```

   也可以在 filter 中比較兩個欄位：
   ```python
   # 找出庫存低於安全庫存的商品
   Product.objects.filter(stock__lt=F('safety_stock'))
   ```

   **`Q()`**：建立複雜的 OR / AND / NOT 條件，突破 `filter()` 只支援 AND 的限制。

   ```python
   from django.db.models import Q

   # OR 條件
   User.objects.filter(Q(city='Taipei') | Q(city='Kaohsiung'))

   # AND + OR 組合
   User.objects.filter(Q(age__gte=18) & (Q(city='Taipei') | Q(city='Tainan')))

   # NOT
   User.objects.filter(~Q(status='banned'))
   ```
   </details>

7. What is the difference between `annotate()` and `aggregate()`?
   `annotate()` 和 `aggregate()` 差在哪？
   <details>
   <summary>Answer</summary>

   - **`aggregate()`**：對整個 queryset 做聚合，回傳一個 **dict**（單一結果）
   - **`annotate()`**：對每一列（或每個 group）附加聚合值，回傳仍是 **queryset**

   ```python
   from django.db.models import Sum, Count, Avg

   # aggregate：整張表的統計 → 一個 dict
   result = Order.objects.aggregate(total=Sum('amount'), count=Count('id'))
   # {'total': Decimal('12345.00'), 'count': 500}

   # annotate：每個 user 各自的統計 → queryset，每列多一個欄位
   result = Order.objects.values('user_id').annotate(total=Sum('amount'))
   # <QuerySet [{'user_id': 1, 'total': ...}, {'user_id': 2, 'total': ...}, ...]>
   ```

   `annotate()` 常搭配 `values()` 做 GROUP BY，等同於：
   ```sql
   SELECT user_id, SUM(amount) AS total FROM orders GROUP BY user_id
   ```
   </details>

8. What is the difference between `values()`, `only()`, and `defer()`?
   `values()`、`only()`、`defer()` 差在哪？
   <details>
   <summary>Answer</summary>

   | | 回傳型態 | 用途 |
   |---|---|---|
   | `values('a','b')` | `QuerySet[dict]` | 只取指定欄位，回傳 dict，不是 model 物件 |
   | `only('a','b')` | `QuerySet[Model]` | 只取指定欄位，回傳 model 物件（存取其他欄位會再打一次 DB） |
   | `defer('c','d')` | `QuerySet[Model]` | 排除指定欄位，其餘都取，回傳 model 物件 |

   ```python
   # values：dict，輕量，不能呼叫 model method
   User.objects.values('id', 'name')
   # [{'id': 1, 'name': 'Alice'}, ...]

   # only：model 物件，但只 SELECT 指定欄位
   user = User.objects.only('id', 'name').first()
   user.name   # OK，已載入
   user.email  # 觸發額外 SQL！（deferred field）

   # defer：排除不需要的大欄位（如 TEXT 類型）
   User.objects.defer('bio', 'avatar')
   ```

   **只需要資料（不需要 model 行為）時用 `values()`，效能最好。**
   </details>

9. How do Django migrations work? What do `makemigrations` and `migrate` each do?
   Django migrations 如何運作？`makemigrations` 和 `migrate` 各做什麼？
   <details>
   <summary>Answer</summary>

   - **`makemigrations`**：比較目前的 model 定義和上一次的 migration 狀態，產生 migration 檔案（描述 schema 變更的 Python 檔）
   - **`migrate`**：執行尚未套用的 migration 檔案，實際修改 DB schema，並在 `django_migrations` 表記錄已執行的 migration

   **Zero-downtime 新增 NOT NULL 欄位的做法**：
   ```
   Step 1：先加欄位，設 nullable=True
   Step 2：Deploy，執行 migrate
   Step 3：用 data migration 補填舊資料的預設值
   Step 4：改欄位為 nullable=False，加 default
   Step 5：Deploy，執行 migrate
   ```

   **Migration 衝突（兩個人同時產生 migration）解法**：
   ```bash
   python manage.py makemigrations --merge
   # 產生一個 merge migration，把兩個分支合併
   ```
   </details>

10. What is a Django Custom Manager, and how do you implement one?
    什麼是 Custom Manager？如何實作？
    <details>
    <summary>Answer</summary>

    Manager 是 model 和 DB 之間的介面（`User.objects` 就是預設的 `Manager`）。
    Custom Manager 讓你封裝常用的 queryset 邏輯，讓呼叫端更簡潔。

    ```python
    class ActiveManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_active=True)

    class User(models.Model):
        name = models.CharField(max_length=100)
        is_active = models.BooleanField(default=True)

        objects = models.Manager()   # 保留原本的 objects
        active = ActiveManager()     # 新增 active manager

    # 使用
    User.active.all()               # 等同 User.objects.filter(is_active=True)
    User.active.filter(age__gte=18) # 可以繼續 chain
    ```

    也可以在 Manager 上加自訂方法：
    ```python
    class OrderManager(models.Manager):
        def paid(self):
            return self.filter(status='paid')

        def total_revenue(self):
            return self.aggregate(total=Sum('amount'))['total']
    ```
    </details>

11. What is WSGI vs ASGI in Django?
    Django 的 WSGI 和 ASGI 差在哪？
    <details>
    <summary>Answer</summary>

    | | WSGI | ASGI |
    |---|---|---|
    | 全名 | Web Server Gateway Interface | Asynchronous Server Gateway Interface |
    | 處理模型 | 同步（每個 request 佔用一個 thread） | 非同步（支援 async/await、WebSocket） |
    | 適合 | 一般 HTTP request/response | 長連線（WebSocket）、SSE、高並發 |
    | Django 版本 | Django 預設，所有版本支援 | Django 3.0+ |

    Django 3.1+ 支援 async view：
    ```python
    async def my_view(request):
        result = await some_async_operation()
        return JsonResponse({'result': result})
    ```

    **何時用 ASGI**：需要 WebSocket（即時聊天、通知推送）、或想用 async view 提升高並發效能時。
    </details>

12. How do you detect N+1 queries in Django tests?
    如何在 Django 測試中偵測 N+1 查詢？
    <details>
    <summary>Answer</summary>

    **方法 1：`assertNumQueries`**（內建，最直接）

    ```python
    from django.test import TestCase

    class BookTest(TestCase):
        def test_no_n_plus_one(self):
            Book.objects.bulk_create([Book(author=author) for author in Author.objects.all()])

            with self.assertNumQueries(1):  # 只允許 1 次 SQL
                books = list(Book.objects.select_related('author').all())
                for book in books:
                    _ = book.author.name
    ```

    **方法 2：`django.db.connection.queries`**（debug 用）
    ```python
    from django.db import connection, reset_queries
    from django.conf import settings

    settings.DEBUG = True
    reset_queries()

    books = Book.objects.all()
    for book in books:
        _ = book.author.name

    print(len(connection.queries))  # 印出 SQL 次數
    for q in connection.queries:
        print(q['sql'])
    ```

    **方法 3：`django-debug-toolbar`** — 在瀏覽器開發時顯示 SQL 次數與內容。

    **方法 4：`nplusone` 套件** — 自動偵測並在測試中 raise exception。
    </details>
