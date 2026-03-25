# PostgreSQL EXPLAIN / ANALYZE 手把手教學

## 章節目錄

| 章節 | 主題 | 核心概念 |
|------|------|---------|
| [Ch 0](00_setup.md) | 環境準備 | Docker 啟動、建立測試資料 |
| [Ch 1](01_explain_structure.md) | 輸出結構解讀 | cost、rows、width、loops、執行順序 |
| [Ch 2](02_seq_scan.md) | Sequential Scan | 何時出現、Rows Removed、不一定是壞事 |
| [Ch 3](03_index_scan.md) | Index Scan / Index Only Scan | 兩段式讀取、Heap Fetches、Covering Index |
| [Ch 4](04_bitmap_scan.md) | Bitmap Scan | 兩階段流程、exact vs lossy、BitmapAnd/Or |
| [Ch 5](05_join_types.md) | Join 類型 | Nested Loop / Hash Join / Merge Join |
| [Ch 6](06_buffers.md) | BUFFERS 與 Cache | shared hit/read、spill to disk |
| [Ch 7](07_statistics.md) | 統計資訊 | pg_stats、ANALYZE、Extended Statistics |
| [Ch 8](08_optimization.md) | 警訊與優化 | 診斷流程、常見案例 |

## 快速啟動

```bash
docker compose up -d
psql -h localhost -U lab -d lab   # 密碼：lab
```

## 最常用的指令

```sql
EXPLAIN (ANALYZE, BUFFERS) <查詢>;
ANALYZE <表名>;
VACUUM <表名>;
```
