# Coin Change

## Problem Description

You are given an integer array `coins` representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer `amount` representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return `-1`.

You may assume that you have an **unlimited number** of each coin.

## Examples

### Example 1

```text
Input: coins = [1,5,10], amount = 12
Output: 3
```

**Explanation:** 12 = 10 + 1 + 1. Note that we do not have to use every kind of coin available.

### Example 2

```text
Input: coins = [2], amount = 3
Output: -1
```

**Explanation:** The amount of 3 cannot be made up with coins of 2.

### Example 3

```text
Input: coins = [1], amount = 0
Output: 0
```

**Explanation:** Choosing 0 coins is a valid way to make up 0.

## Constraints

- `1 <= coins.length <= 10`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10000`

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**

### M - Match

**Pattern:** Dynamic Programming (Unbounded Knapsack)

### P - Plan

- DP

1. Create dp array where `dp[i]` = min coins needed to make amount `i`

```python
dp = [float('inf')] * (amount + 1)
dp[0] = 0  # base case: 0 coins needed to make amount 0
```

2. For each amount `i`, try using each coin `c`: take min of current `dp[i]` vs using coin `c` (which is `1 + dp[i - c]`)

```python
for i in range(1, amount + 1):
    for c in coins:
        if i - c >= 0:
            dp[i] = min(dp[i], 1 + dp[i - c])
```

3. Return result (check if amount is reachable)

```python
return dp[amount] if dp[amount] != float('inf') else -1
```

### I - Implement

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**
O(c*amount)

**Space Complexity:**
O(amount)