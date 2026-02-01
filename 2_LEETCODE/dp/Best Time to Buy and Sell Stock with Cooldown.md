# Best Time to Buy and Sell Stock with Cooldown

## Problem Description

You are given an integer array `prices` where `prices[i]` is the price of a stock on the `i`th day.

You may buy and sell one stock multiple times with the following restrictions:

- After you sell your stock, you cannot buy another one on the next day (i.e., there is a **cooldown period of one day**).
- You may only own **at most one stock** at a time.
- You may complete as many transactions as you like.

Return the **maximum profit** you can achieve.

## Examples

### Example 1

```text
Input: prices = [1,3,4,0,4]
Output: 6
```

**Explanation:**

- Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 2
- Cooldown on day 2
- Buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4
- Total profit = 2 + 4 = 6

### Example 2

```text
Input: prices = [1]
Output: 0
```

## Constraints

- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

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

**Approach: bottom-up**

**State Machine with 3 states:**

- `hold`: max profit when **holding** a stock (bought but not yet sold)
- `sell`: max profit on the day we **just sold** (triggers cooldown tomorrow)
- `cool`: max profit when in **cooldown** or idle (not holding, free to buy)

**Initial values:**

- `hold = -prices[0]` → bought on day 0
- `sell = 0` → haven't sold anything yet
- `cool = 0` → no action taken

```python
for i in range(1, len(prices)):
    prev_hold = hold
    prev_sell = sell
    prev_cool = cool


    # hold = accumulated profit - buy cost (if had profit before, profit base increases)
    # must buy from prev_cool (cooldown rule: can't buy right after selling)
    hold = max(prev_cool - prices[i], prev_hold)
    sell = prev_hold + prices[i] # sell today = prev hold + today's price (stock bought sometime before today)
    cool = max(prev_sell, prev_cool) # idle today = max(forced cooldown after sell, keep waiting)
```

- `return max(sell, cool)`
  - `sell`: best profit if selling on last day
  - `cool`: best profit if already sold before, waiting until last day
  - must not hold stock on last day, so only compare these two states

```
prices = [3, 6, 1, 2, 9]

Day     1       2       3       4       5
price   3       6       1       2       9
───────────────────────────────────────────
hold   -3      -3       2       2       2
sell    0       3      -2       4      11
cool    0       0       3       3       4

# Day 3: prev_cool (3) > prev_sell (-2), cool comes from "keep waiting"
# Day 4: sell = 2+2 = 4, cool = max(-2,3) = 3
# Day 5: sell = 2+9 = 11 → best path: buy D1→sell D2→buy D3→sell D5
```

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
O(n)

**Space Complexity:**
O(1)
