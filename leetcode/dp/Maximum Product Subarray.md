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

**Test Cases:**

**Edge Cases:**

**Key Observations:**

- Need to track both `min_product` and `max_product` at each iteration, because multiplying by a negative number can flip min to max

### M - Match

**Pattern:** DP

### P - Plan

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

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pass
```

### R - Review

- Remember to save `max_product` in a temp variable before updating, because `min_product` calculation needs the original `max_product` value

### E - Evaluate

**Time Complexity:**
O(n)

**Space Complexity:**
O(1)
