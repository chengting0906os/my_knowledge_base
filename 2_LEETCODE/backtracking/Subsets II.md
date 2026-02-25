# Subsets II

## Problem Description

You are given an array `nums` of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

## Examples

### Example 1

```text
Input: nums = [1,2,1]
Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
```

### Example 2

```text
Input: nums = [7,7]
Output: [[],[7],[7,7]]
```

## Constraints

- `1 <= nums.length <= 11`
- `-20 <= nums[i] <= 20`

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

**Approach: Backtracking(While Loop)**

1. Init:
   - res = []
   - n = len(nums)
   - nums.sort()
2. def backtrack(i, subset)
   - if i == n:
     res.append(subset[::])
     return
   - subset.append(nums[i]) # pick
   - backtrack(i + 1, subset)
   - subset.pop() # not pick
   - while i + 1 less than n and nums[i + 1] == nums[i]:
     i += 1
   - backtrack(i + 1, subset)
3. backtrack(0, [])
4. return res

### I - Implement

**Approach: Backtracking(For Loop)**

1. Init:
   - res = []
   - n = len(nums)
   - nums.sort()
2. def backtrack(i, subset)
    - res.append(subset[::])
    - travser from i to n, idx j
        - if j > i and nums[j] == nums[j-1]: continue # don't skip first time and skip if equal
        - subset.append(nums[i])
        - backtrack(j+1, subset)
        - subset.pop()
    

3. backtrack(0, [])
4. return res

**Approach: Iteration**
1. Init:
    - nums.sort()
    - res = [[]]
    - pre_idx = 0
    - idx = 0
2. For each index i
    - if i > 0 and nums[i] == nums[i-1]
        - pre_idx = idx  # only extend subsets added in previous round
      else
        - pre_idx = 0
    - idx = len(res)  # snapshot before appending new subsets
    - traverse j from pre_idx to idx - 1
        - res.append(res[j] + [nums[i]])
3. return res


> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
extra: O(n) or O(1)
output: O(2^n)
