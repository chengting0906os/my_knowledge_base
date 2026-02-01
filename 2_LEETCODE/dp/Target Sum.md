# Target Sum

## Problem Description

You are given an array of integers `nums` and an integer `target`.

For each number in the array, you can choose to either **add** or **subtract** it to a total sum.

- For example, if `nums = [1, 2]`, one possible sum would be `"+1-2=-1"`.
- If `nums = [1, 1]`, there are two different ways to sum the input numbers to get a sum of `0`: `"+1-1"` and `"-1+1"`.

Return the number of different ways that you can build the expression such that the total sum equals `target`.

## Examples

### Example 1

```text
Input: nums = [2,2,2], target = 2
Output: 3
```

**Explanation:** There are 3 different ways to sum the input numbers to get a sum of 2.

- `+2 +2 -2 = 2`
- `+2 -2 +2 = 2`
- `-2 +2 +2 = 2`

## Constraints

- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `-1000 <= target <= 1000`

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

- [2,2,2]
- you need to use last dict and don't update it in this round
- dp = [defautdict(int) for _ in range(len(nums)+1)]
- dp[0][0] = 1
-

```
for i in range(1, len(nums)+1):
    num = nums[i-1]
    for s, count in dp[i-1].items()
        dp[i][s-num] += count
        dp[i][s+num] += count

    return dp[-1][target]
```

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

- If you don't use `defaultdict(int)`, use `dp[i].get(s - num, 0)` and `dp[i].get(s + num, 0)`; otherwise you might hit a `KeyError`.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(n)

**Space Complexity:**
O(1)
