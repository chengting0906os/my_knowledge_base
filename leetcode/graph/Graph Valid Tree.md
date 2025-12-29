# Graph Valid Tree

## Problem Description

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

> **Note:**
>
> - You can assume that no duplicate edges will appear in edges
> - Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges

## Examples

### Example 1

```text
Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true
```

### Example 2

```text
Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false
```

## Constraints

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

- `edges = []` with `n = 1` → single node, valid tree → `true`
- `edges = []` with `n > 1` → disconnected nodes → `false`
- Disconnected sub-graphs → `false`

**Key Observations:**

- Valid tree conditions: **no cycle** + **all nodes connected**
- For a tree with `n` nodes, must have exactly `n - 1` edges
- This is an **undirected graph** (need to track parent to avoid false cycle detection)

### M - Match

**Pattern:** Graph / DFS / BFS / Union Find

### P - Plan

1. Early termination check

```python
if len(edges) != n - 1:
    return False
```

2. Build adjacency list (undirected → add both directions)

```python
adj = [[] for _ in range(n)]
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)
```

3. DFS with parent tracking to detect cycle

```python
visited = set()

def dfs(node, parent):
    visited.add(node)

    for nei in adj[node]:
        if nei == parent:  # skip the edge we came from
            continue
        if nei in visited:  # cycle detected
            return False
        if not dfs(nei, node):
            return False

    return True
```

4. Check: no cycle + all nodes visited

```python
return dfs(0, -1) and len(visited) == n
```

### I - Implement

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass
```

### R - Review
- Need to check len(visited) == n

### E - Evaluate

**Time Complexity:**
O(V + E)

**Space Complexity:**
O(V + E)
