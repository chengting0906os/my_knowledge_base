# Same Binary Tree

## Problem Description

Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

## Examples

### Example 1

```text
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

```
  p:       q:
   1        1
  / \      / \
 2   3    2   3

Same structure, same values → true
```

### Example 2

```text
Input: p = [4,7], q = [4,null,7]
Output: false
```

```
  p:       q:
   4        4
  /          \
 7            7

Different structure → false
```

### Example 3

```text
Input: p = [1,2,3], q = [1,3,2]
Output: false
```

```
  p:       q:
   1        1
  / \      / \
 2   3    3   2

Same structure, different values → false
```

### Constraints

- `0 <= The number of nodes in both trees <= 100`
- `-100 <= Node.val <= 100`

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

**Approach: Iterative DFS**

1. put root p and root q into stack
2. while stack:
   - node1, node2 = stack.pop()
   - if not node1 and not node2: continue
   - if not node1 or not node2: return False
   - if node1.val != node2.val: return False
   - stack.append(node1.left, node2.left)
   - stack.append(node1.right, node2.right)
  
**Approach: Breadth First Search**
 

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(n)

**Space Complexity:**
O(h)
