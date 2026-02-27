## MITM（Man-in-the-Middle，中間人攻擊）

在 MITM 攻擊中，攻擊者夾在使用者與伺服器之間，攔截、監聽，甚至竄改雙方傳輸的資料。  
Web 情境常見於瀏覽器與網站通訊過程，特別是在不安全的 HTTP 或惡意公共 Wi-Fi 環境。

## 防禦重點

- 全站使用 HTTPS（不只登入頁）
- 所有子資源（JS/CSS/圖片/字型）也必須走 HTTPS，避免 mixed content
- 使用安全的 TLS 設定與有效憑證
- 啟用 HSTS（`Strict-Transport-Security`）降低 SSL stripping 風險
- 可考慮加入 HSTS preload 清單，降低首次連線被降級風險

### Django 範例（HSTS）

在 `settings.py` 設定：

```python
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

說明：

- Django 會在 HTTPS 回應加上 `Strict-Transport-Security` header。
- 瀏覽器收到後，會在 `max-age` 期間強制使用 HTTPS，降低 SSL stripping 風險。

## Ref

- https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/MITM
