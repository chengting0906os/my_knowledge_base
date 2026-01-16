# Rotate Image

## Problem Description

Given a square `n x n` matrix of integers `matrix`, rotate it by **90 degrees clockwise**.

You must rotate the matrix **in-place**. Do not allocate another 2D matrix and do the rotation.

## Examples

### Example 1

```text
Input: matrix = [
  [1,2],
  [3,4]
]

Output: [
  [3,1],
  [4,2]
]
```

### Example 2

```text
Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Rotate 90° clockwise = **Transpose** + **Reverse each row**
- Transpose: swap `matrix[i][j]` ↔ `matrix[j][i]` (along main diagonal)
- After rotation: `matrix[j][n-1-i]` ← original `matrix[i][j]`

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:**

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

**Approach: Reverse + Transpose**

1. **Reverse rows** (flip upside down)

   ```python
   matrix.reverse()  # in-place
   ```

2. **Transpose** (swap along main diagonal)
   ```python
   for i in range(n):
       for j in range(i + 1, n):  # j > i to avoid double swap
           matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
   ```

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
O(n²): n(n-1)/2

**Space Complexity:**
O(1)
