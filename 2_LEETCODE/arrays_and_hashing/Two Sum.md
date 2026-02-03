# Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition.

Return the answer with the smaller index first.

## Examples

### Example 1

```text
Input: nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
```

### Example 2

```text
Input: nums = [4,5,6], target = 10
Output: [0,2]
```

### Example 3

```text
Input: nums = [5,5], target = 10
Output: [0,1]
```

## Constraints

- `2 <= nums.length <= 1000`
- `-10,000,000 <= nums[i] <= 10,000,000`
- `-10,000,000 <= target <= 10,000,000`
- Only one valid answer exists.

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
   - `mp = {}` (value -> index)
2. Traverse with enumerate `(i, n)`
   - If `target - n` in `mp`, return `[mp[target - n], i]`
   - Else `mp[n] = i`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
