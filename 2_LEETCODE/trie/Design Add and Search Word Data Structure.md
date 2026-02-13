# Design Add and Search Word Data Structure

## Problem Description

Design a data structure that supports adding new words and searching for existing words.

Implement the `WordDictionary` class:

- `addWord(word)` Adds word to the data structure.
- `search(word)` Returns `True` if there is any string in the data structure that matches `word` or `False` otherwise. `word` may contain dots `.` where dots can be matched with any letter.

## Examples

### Example 1

```text
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["day"],["bay"],["may"],["say"],["day"],[".ay"],["b.."]]

Output:
[null, null, null, null, false, true, true, true]
```

```python
wordDictionary = WordDictionary()
wordDictionary.addWord("day")
wordDictionary.addWord("bay")
wordDictionary.addWord("may")
wordDictionary.search("say")  # False
wordDictionary.search("day")  # True
wordDictionary.search(".ay")  # True
wordDictionary.search("b..")  # True
```

## Constraints

- `1 <= word.length <= 20`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consists of `.` or lowercase English letters.
- There will be at most 2 dots in `word` for search queries.
- At most 10,000 calls will be made to `addWord` and `search`.

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Trie + DFS / Backtracking

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

- Create a `TrieNode` class with attributes `children = {}` and `is_word = False`.
- Initialize `WordDictionary` with `self.root = TrieNode()`.
- Create a `dfs` function inside `search` to handle `.` wildcards.
- Return with `return dfs(0, self.root)`.
- DFS flow: start from `root` and walk the word from index `i`. If the current char is `.`, try every child and succeed if any path works. If it is a letter, follow that child or fail if missing. When all characters are consumed, return whether the current node marks a word end.


### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
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
