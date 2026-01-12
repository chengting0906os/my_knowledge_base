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

**Test Cases:**

**Edge Cases:**

**Key Observations:**

- Rotate 90° clockwise = **Transpose** + **Reverse each row**
- Transpose: swap `matrix[i][j]` ↔ `matrix[j][i]` (along main diagonal)
- After rotation: `matrix[j][n-1-i]` ← original `matrix[i][j]`

### M - Match

**Pattern:**

### P - Plan

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

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**
O(n²): n(n-1)/2

**Space Complexity:**
O(1)
