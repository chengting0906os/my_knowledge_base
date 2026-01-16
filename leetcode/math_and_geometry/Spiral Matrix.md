# Spiral Matrix

## Problem Description

Given an `m x n` matrix of integers `matrix`, return a list of all elements within the matrix in **spiral order**.

## Examples

### Example 1

```text
Input: matrix = [[1,2],[3,4]]
Output: [1,2,4,3]
```

### Example 2

```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 3

```text
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints

- `1 <= matrix.length, matrix[i].length <= 10`
- `-100 <= matrix[i][j] <= 100`

---

## UMPIRE

### U - Understand

**Test Cases:**

**Edge Cases:**

**Key Observations:** 

### M - Match

**Pattern:** recursive, iteration

### P - Plan

**Approach: Recursive (Boundary Shrinking)**

1. Initialize `rows = len(matrix)`, `cols = len(matrix[0])`, `res = []`
2. Create a recursive function `dfs(row_start, row_end, col_start, col_end)`:
   - **Base case:** if `row_start > row_end` or `col_start > col_end`, return
   - Traverse top row: left → right
   - Traverse right column: top+1 → bottom
   - Traverse bottom row: right+1 → left (if `row_start != row_end`)
   - Traverse left column: bottom + 1 → top - 1 (if `col_start != col_end`)
   - Recurse: `dfs(row_start + 1, row_end - 1, col_start + 1, col_end - 1)`
3. Call `dfs(0, rows - 1, 0, cols - 1)`
4. Return `res`

**Approach: Iterative (Boundary Shrinking)**

1. Initialize boundaries: `left = 0`, `right = cols - 1`, `top = 0`, `bottom = rows - 1`, `res = []`
2. While `left <= right` and `top <= bottom`:
   - Traverse top row: left → right
   - Traverse right column: top + 1 → bottom
   - **Early exit:** if `left == right` or `top == bottom`, break (single row/column case)
   - Traverse bottom row: right - 1 → left
   - Traverse left column: bottom - 1 → top + 1
   - Shrink boundaries: `left += 1`, `right -= 1`, `top += 1`, `bottom -= 1`
3. Return `res`



### I - Implement

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass
```

### R - Review

### E - Evaluate

**Time Complexity:**

**Space Complexity:**
