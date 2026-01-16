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

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Equal partition means each subset sums to `total // 2`
- If total is odd → impossible to split evenly
- This is a 0/1 Knapsack problem: can we select items to reach exactly `target`?
- For each item: **skip** (don't include) or **take** (include in subset)
- If we take item, remaining sum `curr_sum - num` must be achievable from previous items

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Dynamic Programming (0/1 Knapsack) (Knapsack problem)

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

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

**Dynamic Programming (Space Optimized - 1D Array)**

1. If `sum(nums)` is odd → return `False` (can't split evenly)
2. Set `target = sum(nums) // 2`
3. Create 1D DP array: `dp = [False] * (target + 1)`
4. **Base Case:** `dp[0] = True` (empty subset sums to 0)

5. **Transition:** For each `num` in `nums`:

   - Iterate **backwards** from `target` down to `num`
   - `dp[s] = dp[s] OR dp[s - num]`
     - `dp[s]` = skip (already achievable without current num)
     - `dp[s - num]` = take (achievable if remaining sum was achievable)

   ```
   for num in nums:
       for s in range(target, num - 1, -1):  # backwards!
           dp[s] = dp[s] or dp[s - num]
   ```

6. Return `dp[target]`

**Alternative: Forward iteration with copy**

Instead of iterating backwards, copy the array each round:

```python
for num in nums:
    next_dp = dp[:]                      # copy previous round
    for s in range(num, target + 1):
        next_dp[s] = next_dp[s] or dp[s - num]
    dp = next_dp
```

- `dp[s - num]` reads from **previous round** → no double-counting
- Trade-off: O(target) extra copy per iteration vs. backwards trick

**Why These Approaches Work (Avoiding Double-Counting)**

In 0/1 Knapsack, each item can only be used **once**. The key is ensuring `dp[s - num]` reads from the **previous round** (before considering current item).

| Approach            | How it ensures previous round                       |
| ------------------- | --------------------------------------------------- |
| Backwards iteration | `dp[s - num]` hasn't been updated yet in this round |
| Forward with copy   | `dp[s - num]` reads from original array             |

**Example of forward iteration WITHOUT copy (WRONG):**

`nums = [1, 2, 3]`, `target = 3`, processing `num = 1`:

```
Initial: dp = [T, F, F, F]

dp[1] = dp[1] OR dp[0] = T    →  dp = [T, T, F, F]
dp[2] = dp[2] OR dp[1] = T    →  dp = [T, T, T, F]  ← dp[1] was just updated!
dp[3] = dp[3] OR dp[2] = T    →  dp = [T, T, T, T]  ← Used 1 three times!
```

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(n\*target)

**Space Complexity:**
O(target)
