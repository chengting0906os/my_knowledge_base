# Search in Rotated Sorted Array

## Problem Description

You are given an array of length `n` which was originally sorted in ascending order. It has now been rotated between `1` and `n` times.

For example, the array `nums = [1,2,3,4,5,6]` might become:

- `[3,4,5,6,1,2]` if it was rotated 4 times
- `[1,2,3,4,5,6]` if it was rotated 6 times

Given the rotated sorted array `nums` and an integer `target`, return the index of `target` within `nums`, or `-1` if it is not present.

You may assume all elements in the sorted rotated array `nums` are unique.

> A solution that runs in O(n) time is trivial, can you write an algorithm that runs in **O(log n)** time?

## Examples

### Example 1

```text
Input: nums = [3,4,5,6,1,2], target = 1
Output: 4
```

### Example 2

```text
Input: nums = [3,5,6,0,1,2], target = 4
Output: -1
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique
- `nums` is an ascending array that is possibly rotated

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Binary Search

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

```python
nums = [5,6,7,8,1,2,3,4], target = 1
```

1. if nums[mid] == target return nums[mid]

2. At each step, identify which half is sorted, then check if target falls within that sorted range to decide which half to eliminate.

```python
# check which half is sorted
if nums[l] <= nums[mid]:
    # left half is sorted
    if nums[l] <= target < nums[mid]:
        r = mid - 1
    else:
        l = mid + 1

elif nums[l] > nums[mid]:
    # right half is sorted
    if nums[mid] < target <= nums[r]:
        l = mid + 1
    else:
        r = mid - 1
```

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
