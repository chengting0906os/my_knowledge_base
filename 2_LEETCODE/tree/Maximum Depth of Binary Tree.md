# Maximum Depth of Binary Tree

## Problem Description

Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

### Example 1

```text
Input: root = [1,2,3,null,null,4]
Output: 3
```

```
     1
    / \
   2   3
      /
     4

Depth = 3 (path: 1 → 3 → 4)
```

### Example 2

```text
Input: root = []
Output: 0
```

### Constraints

- `0 <= The number of nodes in the tree <= 100`
- `-100 <= Node.val <= 100`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Empty tree → return 0

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:**

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

**Approach: Recursive DFS**

1. Base Case: if not root, return 0
2. return `1 + max(self.maxDepth(root.left), self.maxDepth(root.right))`

**Approach: Iterative DFS (Stack)**
1. Base Case: if not root, return 0
2. Init:
   - stack = [(root, 1)]
   - res = 0
3. while stack:
   - node, depth = stack.pop()
   - res = max(res, depth)
   - if node.left: stack.append((node.left, depth + 1))
   - if node.right: stack.append((node.right, depth + 1))
4. return res

**Approach: Breadth First Search (Queue)**
1. Base Case: if not root, return 0
2. Init:
   - queue = deque([root])
   - depth = 0
3. while queue:
   - depth += 1
   - for i in range(len(queue)): process all nodes at current level
     - node = queue.popleft()
     - if node.left: queue.append(node.left)
     - if node.right: queue.append(node.right)
4. return depth

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
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
O(n)
