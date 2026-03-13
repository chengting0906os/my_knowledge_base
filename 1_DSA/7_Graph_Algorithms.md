# Graph Algorithms

- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Topological Sort
- Dijkstra's Algorithm

---

## Graph Representations

### Comparison

| Representation | Space | Edge Query (u,v) | Neighbor Iteration | Best For |
|----------------|-------|------------------|--------------------|----------|
| Adjacency Matrix | O(n²) | O(1) | O(n) | Dense graphs, frequent edge lookups |
| Adjacency List | O(n + E) | O(degree(u)) | O(1) | General use, sparse graphs |
| Edge List | O(E) | O(E) | O(E) | Edge-centric ops (e.g. Kruskal) |
| Degree Array | O(n) | ❌ | ❌ | Degree counting only |

---

### Adjacency Matrix

An n×n 2D array where `matrix[u][v] = 1` means there is an edge u→v.

```python
n = 5
matrix = [[0] * n for _ in range(n)]
matrix[0][1] = 1  # directed: 0 → 1
matrix[1][0] = 1  # undirected: also add reverse
```

**Pros**
- Edge existence check (u, v): O(1)
- Simple to implement

**Cons**
- Always O(n²) space — wasteful for sparse graphs
- Iterating all neighbors requires scanning the full row: O(n)

---

### Adjacency List

Each node holds a list of its neighbors. The default choice for most problems.

```python
from collections import defaultdict

graph = defaultdict(list)
graph[0].append(1)  # directed: 0 → 1
graph[1].append(0)  # undirected: also add reverse

for v in graph[u]:  # iterate neighbors of u
    ...
```

**Pros**
- Space O(n + E) — efficient for sparse graphs
- Neighbor iteration: O(degree), no wasted work

**Cons**
- Checking if edge (u, v) exists requires scanning u's list: O(degree(u))

---

### Edge List

All edges stored as a flat list of `(u, v)` or `(u, v, weight)` tuples.

```python
edges = [(0, 1, 4), (1, 2, 3), (0, 2, 10)]  # (u, v, weight)

# Sort by weight — used in Kruskal's MST
edges.sort(key=lambda e: e[2])
```

**Pros**
- Space O(E) — the most compact representation
- Natural fit when edges need to be sorted (Kruskal)

**Cons**
- Any neighbor or edge query requires a full scan: O(E)

---

### Degree Array

Only stores how many edges each node has — no connectivity information.

```python
degree = [0] * n
for u, v in edges:
    degree[u] += 1
    degree[v] += 1  # undirected
```

**Use cases**
- Topological Sort: find nodes with in-degree 0 as starting points
- Eulerian Path: check the number of odd-degree nodes
- Cannot be used for graph traversal (BFS/DFS)

---

### When to Use What

```
Dense graph (E ≈ n²)          → Adjacency Matrix
Sparse graph (general case)   → Adjacency List  ← default choice
Need to sort edges (Kruskal)  → Edge List
Only need degree counts        → Degree Array
```
