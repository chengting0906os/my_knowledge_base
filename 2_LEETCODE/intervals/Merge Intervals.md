# Merge Intervals

## Problem Description

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

**Note:** Intervals are non-overlapping if they have no common point. For example, `[1, 2]` and `[3, 4]` are non-overlapping, but `[1, 2]` and `[2, 3]` are overlapping.

## Examples

### Example 1

```text
Input: intervals = [[1,3],[1,5],[6,7]]
Output: [[1,5],[6,7]]
```

### Example 2

```text
Input: intervals = [[1,2],[2,3]]
Output: [[1,3]]
```

## Constraints

- `1 <= intervals.length <= 1000`
- `intervals[i].length == 2`
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

**Approach: Sorting**

1. sort intervals by start
2. init res = [intervals[0]]
3. traverse intervals[1:]:
   - if overlap (inter[0] <= res[-1][1]): merge by updating res[-1][1] = max(...)
   - else: append interval to res
4. return res

**Approach: Greedy**

1. find max_start
2. create a list [0] \* max_start+1
3. traverse and record mp[start] = max(end + 1, mp[start])
4. init
   - res = []
   - cur_max_reach = float('-inf')
   - interval_start = None
5. traverse
   - for i in range(len(mp))
     - if mp[i] != 0:
       - if interval_start is None: interval_start = i
       - cur_max_reach = max(mp[i] - 1, cur_max_reach)
     - if i == cur_max_reach:
       - res.append([interval_start, cur_max_reach])
       - cur_max_reach = -1
       - interval_start = None
   - if interval_start is not None:
     - res.append([interval_start, cur_max_reach])

6. return res

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(n log n) - sorting

**Space Complexity:**
O(n) - output array
