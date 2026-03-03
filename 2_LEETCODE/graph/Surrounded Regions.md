# 130. Surrounded Regions

## Problem Description

You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`. Capture all regions that are surrounded:

- **Connect:** A cell is connected to adjacent cells horizontally or vertically.
- **Region:** A region is formed by connecting every `'O'` cell.
- **Surround:** A region is surrounded if **none** of its `'O'` cells are on the edge of the board — i.e., it is completely enclosed by `'X'` cells.

To capture a surrounded region, replace all `'O'`s with `'X'`s **in-place**. You do not need to return anything.

## Examples

### Example 1

```text
Input:
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

Output:
[
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
```

**Explanation:** The bottom `'O'` is on the edge, so it cannot be surrounded and is not captured. The inner `'O'`s are fully enclosed and get replaced.

### Example 2

```text
Input:  board = [["X"]]
Output:          [["X"]]
```

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Any `'O'` connected (directly or indirectly) to a border `'O'` is **safe** — it should NOT be captured
- All other `'O'`s are surrounded and should be replaced with `'X'`

**Edge Cases:**

- Board is 1×1
- All `'O'`s are on the edge
- No `'O'`s at all

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Graph, DFS / BFS, Boundary traversal

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
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
