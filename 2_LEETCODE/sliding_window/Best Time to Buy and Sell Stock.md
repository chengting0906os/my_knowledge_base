# Best Time to Buy and Sell Stock

## Problem Description

You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on the `i`th day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be `0`.

## Examples

### Example 1

```text
Input: prices = [10,1,5,6,7,1]
Output: 6
```

Explanation: Buy `prices[1]` and sell `prices[4]`, profit = 7 - 1 = 6.

### Example 2

```text
Input: prices = [10,8,7,5,2]
Output: 0
```

Explanation: No profitable transactions can be made, thus the max profit is 0.

## Constraints

- `1 <= prices.length <= 100`
- `0 <= prices[i] <= 100`

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
>   **Approach: Sliding Window (Two Pointers)**

1. Left pointer = buy day, right pointer = sell day (starts one step ahead).
2. Walk through the array. If sell price > buy price, calculate profit and track the max.
3. If sell price <= buy price, reset left to right (found a new minimum buy price).
4. Always move right forward.
5. Return the max profit.

**Approach: DP**

1. Init:
   - max_p = 0
   - min_buy = prices[0]
2. traverse from 1
   - max_p = max(max_p, prices[i] - min_buy)
   - min_buy = min(min_buy, prices[i])
3. return max_p

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
