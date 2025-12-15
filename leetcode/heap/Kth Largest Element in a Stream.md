# Kth Largest Element in a Stream

## Problem Description

Design a class to find the kth largest integer in a stream of values, including duplicates.

E.g. the 2nd largest from `[1, 2, 3, 3]` is `3`. The stream is not necessarily sorted.

Implement the following methods:

| Method | Description |
|--------|-------------|
| `KthLargest(int k, int[] nums)` | Initializes the object given an integer `k` and the stream of integers `nums` |
| `int add(int val)` | Adds the integer `val` to the stream and returns the kth largest integer in the stream |

## Examples

### Example 1

```text
Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

Output:
[null, 3, 3, 3, 5, 6]
```

**Explanation:**

```python
kthLargest = KthLargest(3, [1, 2, 3, 3])
kthLargest.add(3)   # return 3
kthLargest.add(5)   # return 3
kthLargest.add(6)   # return 3
kthLargest.add(7)   # return 5
kthLargest.add(8)   # return 6
```

## Constraints

- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**

### M - Match

**Pattern:** Min Heap

### P - Plan

1. `__init__`: Heapify nums list
2. `__init__`: Pop until `len(heap) == k`
3. `add`: If `len(heap) == k`, use `heappushpop`; else `heappush`
4. `add`: Return `heap[0]` (the kth largest)

### I - Implement

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:** O(n log k)

**Space Complexity:** O(k)
