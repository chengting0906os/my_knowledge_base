# Permutation in String

## Problem Description

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

That means if a permutation of `s1` exists as a substring of `s2`, then return `true`.

Both strings only contain lowercase letters.

## Examples

### Example 1

```text
Input: s1 = "abc", s2 = "lecabee"
Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".
```

### Example 2

```text
Input: s1 = "abc", s2 = "lecaabee"
Output: false
```

## Constraints

- `1 <= s1.length, s2.length <= 1000`
- `s1` and `s2` consist of lowercase English letters

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

1. Edge case: if `len(s1) > len(s2)`, return `False`
2. Build two frequency arrays of size 26 (one per lowercase letter):
   - `need[i]`   = count of character `i` in `s1`
   - `window[i]` = count of character `i` in the current window of `s2`
3. Initialize the first window `s2[0 : len(s1)]` and fill both arrays simultaneously
   - `l = 0`, `r = len(s1)`
4. Check initial window: if `need == window`, return `True`
5. Slide the window from index `r` to `len(s2) - 1`:
   - Add `s2[r]` to window (right expand)
   - Remove `s2[l]` from window (left shrink), then `l += 1`
   - If `need == window`, return `True`
6. Return `False` if no match found

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
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
O(1) # fixed-size array (26 characters)