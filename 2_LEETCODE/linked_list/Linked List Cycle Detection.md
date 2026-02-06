# Linked List Cycle Detection

## Problem Description

Given the beginning of a linked list `head`, return `true` if there is a cycle in the linked list. Otherwise, return `false`.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

## Examples

### Example 1

```text
Input: head = [1,2,3,4], index = 1
Output: true
```

Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

### Example 2

```text
Input: head = [1,2], index = -1
Output: false
```

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Linked List - Fast and Slow Pointers

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

- If fast and slow pointers meet, there is a cycle.

1. Init: both pointers start at head.
   - slow = head
   - fast = head

2. While fast and fast.next exist, move both pointers.
   - slow = slow.next (move 1 step)
   - fast = fast.next.next (move 2 steps)
   - if slow == fast: return True (they met, cycle found)

3. return False (fast reached the end, no cycle)

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**

**Space Complexity:**
