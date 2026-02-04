# Valid Palindrome

## Problem Description

Given a string `s`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

## Examples

### Example 1

```text
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
```

### Example 2

```text
Input: s = "tab a cat"
Output: false
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists only of printable ASCII characters

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

**Approach: Clean First**

1. Clean string: keep only alphanumeric, convert to lowercase
2. Two pointers from both ends, compare and move inward
3. If mismatch found → return False, else → return True

**Approach: Skip In-place (O(1) space)**

1. Two pointers from both ends
2. Skip non-alphanumeric chars while moving
3. Compare (case-insensitive), if mismatch → False
4. Return True

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
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
O(n) or O(1)
