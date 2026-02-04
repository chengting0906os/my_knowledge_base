# Python Cheatsheet for LeetCode

## String Methods

| Method            | Description           | Example                              |
| ----------------- | --------------------- | ------------------------------------ |
| `isalnum()`       | Check if alphanumeric | `"abc123".isalnum()` → `True`        |
| `isalpha()`       | Check if alphabetic   | `"abc".isalpha()` → `True`           |
| `isdigit()`       | Check if digit        | `"123".isdigit()` → `True`           |
| `lower()`         | Convert to lowercase  | `"ABC".lower()` → `"abc"`            |
| `ord()` / `chr()` | Char ↔ ASCII          | `ord('a')` → `97`, `chr(97)` → `'a'` |

## Collections

| Method      | Description    | Example                             |
| ----------- | -------------- | ----------------------------------- |
| `Counter()` | Count elements | `Counter("aab")` → `{'a':2, 'b':1}` |

## defaultdict

| Usage | Example                                    |
| ----- | ------------------------------------------ |
| List  | `defaultdict(list)` → `d[key].append(val)` |
| Int   | `defaultdict(int)` → `d[key] += 1`         |
| Set   | `defaultdict(set)` → `d[key].add(val)`     |

```python
from collections import defaultdict
graph = defaultdict(list)
graph[1].append(2)  # No KeyError!
```

## deque

| Usage       | Example              |
| ----------- | -------------------- |
| Append      | `dq.append(val)`     |
| Append left | `dq.appendleft(val)` |
| Pop         | `dq.pop()`           |
| Pop left    | `dq.popleft()`       |

```python
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)  # [0, 1, 2, 3]
dq.popleft()      # → 0
```

## heapq

| Usage    | Example                        |
| -------- | ------------------------------ |
| Push     | `heappush(heap, val)`          |
| Pop      | `heappop(heap)` → smallest     |
| Heapify  | `heapify(arr)` → in-place O(n) |
| Top k    | `nlargest(k, arr)`             |
| Bottom k | `nsmallest(k, arr)`            |
| Max heap | Push `-val`, pop then negate   |

```python
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappop(heap)  # → 1 (min)
```

## Iteration

| Method        | Description      | Example                       |
| ------------- | ---------------- | ----------------------------- |
| `enumerate()` | Index + value    | `for i, v in enumerate(arr)`  |
| `zip()`       | Iterate multiple | `for a, b in zip(arr1, arr2)` |

## Reverse

| Usage    | Example                  | Note             |
| -------- | ------------------------ | ---------------- |
| Iterate  | `for x in reversed(arr)` | Returns iterator |
| Slice    | `arr[::-1]`              | Returns new list |
| In-place | `arr.reverse()`          | ⚠️ Returns None  |
| To list  | `list(reversed(arr))`    | Iterator → list  |

## Sorting

| Usage            | Example                                    |
| ---------------- | ------------------------------------------ |
| Basic            | `sorted([3,1,2])` → `[1,2,3]`              |
| Reverse          | `sorted(arr, reverse=True)`                |
| By key           | `sorted(arr, key=lambda x: x[1])`          |
| By length        | `sorted(words, key=len)`                   |
| By multiple keys | `sorted(arr, key=lambda x: (x[0], -x[1]))` |
| In-place         | `arr.sort()` (modifies original)           |

⚠️ **Common Mistake:**

```python
arr = arr.sort()  # ❌ arr becomes None!
arr.sort()        # ✓ modifies arr in-place

new_arr = sorted(arr)  # ✓ returns new list
```
