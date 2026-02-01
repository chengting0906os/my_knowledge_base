# Word Break

## Problem Description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

## Examples

### Example 1

```text
Input: s = "neetcode", wordDict = ["neet","code"]
Output: true
```

**Explanation:** Return true because "neetcode" can be split into "neet" and "code".

### Example 2

```text
Input: s = "applepenapple", wordDict = ["apple","pen","ape"]
Output: true
```

**Explanation:** Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

### Example 3

```text
Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
Output: false
```

## Constraints

- `1 <= s.length <= 200`
- `1 <= wordDict.length <= 100`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** DP

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

- Top-Down
Approach: start from the beginning and try each dictionary word as the next segment; if any path reaches the end, return True. To avoid repeated work, use memo to record whether each index is segmentable.

1. `memo = {len(s): True}` (base case: empty suffix is breakable)

2. `dfs(i)` returns whether `s[i:]` can be segmented
```text
def dfs(i):
    # if i reaches the end (memo[len(s)] = True), return True
    # iterate wordDict and try each word from position i
    # if s[i:i+len(word)] matches, recurse on dfs(i + len(word))
    # if any recursion is True, memo[i] = True; otherwise memo[i] = False
```
3. return `dfs(0)`

- Bottom-Up

1. create `dp = [False] * (len(s) + 1)`
2. `dp[len(s)] = True` (empty suffix is breakable)
3. iterate `i` from the end to the start; for each word:
   - if `s[i:i+len(word)]` matches, set `dp[i] = dp[i+len(word)]`
   - if `dp[i]` becomes True, break the inner loop (no need to try more words)
4. return `dp[0]`


### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

Remember to break early when `dp[i]` becomes True in the bottom-up method.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

n = len(s)
m = len(wordDict)
t = max word length

**Time Complexity:**
O(n*m*t)

**Space Complexity:**
O(n)
