# Valid Parenthesis String

## Problem Description

You are given a string `s` which contains only three types of characters: `'('`, `')'` and `'*'`.

Return `true` if `s` is valid, otherwise return `false`.

A string is valid if it follows all of the following rules:

- Every left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Every right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- A `'*'` could be treated as a right parenthesis `')'` character or a left parenthesis `'('` character, or as an empty string `""`.

## Examples

### Example 1

```text
Input: s = "((**)"
Output: true
```

**Explanation:** One of the `'*'` could be a `')'` and the other could be an empty string.

### Example 2

```text
Input: s = "(((*)"
Output: false
```

## Constraints

- `1 <= s.length <= 100`
- `s` consists of `'('`, `')'` and `'*'` only.

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

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
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
