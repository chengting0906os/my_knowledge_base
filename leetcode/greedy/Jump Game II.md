# Jump Game II

## Problem Description

You are given an array of integers `nums`, where `nums[i]` represents the maximum length of a jump towards the right from index `i`. If you are at `nums[i]`, you can jump to any index `i + j` where:

- `j <= nums[i]`
- `i + j < nums.length`

You are initially positioned at `nums[0]`.

Return the minimum number of jumps to reach the last position in the array (index `nums.length - 1`). You may assume there is always a valid answer.

## Examples

### Example 1

```text
Input: nums = [2,4,1,1,1,1]
Output: 2
Explanation: Jump from index 0 to index 1, then jump from index 1 to the last index.
```

### Example 2

```text
Input: nums = [2,1,2,1,0]
Output: 2
```

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 100`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Greedy

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. init
   - `n = len(nums)`
   - `max_reach = 0` (farthest we can reach so far)
   - `r = 0` (right boundary of the current jump)
   - `jumps = 0`

2. traverse nums
   - update `max_reach` every step
   - when `i == r`, we must take a jump and extend `r` to `max_reach`
   - loop only to `n - 1`, because landing on the last index ends the process

```python
for i in range(n - 1):
    max_reach = max(max_reach, i + nums[i])
    if i == r:
        jumps += 1
        r = max_reach

return jumps


```

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

Note: Loop only to `n - 1` because once you reach the last index, you do not need to update `jumps` again.

**Time Complexity:**
O(n)

**Space Complexity:**
O(1)
