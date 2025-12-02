# Remove Nth Node From End of List

## Problem Description

You are given the head of a linked list. Remove the nth node from the end of the list and return its head.

## Examples

### Example 1

```text
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2

```text
Input: head = [1], n = 1
Output: []
```

### Example 3

```text
Input: head = [1,2], n = 1
Output: [1]
```

## Constraints

- The number of nodes in the list is `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**

### M - Match

**Pattern:**

### P - Plan

1. Create dummy = ListNode(0, head)
2. Use slow and fast pointers
3. Return dummy.next

### I - Implement

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
