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

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- One or both lists are empty → return the non-empty list or `[]`

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Linked List - Two Pointers with Dummy Node

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

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
       - `list1 = list1.next`
     - Else:
       - `current.next = list2`
       - `list2 = list2.next`
     - `current = current.next`

4. **Attach remaining nodes:**
   - If `list1` still has nodes: `current.next = list1`
   - If `list2` still has nodes: `current.next = list2`

5. **Return:** `dummy.next`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**

**Space Complexity:**
