# Non-Cyclical Number (Happy Number)

## Problem Description

A non-cyclical number is defined by the following algorithm:

1. Given a positive integer, replace it with the sum of the squares of its digits.
2. Repeat until the number equals `1`, or it loops infinitely in a cycle which does not include `1`.
3. If it stops at `1`, return `true`. Otherwise, return `false`.

## Examples

### Example 1

```text
Input: n = 100
Output: true
```

**Explanation:** 1² + 0² + 0² = 1

### Example 2

```text
Input: n = 101
Output: false
```

**Explanation:**

- 1² + 0² + 1² = 2
- 2² = 4
- 4² = 16
- 1² + 6² = 37
- 3² + 7² = 58
- 5² + 8² = 89
- 8² + 9² = 145
- 1² + 4² + 5² = 42
- 4² + 2² = 20
- 2² + 0² = 4 (cycle detected)

## Constraints

- `1 <= n <= 1000`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- We need to detect a cycle — if we see a number we've already visited, return false
- n = 1 → return true

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

- **Pattern:** Hash Set (cycle detection) or Floyd's Fast/Slow Pointers

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

**Approach Space O(n)**

1. Create func:

```python
def sum_of_square(self, n):
    res = 0
    while n:
        rem = n % 10
        res += rem * rem
        n = n // 10

    return res
```

2. create a bucket set()
3. bucket.add(n)
4. while True:
   - num = self.sum_of_square(n)
   - if num == 1: return True
   - if num in bucket: return False
   - bucket.add(n)
   - n = num

**Approach Space O(1)**

1. Same as above
2. Init:
   - slow: n
   - fast: self.sum_of_square(n)
3. while slow != fast:
   - fast = self.sum_of_square(fast)
   - fast = self.sum_of_square(fast)
   - slow = self.sum_of_square(slow)
4. return fast == 1

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(log n) — per step, digits reduce; cycle is bounded

**Space Complexity:**
O(log n) — hash set approach / O(1) — fast/slow pointers
