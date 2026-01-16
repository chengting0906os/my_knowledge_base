# Unique Paths

## Problem Description

There is an `m x n` grid where you are allowed to move either **down** or **to the right** at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that can be taken from the top-left corner of the grid `(grid[0][0])` to the bottom-right corner `(grid[m - 1][n - 1])`.

You may assume the output will fit in a 32-bit integer.

## Examples

### Example 1

```text
Input: m = 3, n = 6
Output: 21
```

### Example 2

```text
Input: m = 3, n = 3
Output: 6
```

## Constraints

- `1 <= m, n <= 100`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** DP

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

**Bottom-Up DP (2D Array) - O(m×n) Space**

1. Create a `m x n` 2D DP list
2. **Base Case:**
   - `dp[0][j] = 1` (first row: only from left)
   - `dp[i][0] = 1` (first col: only from above)
3. **Transition:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
4. Return `dp[m-1][n-1]`

**Space Optimized (1D Array) - O(n) Space**

Each row only depends on previous row → compress to 1D:

1. Create `dp = [1] * n` (first row all 1s)
2. **Transition:** For each row (m-1 times):
   - `dp[j] = dp[j] + dp[j-1]`
     - `dp[j]` (before update) = from above (previous row)
     - `dp[j-1]` (already updated) = from left (same row)

```python
dp = [1] * n
for _ in range(1, m):
    for j in range(1, n):
        dp[j] = dp[j] + dp[j-1]
return dp[-1]
```

3. Return `dp[-1]`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(m x n)

**Space Complexity:**
O(n)
