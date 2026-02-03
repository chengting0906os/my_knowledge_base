# Contains Duplicate

## Problem Description

Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

## Examples

### Example 1

```text
Input: nums = [1, 2, 3, 3]
Output: true
```

### Example 2

```text
Input: nums = [1, 2, 3, 4]
Output: false
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

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

1. Init
   - `bucket = set()`
2. For each element, check then append
   - If element already in bucket, return `True`
   - Add element to bucket
3. Return `False` at the end

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
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
O(n)
