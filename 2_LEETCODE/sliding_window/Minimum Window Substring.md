# Minimum Window Substring

## Problem Description

Given two strings `s` and `t`, return the shortest substring of `s` such that every character in `t`, including duplicates, is present in the substring.

If such a substring does not exist, return an empty string `""`.

You may assume that the correct output is always unique.

## Examples

### Example 1

```text
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.
```

### Example 2

```text
Input: s = "xyz", t = "xyz"
Output: "xyz"
```

### Example 3

```text
Input: s = "x", t = "xy"
Output: ""
```

## Constraints

- `1 <= s.length <= 1000`
- `1 <= t.length <= 1000`
- `s` and `t` consist of uppercase and lowercase English letters

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Sliding Window + Hash Map

### P - Plan

1. Initialize two hash maps:
   - `count`: frequency of characters in `t`
   - `window`: frequency of characters in the current window of `s`
2. Initialize pointers and trackers:
   - `have = 0`
   - `need = len(count)` (number of distinct required characters)
   - `res = (float("inf"), 0)` (best window length, start index)
   - `l = 0`
3. Traverse `s` with right pointer `r`:
   - Add `s[r]` to `window`
   - If `s[r]` is required and now matches the target count, increment `have`
4. When `have == need`, shrink from the left:
   - Update `res` if current window is shorter
   - Remove `s[l]` from `window`
   - If `s[l]` is required and falls below target count, decrement `have`
   - Move `l += 1`
5. Return result:
   - If no valid window was found, return `""`
   - Otherwise return the substring using `res`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        pass
```

### R - Review

### E - Evaluate
