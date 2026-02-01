# Partition Labels

## Problem Description

You are given a string `s` consisting of lowercase English letters.

We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

Return a list of integers representing the size of these substrings in the order they appear in the string.

## Examples

### Example 1

```text
Input: s = "xyxxyzbzbbisl"
Output: [5, 5, 1, 1, 1]
```

**Explanation:** The string can be split into `["xyxxy", "zbzbb", "i", "s", "l"]`.

### Example 2

```text
Input: s = "abcabc"
Output: [6]
```

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

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

- init
  - mp = {}
  - res = []
  - farthest = 0
  - first = 0
- traverse and record biggest idx of char using {}
- traverse and update farthest every step within substring
  - if i == farthest means it already reach this substring's end
    - append `farthest - first + 1` to res
    - update first to i + 1, which is next substring's start
- `return res`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
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
O(1)
