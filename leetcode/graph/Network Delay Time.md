# Network Delay Time

## Problem Description

You are given a network of `n` directed nodes, labeled from `1` to `n`. You are also given `times`, a list of directed edges where `times[i] = (ui, vi, ti)`:

- `ui` is the source node (an integer from `1` to `n`)
- `vi` is the target node (an integer from `1` to `n`)
- `ti` is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to `0`)

You are also given an integer `k`, representing the node that we will send a signal from.

Return the **minimum time** it takes for all of the `n` nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return `-1` instead.

## Examples

### Example 1

```text
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Explanation: The signal starts at node 2, reaches node 1 and 3 at time 1, then reaches node 4 at time 2.
```

### Example 2

```text
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

### Example 3

```text
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
Explanation: Node 1 cannot be reached from node 2.
```

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= ui, vi <= n`
- `ui != vi`
- `0 <= ti <= 100`
- All the pairs `(ui, vi)` are unique (i.e., no multiple edges)

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:**

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

```python

```

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

**Space Complexity:**
