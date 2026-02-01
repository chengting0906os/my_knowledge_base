# Kth Largest Element in an Array

## Problem Description

Given an unsorted array of integers `nums` and an integer `k`, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

> **Follow-up:** Can you solve it without sorting?

## Examples

### Example 1

```text
Input: nums = [2,3,1,5,4], k = 2
Output: 4
```

### Example 2

```text
Input: nums = [2,3,1,1,5,5,4], k = 3
Output: 4
```

## Constraints

- `1 <= k <= nums.length <= 10000`
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

**Pattern:** Min Heap / Quick Select

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
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
