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

- use `abs(n)`, If `n < 0` return `1 / res`
- return `1` while `n = 0`
- Exponent `n` repeatedly divided by 2 always ends with `1 → 0` (base case: `n == 0` returns `1`)

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Binary Exponentiation, DFS, iterative

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

**Base Case:** `n == 0` returns `1`

**DFS (Recursive)**

1. Create a helper function `dfs(base, exp)`:
   - **Base case:** if `exp == 0` return `1`
   - Recursively compute `half = dfs(base, exp // 2)`
   - If `exp % 2 == 0`: return `half * half`
   - Else: return `half * half * base`
2. Call `dfs(x, abs(n))`
3. Return `1 / res` if `n < 0` else `res`

**Iterative**

1. Edge case: if `x == 0` return `0`
2. Init variables:
   - `exponent = abs(n)`
   - `res = 1`
3. While `exponent > 0`:
   - If `exponent % 2 == 1`: `res *= x` # FISRT round and LAST round
   - `x *= x`
   - `exponent //= 2`
4. Return `1 / res` if `n < 0` else `res`

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
O(log n) - exponent repeatedly divided by 2
**Space Complexity:**
O(1)
