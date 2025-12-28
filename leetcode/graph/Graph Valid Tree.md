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

```
if len(edges) > n:
    return False
```

**Key Observations:**

if cycle: False

### M - Match

**Pattern:** Graph / DFS / BFS

### P - Plan
1. 
```
if len(edges) > n:
    return False
```

2. adj list
3. 

### I - Implement

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
