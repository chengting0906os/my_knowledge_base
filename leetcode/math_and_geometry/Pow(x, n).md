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

**Test Cases:**

**Edge Cases:**

**Key Observations:**

### M - Match

**Pattern:** Binary Exponentiation

### P - Plan
- DFS

- BFS 

### I - Implement

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
