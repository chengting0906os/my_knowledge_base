# Letter Combinations of a Phone Number

## Problem Description

You are given a string `digits` made up of digits from `2` through `9` inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

| Digit | Letters |
|-------|---------|
| 2     | abc     |
| 3     | def     |
| 4     | ghi     |
| 5     | jkl     |
| 6     | mno     |
| 7     | pqrs    |
| 8     | tuv     |
| 9     | wxyz    |

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that `digits` could represent. You may return the answer in any order.

## Examples

### Example 1

```text
Input: digits = "34"
Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
```

### Example 2

```text
Input: digits = ""
Output: []
```

### Constraints

- `0 <= digits.length <= 4`
- `2 <= digits[i] <= 9`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Empty string → return `[]`

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Backtracking

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

**Approach: Backtracking**
1. Edge case: if not digits, return [].
2. Create a map to store digit-to-letters pairs.
3. Init `res` list and `n = len(digits)`.
4. Create a backtracking function with index `i` and current string `sub_str`.
   - Base case: if i == n → res.append(sub_str), return
   - For each char in mp[digits[i]]: backtrack(i + 1, sub_str + char)

5. backtrack(0, "")
6. return res

**Approach: Iteration**
1. Edge case: if not digits, return [].
2. Create a map to store digit-to-letters pairs.
3. Init `res` = [""] and `n = len(digits)`.
4. for digit in digits:
    - create a `tmp = []`
    - for cur_str in res:
        - for char in mp[digit]:
            - tmp.append(cur_str + char)
    - res = tmp
5. return res



### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
