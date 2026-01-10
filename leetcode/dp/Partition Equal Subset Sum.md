# Partition Equal Subset Sum

## Problem Description

You are given an array of positive integers `nums`.

Return `true` if you can partition the array into two subsets, `subset1` and `subset2` where `sum(subset1) == sum(subset2)`. Otherwise, return `false`.

## Examples

### Example 1

```text
Input: nums = [1,2,3,4]
Output: true
```

**Explanation:** The array can be partitioned as `[1, 4]` and `[2, 3]`.

### Example 2

```text
Input: nums = [1,2,3,4,5]
Output: false
```

## Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 50`

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**
- Equal partition means each subset sums to `total // 2`
- If total is odd → impossible to split evenly
- This is a 0/1 Knapsack problem: can we select items to reach exactly `target`?
- For each item: **skip** (don't include) or **take** (include in subset)
- If we take item, remaining sum `curr_sum - num` must be achievable from previous items

### M - Match

**Pattern:** Dynamic Programming (0/1 Knapsack) (Knapsack problem)

### P - Plan

**Top-Down DP Approach (Memoization):**

1. If `sum(nums)` is odd → return `False` (can't split evenly)
2. Set `target = sum(nums) // 2`
3. Create memo table: `memo[i][remaining]` = -1 (unvisited), 0 (False), 1 (True)
4. Define `dfs(i, remaining)` → returns True if we can make `remaining` using items from index `i` onwards

   **Base cases:**
   - `remaining == 0` → return `True` (found valid subset)
   - `i >= len(nums)` → return `False` (no more items to try)
   - `remaining < 0` → return `False` (exceeded target)
   - `memo[i][remaining] != -1` → return cached result

   **Recursion (skip OR take):**
   - `skip = dfs(i + 1, remaining)` → skip current item
   - `take = dfs(i + 1, remaining - nums[i])` → take current item
   - `memo[i][remaining] = skip or take`
   - return `memo[i][remaining]`

5. Return `dfs(0, target)`


**Bottom-Up DP Approach:**

1. If `sum(nums)` is odd → return `False` (can't split evenly)
2. Set `target = sum(nums) // 2`
3. Create 2D DP table: `dp[i][curr_sum]` = can we make `curr_sum` using first `i` items?

```
DP Table Structure (nums = [1, 5, 11, 5], target = 11):

        curr_sum →
          0   1   2   3   4  ...  11(target)
    [ ]   T   F   F   F   F       F
    [1]   T   T   F   F   F       F
    [5]   T   T   F   F   F       T
    [11]  T   T   F   F   F       T
    [5]   T   T   F   F   F       T
```

4. **Base case:** `dp[i][0] = True` (empty subset sums to 0)

5. **Transition:** For each item `nums[i-1]` and `curr_sum`:

   - If `nums[i-1] > curr_sum`: item too big → **skip only**
     - `dp[i][curr_sum] = dp[i-1][curr_sum]`
   - Else: **skip OR take**
     - `skip = dp[i-1][curr_sum]` → check if we already achieved `curr_sum` before
     - `take = dp[i-1][curr_sum - nums[i-1]]` → take this item, check remaining sum
     - `dp[i][curr_sum] = skip or take`

6. Return `dp[n][target]`

**Dynamic Programming (Optimal)**

### I - Implement

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
