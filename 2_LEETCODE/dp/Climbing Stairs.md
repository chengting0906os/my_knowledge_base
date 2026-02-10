# Climbing Stairs

## Problem Description

You are given an integer `n` representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

## Examples

### Example 1

```text
Input: n = 2
Output: 2
```

**Explanation:**

- 1 + 1 = 2
- 2 = 2

### Example 2

```text
Input: n = 3
Output: 3
```

**Explanation:**

- 1 + 1 + 1 = 3
- 1 + 2 = 3
- 2 + 1 = 3

## Constraints

- `1 <= n <= 30`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Edge case: n = 1 → return 1

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

- **Pattern:** DP

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. Base case: if n <= 2, return n
2. Init two variables:
   - one = 1 (ways to reach step 1)
   - two = 2 (ways to reach step 2)
3. Traverse from step 3 to n:
   - temp = one + two
   - shift: one = two, two = temp
4. Return two

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def climbStairs(self, n: int) -> int:
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
O(1) — only need two variables
