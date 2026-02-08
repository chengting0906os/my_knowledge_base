# Balanced Binary Tree

## Problem Description

Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

## Examples

### Example 1

```text
Input: root = [1,2,3,null,null,4]
Output: true
```

```
     1
    / \
   2   3
      /
     4

Every node's subtrees differ in height by at most 1 → balanced
```

### Example 2

```text
Input: root = [1,2,3,null,null,4,null,5]
Output: false
```

```
       1
      / \
     2   3
        /
       4
      /
     5

Node 1: left height=1, right height=3 → diff=2 → not balanced
```

### Example 3

```text
Input: root = []
Output: true
```

### Constraints

- `0 <= The number of nodes in the tree <= 1000`
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

**Approach: Depth First Search**

1. Create a dfs helper that returns the height of a subtree
   - Recursively get left height and right height
   - If abs(left height - right height) > 1 → not balanced
   - if not root return (True, 0)
   - is_balance = left[0] and right[0] and abs(left height - right height) <= 1
2. return dfs(root)[0]

**Approach: Iterative DFS**
postorder traverse

1. Init:
   - stack = []
   - curr = root
   - last_node = None
   - depths = {}
2. while stack or curr:
   - if curr:
     - stack.append(curr)
     - curr = curr.left
   - else:
     - curr = stack[-1]
     - if not curr.right or last_node == curr.right:
       - stack.pop()
       - left = depths.get(curr.left, 0)
         right = depths.get(curr.right, 0)

         if abs(left - right) > 1:
         return False

       - depths[curr] = 1 + max(left, right)
       - last_node = curr
       - curr = None

     - else:
       - curr = curr.right

3. return True

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(n) — visit each node once

**Space Complexity:**
O(h) — recursion stack, where h is the height of the tree (worst case O(n) for skewed tree)
