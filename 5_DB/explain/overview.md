# 看懂 Query Plan

> 參考：https://hackmd.io/@moment89/QueryPlan

---

## SQL 執行四階段

1. **Parser**：檢查語法，產生語法樹 → 查詢樹
2. **Rewrite**：重組查詢樹（如 view 展開為實際 SQL）
3. **Planner/Optimizer**：根據 `pg_stats` 統計資料做成本估算，選出預期成本最低的查詢計畫
   - ✅ `EXPLAIN` 看到的就是這個階段的產物
   - ⚠️ 資料分佈不同，同一段 SQL 效能可能天差地別
4. **Executor**：實際執行計畫，回傳結果
   - ✅ `EXPLAIN ANALYZE` 會真正執行並回報實際時間

---

## EXPLAIN 欄位

| 欄位 | 意思 |
|---|---|
| `cost=A..B` | 預估成本（A=啟動，B=完成） |
| `rows` | 預估產出行數 |
| `width` | 每行預估大小（byte） |

## EXPLAIN ANALYZE 多出的欄位

| 欄位 | 意思 |
|---|---|
| `actual time=A..B` | 實際時間（ms） |
| `rows` | 實際產出行數 |
| `loops` | 該節點被執行幾次 |
| `Planning Time` | Planner 產生計畫的時間 |
| `Execution Time` | Executor 實際執行時間 |

> 上層節點的統計包含下層節點加總，所以上層 >= 下層總和

---

## 閱讀方式

**從縮排最深的地方往外讀**（內層先執行），找 cost / actual time 最大的節點，從瓶頸開始評估。

---

## 常見 Scan Node

| 節點 | 說明 | 注意 |
|---|---|---|
| **Seq Scan** | 全表逐筆掃描 | 資料量大時效能差 |
| **Index Scan** | 用 index 定位 block，再回 heap 撈資料 | 比 Seq Scan 快，但多一次 I/O |
| **Index Only Scan** | 直接從 index 取資料，不回 heap | 最快；用 INCLUDE 可擴大適用範圍 |
| **Bitmap Index Scan** | 先建 Bitmap 記錄符合條件的 block，再批次回 heap | 適合多條件（AND/OR）或命中量中等時 |

---

## 常見 Join Node

| 節點 | 適合情境 | 複雜度 |
|---|---|---|
| **Nested Loop** | 外層資料量小、JOIN 條件有 index、非等號條件 | O(M×N) 最差 |
| **Hash Join** | 等號條件、其中一方放得進 work_mem | 建 hash table，查找 O(1) |
| **Merge Join** | 等號條件、JOIN 欄位有 index（已排序） | 兩邊已排序才有效 |

---

## 常見 Operation Node

| 節點 | 說明 | 風險 |
|---|---|---|
| **Sort** | 排序，O(n log n) | 超過 work_mem 會溢出磁碟 |
| **Aggregate** | GROUP BY、SUM/COUNT 等 | Group 數量多時記憶體壓力大 |
| **Limit** | 取前 N 筆 | OFFSET 越大越慢 |
| **WindowAgg** | Window Function（ROW_NUMBER、RANK 等） | 排序成本高，大資料量效能差 |
| **Append** | 合併多個子計畫結果（UNION ALL、Partition） | - |

---

## 優化思路

**Scan：** 讓計畫走 Index Scan / Index Only Scan / Bitmap Index Scan
- 若有 index 卻不走 → 檢查條件是否與 index 相符、手動更新統計資料（`ANALYZE`）

**Join：** 兩表都大時希望走 Merge Join / Hash Join
- 若走 Nested Loop → 檢查是否用了非等號條件、能否改寫 SQL

**Operation：** 找 cost 特別大的節點，評估能否改邏輯或資料結構

---

## 重要觀念

- 同一段 SQL，資料分佈不同 → 計畫可能完全不同
- `Buffers: read` 大 → 磁碟 I/O 多 → 瓶頸來源
- `Buffers: hit` → 從 cache 拿，快
- 第一次執行慢（read），第二次快（hit）→ benchmark 需排除 I/O 噪音
- `Heap Fetches: 0` → Index Only Scan 最理想狀態
