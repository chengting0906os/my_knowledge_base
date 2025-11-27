# Merge Two Sorted Linked Lists

## Problem Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from `list1` and `list2`.

## Examples

### Example 1

```text
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]
```

### Example 2

```text
Input: list1 = [], list2 = [1,2]
Output: [1,2]
```

### Example 3

```text
Input: list1 = [], list2 = []
Output: []
```

---

## UMPIRE

### U - Understand

**Edge Cases:**

- One or both lists are empty → return the non-empty list or `[]`

### M - Match

**Pattern:** Linked List - Two Pointers with Dummy Node

### P - Plan

1. **Handle edge cases:**
   - If `list1` is `None`, return `list2`
   - If `list2` is `None`, return `list1`

2. **Create dummy node:**

   ```python
   dummy = ListNode()
   current = dummy
   ```

3. **Merge two lists:**
   - While both `list1` and `list2` exist:
     - If `list1.val < list2.val`:
       - `current.next = list1`
       - `list1 = list1.next` (指針往右移)
     - Else:
       - `current.next = list2`
       - `list2 = list2.next` (指針往右移)
     - `current = current.next` (current 指針也往右移)

4. **Attach remaining nodes:**
   - If `list1` still has nodes: `current.next = list1`
   - If `list2` still has nodes: `current.next = list2`

5. **Return:** `dummy.next` (dummy 始終保持在最開頭)

**Pseudocode:**

```python
# Edge cases
if not list1: return list2
if not list2: return list1

# Create dummy node
dummy = ListNode()
current = dummy

# Merge while both exist
while list1 and list2:
    if list1.val < list2.val:
        current.next = list1
        list1 = list1.next
    else:
        current.next = list2
        list2 = list2.next
    current = current.next

# Attach remaining nodes
current.next = list1 if list1 else list2

return dummy.next
```
