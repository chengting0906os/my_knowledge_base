# Redundant Connection

## Problem Description

You are given a connected undirected graph with `n` nodes labeled from `1` to `n`. Initially, it contained no cycles and consisted of `n-1` edges.

We have now added one additional edge to the graph. The edge has two different vertices chosen from `1` to `n`, and was not an edge that previously existed in the graph.

The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` represents an edge between nodes `ai` and `bi` in the graph.

Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears **last** in the input `edges`.

## Examples

### Example 1

```text
Input: edges = [[1,2],[1,3],[3,4],[2,4]]
Output: [2,4]
```

### Example 2

```text
Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
Output: [3,4]
```

## Constraints

- `n == edges.length`
- `3 <= n <= 100`
- `1 <= edges[i][0] < edges[i][1] <= edges.length`
- There are no repeated edges and no self-loops in the input

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**

- Use Union Find to detect cycle
- If `find(u) == find(v)` before union → this edge creates a cycle → redundant
- Return the last such edge in input order

### M - Match

**Pattern:** Union Find

### P - Plan

1. Initialize DSU with `parent[i] = i` and `rank[i] = 1`
2. Implement `find(x)` with path compression
3. Implement `union(u, v)`:
   - If same parent → return `False` (cycle detected)
   - Else union by rank → return `True`
4. Iterate edges: if `union(u, v)` returns `False`, return `[u, v]`

### I - Implement

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:** O(E × α(V)) ≈ O(E)

- α is inverse Ackermann, practically constant

**Space Complexity:** O(V)