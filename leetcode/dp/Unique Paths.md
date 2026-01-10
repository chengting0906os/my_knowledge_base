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

**Test Cases:**

**Edge Cases:**
- m = 1 or n = 1 → only one path (straight line)

**Key Observations:**
- Can only move right or down
- Total moves needed: (m-1) downs + (n-1) rights

### M - Match

**Pattern:** Dynamic Programming (Grid DP) / Combinatorics

### P - Plan

**Top-Down DP Approach (Memoization):**

1. Create memo table: `memo[row][col]` = number of paths from (row, col) to destination
2. Define `dfs(row, col)` → returns number of unique paths from current cell to bottom-right

   **Base cases:**
   - `row == m-1 and col == n-1` → return `1` (reached destination)
   - `row >= m or col >= n` → return `0` (out of bounds)
   - `memo[row][col] != -1` → return cached result

   **Recursion:**
   - `down = dfs(row + 1, col)` → move down
   - `right = dfs(row, col + 1)` → move right
   - `memo[row][col] = down + right`
   - return `memo[row][col]`

3. Return `dfs(0, 0)`

**Bottom-Up DP Approach:**

1. Create 2D DP table: `dp[i][j]` = number of paths to reach cell (i, j)

```
DP Table Structure (m = 3, n = 4):

         col →
          0   1   2   3
row  0    1   1   1   1
 ↓   1    1   2   3   4
     2    1   3   6   10
```

2. **Base case:** First row and first column are all `1` (only one way to reach)

3. **Transition:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
   - Paths from above + paths from left

4. Return `dp[m-1][n-1]`

### I - Implement

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:** O(m * n)

**Space Complexity:** O(m * n) or O(n) with space optimization
