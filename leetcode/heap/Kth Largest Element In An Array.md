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

**Test Cases:**

**Edge Cases:**

**Key Observations:**

### M - Match

**Pattern:** Min Heap / Quick Select

### P - Plan

### I - Implement

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
