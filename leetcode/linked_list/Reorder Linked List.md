# Reorder Linked List

## Problem Description

You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can initially be represented as:

```text
[0, 1, 2, 3, 4, 5, 6]
```

Reorder the nodes of the linked list to be in the following order:

```text
[0, 6, 1, 5, 2, 4, 3]
```

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

```text
[0, n-1, 1, n-2, 2, n-3, ...]
```

**Important:** You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

## Examples

### Example 1

```text
Input: head = [2,4,6,8]
Output: [2,8,4,6]
```

### Example 2

```text
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]
```

## Constraints

- `1 <= Length of the list <= 1000`
- `1 <= Node.val <= 1000`

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:**

### M - Match

**Pattern:**
Linked List
slow and fast


### P - Plan
split into two parts, use fast

### I - Implement

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
