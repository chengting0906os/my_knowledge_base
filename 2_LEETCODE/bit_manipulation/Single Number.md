# Single Number

## Problem Description

You are given a non-empty array of integers `nums`. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with `O(n)` runtime complexity and use only `O(1)` extra space.

## Examples

### Example 1

```text
Input: nums = [3,2,3]
Output: 2
```

### Example 2

```text
Input: nums = [7,6,6,7,8]
Output: 8
```

## Constraints

- `1 <= nums.length <= 10000`
- `-10000 <= nums[i] <= 10000`

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

1. Init res = 0
2. Iterate through `nums`, and for each number do `res ^= num`
3. return res

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
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
