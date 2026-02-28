# Authentication vs Authorization

## 中文簡答

### Authentication（驗證身份）

- 你是誰。
- 常見方式：密碼、OTP、OAuth、Biometric。

### Authorization（授權）

- 你能做什麼。
- 常見方式：Role/Permission（RBAC）、Policy、ACL。

### 差異一句話

- 先 Authentication，再 Authorization。  
- 先確認「是不是你」，再決定「你可不可以做這件事」。

### 例子

- 登入成功 = Authentication 通過。  
- 你能不能刪除訂單 = Authorization 判斷。

---

## English Short Version

### Authentication

- Verifies identity: "Who are you?"
- Examples: password, OTP, OAuth, biometrics.

### Authorization

- Controls access: "What can you do?"
- Examples: roles/permissions (RBAC), policies, ACL.

### One-liner

- Authentication first, authorization second.

### Example

- Login success = authentication.  
- Can delete an order = authorization.
