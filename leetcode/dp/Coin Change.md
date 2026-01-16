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

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Dynamic Programming (Unbounded Knapsack)

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

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

- BFS (level-order traversal, first to reach 0 is the answer)

0. Edge case

```python
if amount == 0:
    return 0
```

1. Create deque with tuple (remaining_amount, steps)

```python
q = deque([(amount, 0)])  # (amount, step)
```

2. Create visited set to avoid revisiting same amount

```python
visited = set([amount])
```

3. BFS: pop from queue, try each coin, first to reach 0 wins

```python
while q:
    curr, step = q.popleft()
    for c in coins:
        nxt = curr - c
        if nxt == 0:
            return step + 1
        if nxt > 0 and nxt not in visited:
            q.append((nxt, step + 1))
            visited.add(nxt)
```

4. Return -1 if amount is not reachable

```python
return -1
```

- DFS with memoization (recursively try every coin, cache results)

1. Create memo dict with base case

```python
memo = {0: 0}  # 0 coins needed to make amount 0
```

2. Define DFS function

```python
def dfs(rem):
    if rem in memo:
        return memo[rem]

    res = float('inf')
    for c in coins:
        if rem - c >= 0:
            res = min(res, 1 + dfs(rem - c))

    memo[rem] = res
    return res
```

3. Call DFS and return result

```python
ans = dfs(amount)
return ans if ans != float('inf') else -1
```


### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(c*amount)

**Space Complexity:**
O(amount)
