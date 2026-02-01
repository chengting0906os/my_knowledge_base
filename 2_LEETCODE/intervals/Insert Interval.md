# Insert Interval

## Problem Description

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represents the start and the end time of the ith interval. `intervals` is initially sorted in ascending order by `start_i`.

You are given another interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and also `intervals` still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return `intervals` after adding `newInterval`.

**Note:** Intervals are non-overlapping if they have no common point. For example, `[1,2]` and `[3,4]` are non-overlapping, but `[1,2]` and `[2,3]` are overlapping.

## Examples

### Example 1

```text
Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
Output: [[1,6]]
```

### Example 2

```text
Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
Output: [[1,2],[3,5],[6,7],[9,10]]
```

## Constraints

- `0 <= intervals.length <= 1000`
- `newInterval.length == intervals[i].length == 2`
- `0 <= start <= end <= 1000`

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

1. init
   - res = []
   - i = 0
   - n = len(intervals)
2. while i < n and intervals[i][1] < newInterval[0]:
   - append intervals[i] to res (no overlap, completely before)
   - i += 1
3. while i < n and intervals[i][0] <= newInterval[1]:
   - merge: newInterval = [min of starts, max of ends]
   - i += 1
   - after loop, append merged newInterval to res
4. return res + intervals[i:]

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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
O(1) + O(n)
