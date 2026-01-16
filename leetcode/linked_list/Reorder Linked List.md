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

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** linked-list
slow and fast
reverse

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. split into two parts, use slow and fast
    list2 = slow
2. reverse second linked-list
    2.1 create prev = None
        while list2: (Not point to None yet)
            nxt pointer point to next listnode as mark
            cur_head(list2).next pointer point to prev
            prev -> cur_head(list2)
            list2 -> nxt

3. combine them

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
