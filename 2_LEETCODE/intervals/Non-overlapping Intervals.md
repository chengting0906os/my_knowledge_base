# Non-overlapping Intervals

## Problem Description

Given an array of intervals where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**Note:** Intervals are non-overlapping even if they have a common point. For example, `[1, 3]` and `[2, 4]` are overlapping, but `[1, 2]` and `[2, 3]` are non-overlapping.

## Examples

### Example 1

```text
Input: intervals = [[1,2],[2,4],[1,4]]
Output: 1
Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.
```

### Example 2

```text
Input: intervals = [[1,2],[2,4]]
Output: 0
```

## Constraints

- `1 <= intervals.length <= 1000`
- `intervals[i].length == 2`
- `-50000 <= start_i < end_i <= 50000`

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

**Approach:**

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

1. sort
   - `intervals.sort(key=lambda x: x[0])`
2. init
   - prev_end = intervals[0][1]
   - res = 0
3. traverse from 1
   - `for i in range(1, len(intervals)):`
   - if start < prev_end
     - res += 1
     - prev_end = min(prev_end, end) # Keep the one with the earlier end time
       else
     - prev_end = end
4. return res

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(nlogn)

**Space Complexity:**
O(1)
