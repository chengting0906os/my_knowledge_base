# Maximum Subarray

## Problem Description

Given an array of integers `nums`, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

### Example 1

```text
Input: nums = [2,-3,4,-2,2,1,-1,4]
Output: 8
```

**Explanation:** The subarray `[4,-2,2,1,-1,4]` has the largest sum 8.

### Example 2

```text
Input: nums = [-1]
Output: -1
```

## Constraints

- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`

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

"""
            1   2   3   4
cur_sum
max_sum
"""

1. init
    - cur_sum = float('-inf')
    - max_sum = float('-inf')

2. traverse each num (Kadane's Algorithm)
   - at each step, decide: extend previous subarray or start fresh from here
     - cur_sum = max(cur_sum + nums[i], nums[i])
   - update global max after each decision
     - max_sum = max(max_sum, cur_sum)

3. return max_sum




### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
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
