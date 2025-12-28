# LRU Cache

## Problem Description

Implement the Least Recently Used (LRU) cache class `LRUCache`. The class should support the following operations:

- `LRUCache(int capacity)` - Initialize the LRU cache of size capacity
- `int get(int key)` - Return the value corresponding to the key if the key exists, otherwise return `-1`
- `void put(int key, int value)` - Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key

**Note:** A key is considered used if a `get` or a `put` operation is called on it.

**Requirement:** Ensure that `get` and `put` each run in **O(1)** average time complexity.

## Examples

### Example 1

```text
Input:
["LRUCache", [2], "put", [1, 10], "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]
```

**Explanation:**

```java
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20
lRUCache.get(1);      // return -1 (not found)
```

## Constraints

- `1 <= capacity <= 100`
- `0 <= key <= 1000`
- `0 <= value <= 1000`

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**
- It's a double linked-list question which you can init a self.left(head) and self.right(tail) Node(0,0) as an init double linked-list than you need to insert or remove Node() between these two init-node.

- Insert new node from at tail (most recent)
- Remove from head (least recent) when no capacity

### M - Match

**Pattern:** Double Linked List

### P - Plan

1. class Node:
    self.key = key
    self.val = val
    self.prev = self.next = None (pointers)

2. class LRUCache init: create two dummy nodes as head and tail

3. implement insert method:
    update next and prev pointers

4. implement remove method:
    update next and prev pointers

5. implement get method:
    if key not in self.cache:
        return -1
    else:
        move existing Node to the tail

6. implement put method:
    add Node to the tail
    if len(self.cache) > self.cap:
        remove LRU node (self.head.next)

### I - Implement

### R - Review

### E - Evaluate

**Time Complexity:**
get(): O(1)
put(): O(1)


**Space Complexity:**
O(n)