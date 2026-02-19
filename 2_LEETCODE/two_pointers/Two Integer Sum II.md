# Two Integer Sum II

## Problem Description

Given an array of integers `numbers` that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, `[index1, index2]`, such that they add up to a given target number `target` and `index1 < index2`.

Note that `index1` and `index2` cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use `O(1)` additional space.

## Examples

### Example 1

```text
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
```

## Constraints

- `2 <= numbers.length <= 1000`
- `-1000 <= numbers[i] <= 1000`
- `-1000 <= target <= 1000`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Return the indices (1-indexed) of two numbers

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** two pointers

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. Initialize two pointers:
   - `l = 0`(start)
   - `r = len(numbers) - 1`(end)
2. while `l < r`:
   - Computer `numbers[l] + numbers[r]`
   - if > target: `r -= 1`
   - if < target `l += 1`
   - if == target: `return [l+1, r+1]`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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
