# Longest Repeating Character Replacement

## Problem Description

You are given a string `s` consisting of only uppercase English characters and an integer `k`.

You can choose up to `k` characters in `s` and replace each of them with any uppercase English character.

Return the length of the longest substring that can be turned into a string with only one distinct character after at most `k` replacements.

## Examples

### Example 1

```text
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the two 'X' with 'Y', or the two 'Y' with 'X'.
```

### Example 2

```text
Input: s = "AAABABB", k = 1
Output: 5
```

## Constraints

- `1 <= s.length <= 1000`
- `0 <= k <= s.length`
- `s` consists of uppercase English letters only

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
    def characterReplacement(self, s: str, k: int) -> int:
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
