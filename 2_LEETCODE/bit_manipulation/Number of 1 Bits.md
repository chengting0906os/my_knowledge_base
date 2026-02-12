# Number of 1 Bits

## Problem Description

You are given an unsigned integer `n`. Return the number of `1` bits in its binary representation.

You may assume `n` is a non-negative integer that fits within 32 bits.

## Examples

### Example 1

```text
Input: n = 00000000000000000000000000010111
Output: 4
```

### Example 2

```text
Input: n = 01111111111111111111111111111101
Output: 30
```

## Constraints

- `0 <= n <= 2^32 - 1`

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

1. Init `count=0`
2. while n > 0, add the last bit to count: count += (n&1), then right shit n by 1
3. Return `count`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(1) fixed to 32 bits

**Space Complexity:**
O(1)
