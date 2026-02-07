# Invert Binary Tree

## Problem Description

You are given the root of a binary tree `root`. Invert the binary tree and return its root.

## Examples

### Example 1

```text
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]
```

```
     1              1
    / \            / \
   2   3   →     3   2
  / \ / \       / \ / \
 4  5 6  7     7  6 5  4
```

### Example 2

```text
Input: root = [3,2,1]
Output: [3,1,2]
```

### Example 3

```text
Input: root = []
Output: []
```

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Empty tree → return None

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:**

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.
>   **Approach: Depth First Search**

1. Base Case: `if not root return None`
2. root.left, root.right = root.right, root.left
3. self.invertTree(root.left)
4. self.invertTree(root.right)
5. return root

**Approach: Iterative DFS**

1. Base Case: `if not root return None`
2. stack = deque([root])
3. while stack: - node = stack.popleft()
   - if node.left: stack.append(node.left)
   - if node.right: stack.append(node.right)
4. return root

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
