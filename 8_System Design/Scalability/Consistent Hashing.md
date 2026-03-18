# Consistent Hashing

## 中文版

一種雜湊策略，讓新增或移除節點時，**只有少量資料需要重新映射**，而非全部重新分配。

### 問題背景

普通 Hash Sharding：`node = hash(key) % N`
- N 個節點時，key 對應 node 2
- 擴容到 N+1 時，幾乎所有 key 都換了節點 → 大量 cache miss 或資料遷移

### 一致性雜湊原理

1. 將 node 和 key 都 hash 到同一個**環（0 ~ 2³²）** 上
2. 每個 key 順時針找到第一個 node，由它負責
3. 新增節點：只影響該節點到前一個節點之間的 key（約 1/N 的資料）
4. 移除節點：該節點的資料移給下一個節點

```
        0
      /   \
  Node A   Node D
    |         |
  Node B   Node C
      \   /
      max
```

### Virtual Nodes（虛擬節點）
將每個實體節點映射到環上多個位置，讓資料分布更均勻，避免因節點雜湊值湊巧集中造成不均。

### 使用場景
- 分散式快取（Memcached、Redis Cluster）
- 分散式資料庫路由
- CDN 節點選擇

## English Version

A hashing strategy that ensures only a **small fraction of keys need remapping** when nodes are added or removed — not all of them.

### The Problem

Naive Hash Sharding: `node = hash(key) % N`
- With N nodes, key maps to node 2
- Scale to N+1 → almost all keys remap → massive cache misses or data migration

### How Consistent Hashing Works

1. Hash both **nodes** and **keys** onto the same **ring (0 ~ 2³²)**
2. Each key is assigned to the first node it encounters going clockwise
3. Add a node: only the keys between the new node and the previous node are remapped (~1/N of data)
4. Remove a node: its keys are reassigned to the next node clockwise

### Virtual Nodes
Map each physical node to multiple positions on the ring for more even distribution, avoiding hot spots caused by unlucky hash placement.

### Use Cases
- Distributed caching (Memcached, Redis Cluster)
- Distributed database routing
- CDN node selection
