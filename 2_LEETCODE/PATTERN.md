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

## Trie

**Template - Add Word:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
```

## Counting Sort

**When to use:**

- Value range is known and small (`max(nums)` within 10^5)
- Need O(n) sort to avoid O(n log n)
- Sorting followed by two pointers (need to rebuild sorted array in-place)

**Key Points:**

- Time O(n + k), Space O(k), where k = value range
- Faster than `sort()`, but only works for integers with a bounded range
- Common pattern: build count array → rebuild sorted array → run two pointers

**Template:**

```python
m = max(nums)
count = [0] * (m + 1)
for x in nums:
    count[x] += 1

# Rebuild sorted array in-place
idx = 0
for val in range(m + 1):
    while count[val] > 0:
        nums[idx] = val
        count[val] -= 1
        idx += 1
```

**Key Problems:**

- [Boats to Save People (LC 881)](https://leetcode.com/problems/boats-to-save-people/) — counting sort rebuild + two pointers greedy
- [H-Index (LC 274)](https://leetcode.com/problems/h-index/) — build citation count array, scan from right
- [Sort an Array (LC 912)](https://leetcode.com/problems/sort-an-array/) — direct counting sort implementation

## Char Indexing (ord)

**When to use:**

- Frequency arrays for lowercase/uppercase letters
- Anagram / permutation checks
- Sliding window on letters

**Key Points:**

- `idx = ord(c) - ord('a')` for `a`-`z`
- `c = chr(idx + ord('a'))` to convert back
- Use size `26` for lowercase, `52` if mixing cases, or `128/256` for ASCII

**Common Operations:**

```python
idx = ord(c) - ord('a')
count[idx] += 1

letter = chr(idx + ord('a'))
```
