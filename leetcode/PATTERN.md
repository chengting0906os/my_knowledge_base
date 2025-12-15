# LeetCode Patterns

## Heap / Priority Queue

**When to use:**

- Find kth largest/smallest element
- Merge k sorted lists/arrays
- Top k frequent elements
- Continuous median (use two heaps)
- Task scheduling with priorities

**Key Points:**

- Python `heapq` is **min heap** by default
- For max heap: negate values (`-val`) or Python 3.14+ (`heappush_max`, `heappop_max`)
- `heapify()` is O(n), `push/pop` is O(log n)
- Keep heap size = k for "kth largest" problems

**Common Operations:**

```python
import heapq

heapq.heapify(nums)           # O(n) - convert list to heap
heapq.heappush(heap, val)     # O(log n) - push value
heapq.heappop(heap)           # O(log n) - pop smallest
heapq.heappushpop(heap, val)  # O(log n) - push then pop (more efficient)
heapq.nlargest(k, nums)       # O(n log k) - get k largest
heapq.nsmallest(k, nums)      # O(n log k) - get k smallest
```

**Template - Kth Largest:**

```python
def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)
    return heap[0]
```
