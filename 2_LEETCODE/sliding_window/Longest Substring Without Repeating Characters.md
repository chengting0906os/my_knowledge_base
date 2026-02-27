# Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

## Examples

### Example 1

```text
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.
```

### Example 2

```text
Input: s = "xxxx"
Output: 1
```

## Constraints

- `0 <= s.length <= 1000`
- `s` may consist of printable ASCII characters

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

**Approach: hash set**

1. Create an empty set `bucket` and two pointers:
   - `bucket = set()`
   - `l = 0`
   - `r = len(lengths) - 1`
2. `while r < len(s)`
   - `if s[r] not in bucket`
     - `bucket.add(s[r])`
     - `res = max(res, len(bucket))`
     - `r += 1`
   - else:
     - `bucket.remove(s[l])`
     - `l += 1`
3. `return res`

**Approach: hash map**

1. Create an empty map `mp` with two pointers
   - `mp = defaultdict(int)`
   - `l = 0`
   - `r = 0`
2. `while r < len(s):`
   if s[l] in mp:
   - `l = max(l, mp[s[l]])`
3. For each round:
   - `mp[s[r]] = r` # update every step
   - `res = max(res, r-l+1)` # update every step
   - `r += 1` # move forward
4. `return res`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
O(m) where m is the total number of unique characters in the string
