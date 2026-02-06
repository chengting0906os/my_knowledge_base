# Reverse Linked List

## Problem Description

Given the beginning of a singly linked list `head`, reverse the list, and return the new beginning of the list.

## Examples

### Example 1

```text
Input: head = [0,1,2,3]
Output: [3,2,1,0]
```

### Example 2

```text
Input: head = []
Output: []
```

## Constraints

- `0 <= The length of the list <= 1000`
- `-1000 <= Node.val <= 1000`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:**

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. Init:
   - prev = None
   - curr = head

```
 prev  temp
  v     v
None    0 -> 1 -> 2 -> 3
```

2. while loop until curr move to None
   - curr move to temp.next
   - temp point to prev
   - prev move to temp
   - temp move to curr

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
