# Products of Array Except Self

## Problem Description

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in `O(n)` time without using the division operation?

## Examples

### Example 1

```text
Input: nums = [1,2,4,6]
Output: [48,24,12,8]
```

### Example 2

```text
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
```

## Constraints

- `2 <= nums.length <= 1000`
- `-20 <= nums[i] <= 20`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer

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

1. (Fill in your high-level steps here)
2.
3.
4.
5.

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
