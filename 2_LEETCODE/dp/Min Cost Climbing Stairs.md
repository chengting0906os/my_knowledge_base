# Min Cost Climbing Stairs

## Problem Description

You are given an array of integers `cost` where `cost[i]` is the cost of taking a step from the `i`th floor of a staircase. After paying the cost, you can step to either the `(i + 1)`th floor or the `(i + 2)`th floor.

You may choose to start at index `0` or index `1`.

Return the minimum cost to reach the top of the staircase (just past the last index in `cost`).

## Examples

### Example 1

```text
Input: cost = [1,2,3]
Output: 2
```

**Explanation:** Start at index 1, pay cost[1] = 2, take two steps to reach the top. Total cost = 2.

### Example 2

```text
Input: cost = [1,2,1,2,1,1,1]
Output: 4
```

**Explanation:**

- Pay cost[0] = 1, take two steps to index 2
- Pay cost[2] = 1, take two steps to index 4
- Pay cost[4] = 1, take two steps to index 6
- Pay cost[6] = 1, take one step to the top
- Total cost = 4

## Constraints

- `2 <= cost.length <= 100`
- `0 <= cost[i] <= 100`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- The "top" is past the last index (i.e., index `len(cost)`)
- You can start at index 0 or 1 (both are free to stand on, you pay when you step)

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

- **Pattern:** DP (similar to Climbing Stairs, but with cost)

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. For each element from index-2 cost[i] = min(cost[i]+cost[i-1], cost[i]+cost[i-2])
2. return min(cost[-1], cost[-2])

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(n)

**Space Complexity:**
O(1) — only need two variables
