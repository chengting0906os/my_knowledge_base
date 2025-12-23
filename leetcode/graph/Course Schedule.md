# Course Schedule

## Problem Description

You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.

The pair `[0, 1]`, indicates that must take course 1 before taking course 0.

There are a total of `numCourses` courses you are required to take, labeled from `0` to `numCourses - 1`.

Return `true` if it is possible to finish all courses, otherwise return `false`.

## Examples

### Example 1

```text
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true
```

**Explanation:** First take course 1 (no prerequisites) and then take course 0.

### Example 2

```text
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false
```

**Explanation:** In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.

## Constraints

- `1 <= numCourses <= 1000`
- `0 <= prerequisites.length <= 1000`
- `prerequisites[i].length == 2`
- `0 <= a[i], b[i] < numCourses`
- All prerequisite pairs are unique.

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**

- It's a directed graph (course b → course a means "b must be taken before a")
- If there is a cycle in this graph, it's impossible to finish all courses (return false)

### M - Match

**Pattern:** Graph, Adjacency List

### P - Plan

- DFS

1. create a mp which keys are course, values are prerequisites
2. create a visted set()
3.

```
def dfs(c):
    # cycle deteted
    if c in visting:
        return False

    # No prerequisites
    if mp[c] == []:
        return True

    # dfs mark as visting
    visited.add(c)
    for pre in mp[c]:
        if not dfs(pre):
            return False
    visited.remove(c)

    # mark as verified, no need to check
    mp[c] = []

    return True
```

4. if not def(c) return False else True

- BFS

1. create an indegrees = [0] \* len(numCourses)
2. create an Adjacency List

```
adj = [[] for in range(numCourses)]
for c, pre in prerequisites:
    indegrees[c] += 1
    adj[pre].append(c)
```

3. create a queue = deque() than append indegree = 0 course into it

```
queue = deque()

for c, indegree in enumerate(indegrees):
    if indegree == 0:
        queue.append(c)
```

4. add termination condition - return finished == numCourses
5. start to BFS

```

while queue:
    c = queue.popleft()
    finised += 1
    for nxt in adj[c]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

```

### I - Implement

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
