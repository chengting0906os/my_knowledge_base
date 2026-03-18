# Circuit Breaker

## 中文版

當下游服務持續失敗時，主動「斷路」停止繼續發送請求，避免錯誤級聯蔓延（Cascading Failure），並給下游服務時間恢復。

### 三個狀態

```
        失敗率超過閾值
Closed ─────────────────→ Open
  ↑                          │
  │  成功                    │ 等待 timeout
  │                          ↓
  └──────────────── Half-Open
       部分請求試探
```

| 狀態 | 行為 |
|------|------|
| **Closed**（正常） | 請求正常通過，記錄失敗率 |
| **Open**（斷路） | 直接 Fail Fast，不發請求，立即回傳錯誤或 fallback |
| **Half-Open**（試探） | 放行少量請求測試下游是否恢復，成功則回 Closed，失敗則回 Open |

### 為什麼需要？
- 沒有斷路器：上游一直打失敗的下游 → 上游 thread pool 耗盡 → 上游也崩 → 整個系統雪崩
- 有斷路器：失敗達閾值 → 直接 Fail Fast → 保護上游資源

### 常搭配
- **Retry**：短暫錯誤時重試
- **Fallback**：斷路時回傳預設值或快取資料
- **Timeout**：避免等太久

常見實作：Resilience4j（Java）、Hystrix（舊）、Polly（.NET）

## English Version

A Circuit Breaker stops sending requests to a failing downstream service, preventing cascading failures and giving the downstream time to recover.

### Three States

```
        Failure rate exceeds threshold
Closed ─────────────────────────────→ Open
  ↑                                      │
  │  Success                             │ Wait timeout
  │                                      ↓
  └──────────────────────────── Half-Open
           Probe with limited requests
```

| State | Behavior |
|-------|---------|
| **Closed** (normal) | Requests pass through; failure rate tracked |
| **Open** (tripped) | Fail Fast — immediately return error or fallback without calling downstream |
| **Half-Open** (probing) | Allow limited requests to test recovery; success → Closed, failure → Open |

### Why it matters
- Without circuit breaker: upstream keeps hitting a failing service → upstream thread pool exhausted → upstream crashes → full cascade failure
- With circuit breaker: failures reach threshold → Fail Fast → upstream resources protected

### Commonly paired with
- **Retry**: for transient errors
- **Fallback**: return default or cached value when open
- **Timeout**: prevent long waits

Common implementations: Resilience4j (Java), Hystrix (legacy), Polly (.NET)
