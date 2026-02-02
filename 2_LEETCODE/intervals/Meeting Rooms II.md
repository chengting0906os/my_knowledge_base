# Meeting Rooms II

## Problem Description

Given an array of meeting time interval objects consisting of start and end times `[[start_1,end_1],[start_2,end_2],...]` (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

**Note:** `(0,8),(8,10)` is not considered a conflict at 8.

## Examples

### Example 1

```text
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)
```

### Example 2

```text
Input: intervals = [(4,9)]
Output: 1
```

## Constraints

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

**Approach: Min Heap**

1. Sort by `interval.start`
2. Init `min_heap = []` (stores end times of ongoing meetings)
3. Traverse intervals:
   - If `min_heap` and `min_heap[0] <= interval.start`:
     - `heapq.heappop(min_heap)` — earliest meeting ended, reuse that day
   - `heapq.heappush(min_heap, interval.end)` — schedule current meeting
4. Return `len(min_heap)` — heap size = number of concurrent days needed

> **Why `if` not `while`?**
> Each new meeting only needs 1 room. Using `if` ensures we reuse at most 1 freed room, so heap size correctly represents the number of concurrent rooms needed.

**Approach: Sweep Line Algorithm**

1. Init `mp = defaultdict(int)` (event map)
2. Record events:
   - `mp[interval.start] += 1` — meeting starts
   - `mp[interval.end] -= 1` — meeting ends
3. Init `res = 0`, `active = 0`
4. Traverse `sorted(mp.keys())`:
   - `active += mp[time]` — update concurrent meetings
   - `res = max(res, active)` — track peak
5. Return `res`

**Approach: Two Pointers**

1. Init:
   - `starts = sorted([i.start for i in intervals])`
   - `ends = sorted([i.end for i in intervals])`
   - `s = 0`, `e = 0` — pointers for starts/ends
   - `active = 0`, `res = 0`
2. Traverse with `while s < len(intervals)`:
   - If `starts[s] < ends[e]`:
     - `active += 1`, `s += 1` — new meeting starts, need a room
   - Else:
     - `active -= 1`, `e += 1` — a meeting ends, free a room
   - `res = max(res, active)` — track peak
3. Return `res`

> **Intuition:**
> Sort starts and ends separately. Use two pointers to simulate timeline: +1 room when hitting a start, -1 room when hitting an end, track the peak.

**Approach: Event Sorting (Greedy)**

1. Init `time = []`, `res = 0`, `active = 0`
2. For each interval:
   - `time.append((start, 1))` — meeting starts
   - `time.append((end, -1))` — meeting ends
3. `time.sort()` — sort by time, then by event (-1 before +1)
4. Traverse `time`:
   - `active += t[1]` — update concurrent meetings
   - `res = max(res, active)` — track peak
5. Return `res`

> **Why `-1` before `+1` at same time?**
> Meetings like `(0,8)` and `(8,10)` can share a room. Process end first, then start → room handoff works.

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**

**Space Complexity:**
