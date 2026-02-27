# HTTP Methods

## English Version

### 1. What Is an HTTP Method

- An HTTP method tells the server what action the client wants to perform on a resource.
- Resource is identified by URL, method describes the operation type.

### 2. Core Methods (Interview Focus)

| Method  | Typical Meaning                      | Idempotent | Request Body |
| ------- | ------------------------------------ | ---------- | ------------ |
| GET     | Read data                            | Yes        | Usually no   |
| POST    | Create/submit action                 | No         | Usually yes  |
| PUT     | Replace full resource                | Yes        | Usually yes  |
| PATCH   | Partially update resource            | Not guaranteed | Usually yes  |
| DELETE  | Remove resource                      | Yes        | Usually no   |
| HEAD    | Same as GET but no response body     | Yes        | No           |
| OPTIONS | Ask supported methods/CORS preflight | Yes        | No           |

### 3. Key Terms

- Idempotent:
  - Repeating the same request should produce the same final state.
  - Example: `PUT` and `DELETE` are idempotent by definition.

### 4. Common REST Mapping

- `GET /users`: list users
- `GET /users/{id}`: get one user
- `POST /users`: create user
- `PUT /users/{id}`: replace user
- `PATCH /users/{id}`: partially update user
- `DELETE /users/{id}`: delete user

### 5. Practical Notes

- Do not use `GET` to do write operations.
- `PUT vs POST`:
  - `POST` is usually for create/action and is typically not idempotent.
  - `PUT` is usually for full replacement of an existing resource and is idempotent.
- `PUT` vs `PATCH`:
  - `PUT` is full replacement.
  - `PATCH` changes only specific fields and is not guaranteed idempotent.
  - Example: `PATCH {"increment": 1}` is often non-idempotent.
- Common success status codes:
  - `POST`: `201 Created` (often with `Location` header)
  - `PUT` / `PATCH`: `200 OK` or `204 No Content`
- `DELETE` can return:
  - `200 OK` (with body)
  - `202 Accepted` (async delete)
  - `204 No Content` (success without body)
- `OPTIONS` is important for CORS preflight.

### 6. Quick Interview Summary

- Method defines action; URL defines resource.
- `GET` is read, `POST` is create/action, `PUT/PATCH` are update, `DELETE` is remove.
- `PUT vs POST`: `POST` is usually non-idempotent; `PUT` is idempotent.
- `PUT vs PATCH`: `PUT` is full replacement; `PATCH` is partial update.
- `PATCH` idempotency depends on operation (set-value may be idempotent, increment usually is not).

---

## 中文版本

### 1. 什麼是 HTTP Method

- HTTP Method 是用來告訴伺服器「我要對這個資源做什麼操作」。
- URL 指向資源，Method 表示操作行為。

### 2. 核心方法（面試最常問）

| 方法    | 典型語意                   | Idempotent（冪等） | Request Body |
| ------- | -------------------------- | ------------------ | ------------ |
| GET     | 讀取資料                   | 是                 | 通常沒有     |
| POST    | 建立資料/觸發動作          | 否                 | 通常有       |
| PUT     | 全量覆蓋更新               | 是                 | 通常有       |
| PATCH   | 部分欄位更新               | 不保證             | 通常有       |
| DELETE  | 刪除資料                   | 是                 | 通常沒有     |
| HEAD    | 與 GET 類似，但不回傳 body | 是                 | 沒有         |
| OPTIONS | 查詢可用方法 / CORS 預檢   | 是                 | 沒有         |

### 3. 名詞重點

- Idempotent（冪等）：
  - 相同請求重複送出，最終狀態應一致。
  - 典型是 `PUT`、`DELETE`。

### 4. REST 常見路由對應

- `GET /users`：取得使用者列表
- `GET /users/{id}`：取得單一使用者
- `POST /users`：建立使用者
- `PUT /users/{id}`：整筆覆蓋更新
- `PATCH /users/{id}`：部分欄位更新
- `DELETE /users/{id}`：刪除使用者

### 5. 實務補充

- 不要用 `GET` 做寫入。
- `PUT` vs `POST`：
  - `POST` 常用於建立或觸發動作，通常非冪等。
  - `PUT` 常用於對既有資源做整筆覆蓋更新，且為冪等。
- `PUT` vs `PATCH`：
  - `PUT` 偏向整筆替換。
  - `PATCH` 只改部分欄位，且冪等性不保證。
  - 例如 `PATCH {"increment": 1}` 通常不是冪等。
- 常見成功回應碼：
  - `POST`：`201 Created`（常搭配 `Location` header）
  - `PUT` / `PATCH`：`200 OK` 或 `204 No Content`
- `DELETE` 常見回應碼：
  - `200 OK`（有回應內容）
  - `202 Accepted`（非同步刪除）
  - `204 No Content`（成功但無回應內容）
- `OPTIONS` 在 CORS preflight 很常出現。

### 6. 面試一句話

- URL 是資源，Method 是動作。
- `GET` 讀、`POST` 建、`PUT/PATCH` 更、`DELETE` 刪。
- `PUT vs POST`：`POST` 通常非冪等；`PUT` 為冪等。
- `PUT vs PATCH`：`PUT` 是完整替換；`PATCH` 是部分欄位修改。
- `PATCH` 是否冪等取決於操作內容（設值常可冪等，`increment` 通常不冪等）。
