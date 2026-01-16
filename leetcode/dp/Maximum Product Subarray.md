# Maximum Product Subarray

## Problem Description

Given an integer array `nums`, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

## Examples

### Example 1

```text
Input: nums = [1,2,-3,4]
Output: 4
```

### Example 2

```text
Input: nums = [-2,-1]
Output: 2
```

## Constraints

- `1 <= nums.length <= 1000`
- `-10 <= nums[i] <= 10`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Need to track both `min_product` and `max_product` at each iteration, because multiplying by a negative number can flip min to max

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** DP

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. init variable

```python
min_product = nums[0]
max_product = nums[0]
res = nums[0]
```

2. Iterate from second element

```python
for n in nums[1:]:
    tmp = n * max_product
    # update max_product
    # update min_product (using tmp)
    # update res with current max_product
```

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

- Remember to save `max_product` in a temp variable before updating, because `min_product` calculation needs the original `max_product` value

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(n)

**Space Complexity:**
O(1)
