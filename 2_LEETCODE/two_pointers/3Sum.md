# 3Sum

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i`, `j`, and `k` are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

## Examples

### Example 1

```text
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

### Example 2

```text
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

### Example 3

```text
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

## Constraints

- `3 <= nums.length <= 1000`
- `-10^5 <= nums[i] <= 10^5`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

- Need all unique triplets whose sum is `0`.
- If we sort first, we can fix one number and use two pointers for the remaining two numbers.
- Duplicates must be skipped for both the fixed index `i` and the moving pointers `j`, `k`.
- Early stop: once `nums[i] > 0`, no later triplet can sum to `0`.

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Array + Sorting + Two Pointers

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. Initialize `res = []`, sort `nums`, and set `n = len(nums)`.
2. Iterate `i` from `0` to `n - 3`:
   - If `nums[i] > 0`, break.
   - If `i > 0` and `nums[i] == nums[i - 1]`, continue (skip duplicate first number).
3. Set two pointers:
   - `j = i + 1`
   - `k = n - 1`
4. While `j < k`:
   - `total = nums[i] + nums[j] + nums[k]`
   - If `total < 0`, move left pointer: `j += 1`
   - If `total > 0`, move right pointer: `k -= 1`
   - Else (`total == 0`):
     - Add answer: `res.append([nums[i], nums[j], nums[k]])`
     - Move both pointers: `j += 1`, `k -= 1`
     - Skip duplicates:
       - `while j < k and nums[j] == nums[j - 1]: j += 1`
       - `while j < k and nums[k] == nums[k + 1]: k -= 1`
5. Return `res`.

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
`O(n^2)` (sorting is `O(n log n)`, then two-pointer scan per `i`)

**Space Complexity:**

- Python sorting implementation detail can use additional memory
- Output storage: `O(m)` where `m` is the number of valid triplets
