# Palindrome Partitioning

## Problem Description

Given a string `s`, split `s` into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

## Examples

### Example 1

```text
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

### Example 2

```text
Input: s = "a"
Output: [["a"]]
```

### Constraints

- `1 <= s.length <= 20`
- `s` contains only lowercase English letters.

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

1. Create a helper function `is_pali` to check whether `s[l:r+1]` is a palindrome.
2. Init `res` list and `part` list. `part` is to store palindromes temporarily.
3. Create a dfs inner function with left and right pointers.
   - Base case: if r >= len(s):
     - if l == r: all characters are partitioned → append part[:] to res
     - return
   - if s[l:r+1] is palindrome:
     - Pick: append s[l:r+1] to part
     - Explore next partition: dfs(r+1, r+1)
     - Backtrack: part.pop()
   - Try a longer substring: dfs(l, r+1)

4. dfs(0, 0)
5. return res

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O()

- There `n-1` gaps -> 2^(n-1) possible ways to partition.
- For each partition, checking palindrome takes O(n).

**Space Complexity:**
O(n) extra space

- recursion stack depth is at most n. and `part` list holds most `n` substrings
  O(n \* 2^n) for the output
- store all partition in `res`
