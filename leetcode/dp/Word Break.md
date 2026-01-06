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

**Test Cases:**

**Edge Cases:**

**Key Observations:**

### M - Match

**Pattern:** DP

### P - Plan

### I - Implement

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
