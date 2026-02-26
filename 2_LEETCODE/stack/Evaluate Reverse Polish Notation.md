# Evaluate Reverse Polish Notation

## Problem Description

You are given an array of strings `tokens` that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

- The operands may be integers or the results of other operations.
- The operators include `'+'`, `'-'`, `'*'`, and `'/'`.
- Assume that division between integers always truncates toward zero.

## Examples

### Example 1

```text
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
```

## Constraints

- `1 <= tokens.length <= 1000`
- `tokens[i]` is `'+'`, `'-'`, `'*'`, or `'/'`, or a string representing an integer in the range `[-100, 100]`.

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

**Approach: Stack**

1. Initialize `stack = deque()`
2. traverse token:
   - `if t not in ("+", "-", "*", "/")`
     - `stack.append(int(t))`
   - else:
     - pop num as `num_2`
     - pop num as `num_1`
     - if ` t == "+"`:
       - `stack.append(num_1+num_2)`
     - elif `t == "-"`:
       - `stack.append(num_1-num_2)`
     - elif `t == "*"`:
       - `stack.append(num_1*num_2)`
     - elif `t == `/`:
       - `stack.append(int(num_1/num_2))`
3. `return stack[-1]`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def evalRPN(self, tokens) -> int:
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
