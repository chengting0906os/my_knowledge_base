# Graph

| 表示法 | Space | Add Edge | Check Edge | Iterate Neighbors |
|--------|-------|----------|------------|-------------------|
| Adjacency List | O(V+E) | O(1) | O(degree) | O(degree) |
| Adjacency Matrix | O(V²) | O(1) | O(1) | O(V) |
| Edge List | O(E) | O(1) | O(E) | O(E) |
| Union-Find | O(V) | O(α(V)) | O(α(V)) | — |

> Adjacency List：稀疏圖首選；Adjacency Matrix：稠密圖或需快速查邊；Union-Find：判斷連通性、偵測 cycle

- Adjacency List
- Adjacency Matrix
- Edge List
- Union-Find (Disjoint Set)

# Graph Algorithms

| 演算法 | Time | Space | 用途 |
|--------|------|-------|------|
| BFS | O(V+E) | O(V) | 最短路徑（無權重）、層序遍歷 |
| DFS | O(V+E) | O(V) | 連通性、cycle 偵測、path 探索 |
| Topological Sort (DFS) | O(V+E) | O(V) | DAG 排序 |
| Kahn's Algorithm | O(V+E) | O(V) | DAG 排序，可偵測 cycle |
| Dijkstra's | O((V+E) log V) | O(V) | 單源最短路徑（非負權重）|
| Bellman-Ford | O(VE) | O(V) | 單源最短路徑（允許負權重）|
| Floyd-Warshall | O(V³) | O(V²) | 全點對最短路徑 |
| Prim's (MST) | O((V+E) log V) | O(V) | 最小生成樹（稠密圖）|
| Kruskal's (MST) | O(E log E) | O(V) | 最小生成樹（稀疏圖）|

- BFS (Breadth-First Search) — [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- DFS (Depth-First Search) — [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- Topological Sort (DFS-based) — [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- Kahn's Algorithm (Topological Sort, BFS-based / in-degree) — [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- Dijkstra's Algorithm — [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- Bellman-Ford Algorithm — [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- Floyd-Warshall Algorithm — [1334. Find the City With the Smallest Number of Neighbors](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- Prim's Algorithm (MST) — [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
- Kruskal's Algorithm (MST) — [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
