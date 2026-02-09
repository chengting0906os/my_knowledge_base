# Meeting Rooms

## Problem Description

Given an array of meeting time interval objects consisting of start and end times `[[start_1,end_1],[start_2,end_2],...]` (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

**Note:** `(0,8),(8,10)` is not considered a conflict at 8.

## Examples

### Example 1

```text
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
```

```
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
```

### Example 2

```text
Input: intervals = [(5,8),(9,15)]
Output: true
```

### Constraints

- `0 <= intervals.length <= 500`
- `0 <= intervals[i].start < intervals[i].end <= 1,000,000`

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

1. Base Case: if not intervals return True
2. sort
3. if start > pre_end:
   return False
4. return True

**Approach: Sorting**

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
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
O(1)
