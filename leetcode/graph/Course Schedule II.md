# Course Schedule II

## Problem Description

You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.

For example, the pair `[0, 1]`, indicates that to take course 0 you have to first take course 1.

There are a total of `numCourses` courses you are required to take, labeled from `0` to `numCourses - 1`.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

## Examples

### Example 1

```text
Input: numCourses = 3, prerequisites = [[1,0]]
Output: [0,1,2]
```

**Explanation:** We must ensure that course 0 is taken before course 1.

### Example 2

```text
Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
Output: []
```

**Explanation:** It's impossible to finish all courses.

## Constraints

- `1 <= numCourses <= 1000`
- `0 <= prerequisites.length <= 1000`
- All prerequisite pairs are unique.

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**

- Same as Course Schedule I, but return the topological order instead of boolean
- If there is a cycle, return `[]`

### M - Match

**Pattern:** Graph, Topological Sort

### P - Plan

1. create an indegrees = [0] \* len(numCourses)
2. create an Adjacency List adj = [[] for _ in range(numCourses)]
```
for c, pre in prerequisites:
    indegrees[c] += 1
    adj[pre].append(c)

```
3. res = [], finished =0
4. create queue
5. 
```
while queue:
    c = queue.popleft()
    finished += 1
    res.append(c)
    for nxt in adj[c]
        indegrees[nxt] -= 1
        if indegress[nxt] == 0
            queue.append(nxt)
    
```
6. return res

### I - Implement

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
