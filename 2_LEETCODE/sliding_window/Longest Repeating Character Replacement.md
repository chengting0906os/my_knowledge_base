# Longest Repeating Character Replacement

## Problem Description

You are given a string `s` consisting of only uppercase english characters and an integer `k`.

You can choose up to `k` characters of the string and replace them with any other uppercase English character.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.

## Examples

### Example 1

```text
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.
```

### Example 2

```text
Input: s = "AAABABB", k = 1
Output: 5
```

## Constraints

- `1 <= s.length <= 1000`
- `0 <= k <= s.length`
- `s` consists of uppercase english letters only

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Sliding Window

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. Create a hashmap to store character frequencies in the current sliding window, and track the maximum frequency.
2. Initalize `max_l = 0`,`l = 0`,`res=0`
3. Move the right pointer `r` across the string:
   - Update the frequency of s[r]
   - update `max_l` with the highest frequency seen so far
   - if `r - l + 1 - max_l > k`:
     - Shrink the window from the left and adjust counts.
       - `mp[s[l]] -= 1`
     - Move the left pointer forward
       - `l += 1`
   - Update res with the valid window size
4. `return res`

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
