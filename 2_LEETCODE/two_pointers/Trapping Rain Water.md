# Trapping Rain Water

## Problem Description

You are given an array of non-negative integers `height` which represent an elevation map. Each value `height[i]` represents the height of a bar, and each bar has width `1`.

Return the maximum area of water that can be trapped between the bars.

## Examples

### Example 1

```text
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
```

## Constraints

- `1 <= height.length <= 1000`
- `0 <= height[i] <= 1000`

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

1. Init:
   - l = 0
   - r = len(heights) - 1
   - max_l = heights[l]
   - max_r = heights[r]
   - res = 0
2. while l < r:
   - if heights[l] <= heights[r]:
     - `res += (max_l - height[l])`
     - `l += 1`
     - `max_l = max(height[l], max_l)`
   - else:
     - `res += (max_r - height[r])`
     - `r -= 1`
     - `max_r = max(height[r], max_r)`
3. `return res`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def trap(self, height: List[int]) -> int:
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
