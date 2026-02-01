# Coin Change II

## Problem Description

You are given an integer array `coins` representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer `amount` representing a target amount of money.

Return the **number of distinct combinations** that total up to `amount`. If it's impossible to make up the amount, return `0`.

You may assume that you have an **unlimited number** of each coin and that each value in `coins` is unique.

## Examples

### Example 1

```text
Input: amount = 4, coins = [1,2,3]
Output: 4
```

**Explanation:**

- 1+1+1+1 = 4
- 1+1+2 = 4
- 2+2 = 4
- 1+3 = 4

### Example 2

```text
Input: amount = 7, coins = [2,4]
Output: 0
```

## Constraints

- `1 <= coins.length <= 100`
- `1 <= coins[i] <= 5000`
- `0 <= amount <= 5000`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

- This is **Unbounded Knapsack** (can use each coin unlimited times)
- We count **combinations**, not permutations → [1,2] and [2,1] are the same
- To avoid duplicates: iterate **coins in outer loop**, amount in inner loop

**Pattern:**

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

**Approach: DFS + Memoization**

1. Create memo: `memo = {}` or 2D array
2. Define `dfs(i, remaining)` → ways to make `remaining` using `coins[i:]`

   **Base Cases:**
   - `remaining == 0` → return `1` (found valid combination)
   - `remaining < 0` or `i >= len(coins)` → return `0`
   - `(i, remaining) in memo` → return cached result

   **Recursion (skip OR use):**
   - `skip = dfs(i + 1, remaining)` → skip this coin
   - `use = dfs(i, remaining - coins[i])` → use this coin (stay at `i`, can reuse)
   - `memo[(i, remaining)] = skip + use`

3. Return `dfs(0, amount)`

```python
def dfs(i, remaining):
    if remaining == 0:
        return 1
    if remaining < 0 or i >= len(coins):
        return 0
    if (i, remaining) in memo:
        return memo[(i, remaining)]

    skip = dfs(i + 1, remaining)
    use = dfs(i, remaining - coins[i])  # stay at i (unbounded)
    memo[(i, remaining)] = skip + use
    return memo[(i, remaining)]
```

**Approach: 2D DP**

1. Init: `n = len(coins)`
2. Create 2D DP: `dp[n+1][amount+1]`
   - `dp[i][a]` = ways to make amount `a` using first `i` coins
3. **Base Case:** `dp[i][0] = 1` (1 way to make amount 0: use nothing)

```
            0   1   2   3   4   5
[]          1   0   0   0   0   0
[1]         1   1   1   1   1   1
[1,2]       1   1   2   2   3   3
[1,2,3]     1
```

4. **Transition:** For each coin `i`, for each amount `a`:

   - If `a >= coins[i-1]`: `dp[i][a] = dp[i-1][a] + dp[i][a - coins[i-1]]`
     - `dp[i-1][a]` = skip this coin
     - `dp[i][a - coins[i-1]]` = use this coin (can reuse, so same row)
   - Else: `dp[i][a] = dp[i-1][a]`

5. Return `dp[n][amount]`

**Approach: 1D DP**

1. Create 1D DP: `dp = [0] * (amount + 1)`
2. **Base Case:** `dp[0] = 1`

```
            0   1   2   3   4   5
            1   0   0   0   0   0
```

3. **Transition:** Iterate coins (outer), then amount (inner)

```python
for coin in coins:
    for a in range(coin, amount + 1):
        dp[a] = dp[a] + dp[a - coin]
```

4. Return `dp[amount]`


### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(c * a)

**Space Complexity:**
O(a)
