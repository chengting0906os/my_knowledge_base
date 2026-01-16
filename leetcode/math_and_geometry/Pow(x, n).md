# Pow(x, n)

## Problem Description

Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).

Given a floating-point value `x` and an integer value `n`, implement the `myPow(x, n)` function, which calculates x raised to the power n.

You may not use any built-in library functions.

## Examples

### Example 1

```text
Input: x = 2.00000, n = 5
Output: 32.00000
```

### Example 2

```text
Input: x = 1.10000, n = 10
Output: 2.59374
```

### Example 3

```text
Input: x = 2.00000, n = -3
Output: 0.12500
```

## Constraints

- `-100.0 < x < 100.0`
- `-1000 <= n <= 1000`
- `n` is an integer
- If `x = 0`, then `n` will be positive

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Binary Exponentiation

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

- DFS

- BFS 

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
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
