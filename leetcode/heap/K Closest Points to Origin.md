# K Closest Points to Origin

## Problem Description

You are given a 2-D array `points` where `points[i] = [xi, yi]` represents the coordinates of a point on an X-Y axis plane. You are also given an integer `k`.

Return the `k` closest points to the origin `(0, 0)`.

The distance between two points is defined as the Euclidean distance: `sqrt((x1 - x2)^2 + (y1 - y2)^2)`

You may return the answer in any order.

## Examples

### Example 1

```text
Input: points = [[0,2],[2,2]], k = 1
Output: [[0,2]]
```

**Explanation:** The distance between (0, 2) and the origin is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.83. So the closest point is (0, 2).

### Example 2

```text
Input: points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]
```

**Explanation:** The output `[[2,0],[0,2]]` would also be accepted.

## Constraints

- `1 <= k <= points.length <= 1000`
- `-100 <= points[i][0], points[i][1] <= 100`

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**

### M - Match

**Pattern:** Max Heap

### P - Plan

1. [:k], heap.append((-dist, [x, y]))  
2. [k:], heapq.heappushpop(heap, (-dist, [x, y]))

### I - Implement

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
