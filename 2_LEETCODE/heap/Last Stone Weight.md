# Last Stone Weight

## Problem Description

You are given an array of integers `stones` where `stones[i]` represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

1. At each step we choose the **two heaviest stones**, with weight `x` and `y` and smash them together
2. If `x == y`, both stones are destroyed
3. If `x < y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`

Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return `0` if none remain.

## Examples

### Example 1

```text
Input: stones = [2,3,6,2,4]
Output: 1
```

**Explanation:**

- Smash 6 and 4 → left with 2, array becomes `[2,3,2,2]`
- Smash 3 and 2 → left with 1, array becomes `[1,2,2]`
- Smash 2 and 2 → array becomes `[1]`

### Example 2

```text
Input: stones = [1,2]
Output: 1
```

## Constraints

- `1 <= stones.length <= 20`
- `1 <= stones[i] <= 100`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Max Heap

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. Edge case: if `not stones` return `0`
2. Negate all values: `stones = [-s for s in stones]`
3. implace `heapify`
4. While `len(stones) >= 2`:
   - Pop two largest (most negative)
   - If different, push difference back
5. Return `-stones[0]` if stones else `0`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(n log n)

**Space Complexity:**
O(n)
