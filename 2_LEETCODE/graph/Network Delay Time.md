# Network Delay Time

## Problem Description

You are given a network of `n` directed nodes, labeled from `1` to `n`. You are also given `times`, a list of directed edges where `times[i] = (ui, vi, ti)`.

- `ui` is the source node (an integer from `1` to `n`)
- `vi` is the target node (an integer from `1` to `n`)
- `ti` is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to `0`)

You are also given an integer `k`, representing the node that we will send a signal from.

Return the **minimum time** it takes for all of the `n` nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return `-1` instead.

## Examples

### Example 1

```text
Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1
Output: 3
```

### Example 2

```text
Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2
Output: -1
```

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 1000`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Graph

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. Initialize graph and state
   - Build adjacency list `adj` from `times`
   - For each `(u, v, w)` in `times`: `adj[u].append((v, w))`
   - `min_heap = [(0, k)]` # `(time, node)`
   - `visited = set()` E Maintain a visited set to avoid reprocessing nodes.
   - `max_time = 0`

2. While `min_heap` is not empty:
   - `t, node = heappop(min_heap)`
   - If `node` is already in `visited`, continue
   - Add `node` to `visited`
   - `max_time = t` # shortest finalized time for current node
   - For each `(nei, w)` in `adj[node]`:
   - If `nei` not in `visited`:
   - `heappush(min_heap, (t + w, nei))`

3. Return result
   - If `len(visited) == n`, return `max_time`
   - Else return `-1`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(ElogV) # each edge can trigger a heap push

**Space Complexity:**
O(V+E)
