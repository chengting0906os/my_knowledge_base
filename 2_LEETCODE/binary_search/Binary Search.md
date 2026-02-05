# Binary Search

## Problem Description

You are given an array of distinct integers `nums`, sorted in ascending order, and an integer `target`.

Implement a function to search for `target` within `nums`. If it exists, return its index. Otherwise, return `-1`.

Your solution must run in `O(log n)` time.

## Examples

### Example 1

```text
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3
```

### Example 2

```text
Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1
```

## Constraints

- `1 <= nums.length <= 10000`
- `-10000 < nums[i], target < 10000`
- All the integers in `nums` are unique.

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

1. Init left pointer and right pointer
   - l = 0
   - r = len(nums) - 1
2. loop while l <= r (we need to check l==r)
   - mid = l + (r-l) // 2
   - if nums[mid] > target:
     r -= 1
   - elif nums[mid] < target:
   - else return mid
3. return -1

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
