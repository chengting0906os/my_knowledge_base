# Merge Triplets to Form Target

## Problem Description

You are given a 2D array of integers `triplets`, where `triplets[i] = [ai, bi, ci]` represents the ith triplet. You are also given an array of integers `target = [x, y, z]` which is the triplet we want to obtain.

To obtain `target`, you may apply the following operation on triplets **zero or more times**:

- Choose two different triplets `triplets[i]` and `triplets[j]` and update `triplets[j]` to become `[max(ai, aj), max(bi, bj), max(ci, cj)]`.
  - E.g. if `triplets[i] = [1, 3, 1]` and `triplets[j] = [2, 1, 2]`, `triplets[j]` will be updated to `[max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2]`.

Return `true` if it is possible to obtain `target` as an element of triplets, or `false` otherwise.

## Examples

### Example 1

```text
Input: triplets = [[1,2,3],[7,1,1]], target = [7,2,3]
Output: true
```

**Explanation:** Choose the first and second triplets, update the second triplet to be `[max(1, 7), max(2, 1), max(3, 1)] = [7, 2, 3]`.

### Example 2

```text
Input: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]
Output: false
```

## Constraints

- `1 <= triplets.length <= 1000`
- `1 <= ai, bi, ci, x, y, z <= 100`

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

- `good = set()`
- For each triplet:
  - If any `t[i] > target[i]`: skip (max would exceed target)
  - Otherwise, for each position where `t[i] == target[i]`, add to `good`
- `return len(good) == 3`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
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
