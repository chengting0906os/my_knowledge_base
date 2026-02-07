## **🔥 1. Redis「穿透」(Cache Penetration)**
**📌 定義**
使用者一直查詢 **不存在於 cache，也不存在於 DB** 的 key。
因為 cache 查不到 → 系統會不斷打 DB 造成：
- DB 直接被打爆
- Redis 完全派不上用場
**📘 常見例子**
查：
user_id = -1
user_id = 9999999999999
隨機亂 key
攻擊者惡意用不存在的 key 不停 bombard
Redis 沒有 → DB 沒有 → 每次都查 DB → DB 撐不住。
**🧯 解法**
**✔ 方案 A：查不到也要 cache（cache null）**
把「查不到」的結果也放進 cache：
user:999999 → null (TTL: 5 minutes)
下次再查就不會打 DB。
**✔ 方案 B：正規化參數（validate parameter）**
查 user id = -1 直接擋掉，不去查 DB。
**✔ 方案 C：布隆過濾器（Bloom Filter）**
做前置判斷：
key 不可能存在 → 不查 Redis 不查 DB

## **❄️ 2. Redis「雪崩」(Cache Avalanche)**
**📌 定義**
**大量 key 同時過期 → Redis 瞬間掉光資料 → 全部 traffic 打到 DB → DB 當場崩潰。**
這是 cache 崩潰災難中的 “核爆級事故”。
**📘 例子**
你 cache 每個 key 都設 TTL = 10 分鐘 剛好 **同一時間大量 key 過期**
12:00 都過期  
12:00 ~ 12:05 直接打 DB  
DB 讀流量爆表
**🧯 解法**
**✔ 方案 A：TTL 加隨機值**
不要讓 key 在同一個時間過期：
TTL = 600s + random(0~60)
**✔ 方案 B：多層 cache（本地 + Redis）**
避免單點災難。
**✔ 方案 C：Cache 預熱（warm-up）**
服務啟動時，預先把熱門 key 加入 cache。
**✔ 方案 D：熔斷與降級**
一旦 Redis 大量 miss → 暫停 DB 低價值查詢。

## **🔦 3. Redis「擊穿」(Cache Breakdown)**
**📌 定義**
某個 **超熱門 key**（例如：商品庫存、促銷資訊）突然過期。
於是：
- 大量使用者同時查詢這個 key
- Redis miss
- 大量請求同時打 DB → DB 被瞬間打爆
⚠️ 和「雪崩」最重要的差別：

| 類型 | 特徵 |
| --- | --- |
| 雪崩 | 很多 key 同時過期 |
| 击穿 | **一個** 超熱門 key 過期 |


雪崩 = 大量 key 擊穿 = 熱點 key

**📘 例子**
搶購系統常見：
product:123:inventory TTL=0
瞬間 20 萬人打 DB 拿庫存 → 系統直接死

**🧯 解法**
**✔ 方案 A：互斥鎖（mutex）**
只有「第一個」 miss 的人去 Query DB，其他人等：
SETNX lock:product:123
查完之後把結果寫回 Redis。
**✔ 方案 B：永不過期（或很長 TTL）**
熱門資料 → TTL 不用太短。
（你之前 seat bitmap 用 Redis 就是這種模式）
**✔ 方案 C：邏輯過期（Logical expiration）**
key 在 Redis 裡 TTL 很長，但 value 裡面自己寫：
expire_time = timestamp
到期後：
- 使用者仍能拿到舊資料（不會炸 DB）
- 後台 worker 自動 refresh
**✔ 方案 D：Local cache（例如：JVM/Node 內建 LRU）**
熱點不一定完全依賴 Redis。

## **🔥 三者的差異摘要表（面試用）**

| 名稱 | 發生原因 | 現象 | 風險 |
| --- | --- | --- | --- |
| **穿透** | 查詢不存在 key | Redis miss + DB miss | DB 被頻繁打爆 |
| **雪崩** | 大量 key 同時過期 | Redis 同時失效 | DB 瞬間超載 |
| **擊穿** | 熱門 key 過期 | 很多請求同時查 DB | DB 熱點被打爆 |


## **🎯 你如果在做票務（你就是啊）**
常見情境：
**✔ Redis 穿透**
查不存在的 event_id → 可用 Bloom Filter
**✔ Redis 雪崩**
座位區 bitmap 大量 TTL 一起過期（不要用 TTL，一律邏輯過期）
**✔ Redis 擊穿**
某個場館座位被高頻查 → 要提前 refresh（你現在 BITFIELD 是永不過期，這是對的）

如果你要，我可以補：
**🔥 在「票務系統」裡 3 大 Redis 問題的最佳實作**
**🔥 Redis 與 Kvrocks 的差異（你在用的是 Kvrocks）**
**🔥 用你的 seat bitmap 如何防止 cache breakdown（擊穿）**
你想看哪一個？
