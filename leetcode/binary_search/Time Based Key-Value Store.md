# Time Based Key-Value Store

## Problem Description

Implement a time-based key-value data structure that supports:

- Storing multiple values for the same key at specified time stamps
- Retrieving the key's value at a specified timestamp

Implement the `TimeMap` class:

| Method | Description |
|--------|-------------|
| `TimeMap()` | Initializes the object |
| `void set(String key, String value, int timestamp)` | Stores the key with the value at the given timestamp |
| `String get(String key, int timestamp)` | Returns the most recent value of key if `set` was previously called on it and the most recent timestamp for that key `prev_timestamp <= timestamp`. If there are no values, returns `""` |

> **Note:** For all calls to `set`, the timestamps are in strictly increasing order.

## Examples

### Example 1

```text
Input:
["TimeMap", "set", "get", "get", "set", "get"]
[[], ["alice", "happy", 1], ["alice", 1], ["alice", 2], ["alice", "sad", 3], ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]
```

**Explanation:**

```python
timeMap = TimeMap()
timeMap.set("alice", "happy", 1)  # store "alice" -> "happy" at timestamp = 1
timeMap.get("alice", 1)           # return "happy"
timeMap.get("alice", 2)           # return "happy" (no value at t=2, return value at t=1)
timeMap.set("alice", "sad", 3)    # store "alice" -> "sad" at timestamp = 3
timeMap.get("alice", 3)           # return "sad"
```

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` only include lowercase English letters and digits
- `1 <= timestamp <= 10^7`

---

## UMPIRE

### U - Understand

**Test Cases:**

- `set("a", "v1", 1)`, `get("a", 1)` → `"v1"`
- `set("a", "v1", 1)`, `get("a", 2)` → `"v1"` (closest timestamp ≤ 2)
- `get("a", 1)` (no set called) → `""`

**Edge Cases:**

- Query timestamp smaller than all stored timestamps → return `""`
- Query timestamp exactly matches a stored timestamp → return that value
- Multiple values for same key at different timestamps

**Key Observations:**

- Timestamps are strictly increasing → values are naturally sorted by time
- Need to find the largest timestamp ≤ query timestamp → binary search

### M - Match

**Pattern:** Binary Search

- Since timestamps are strictly increasing, we can use binary search to find the largest timestamp ≤ target

### P - Plan

1. Use `defaultdict(list)` to store `key -> [[value, timestamp], ...]`
2. `set`: Append `[value, timestamp]` to the list (already sorted due to strictly increasing timestamps)
3. `get`: Use binary search to find the rightmost timestamp ≤ target timestamp

### I - Implement

```python
class TimeMap:

    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**
set: O(1)
get: O(n)
**Space Complexity:** O(n)


