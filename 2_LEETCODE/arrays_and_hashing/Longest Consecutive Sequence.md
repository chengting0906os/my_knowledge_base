# Longest Consecutive Sequence

## Problem Description

Given an array of integers `nums`, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly `1` greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in `O(n)` time.

## Examples

### Example 1

```text
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].
```

### Example 2

```text
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
```

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

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

**Approach: Hash Set**

1. Convert the nums list into set for O(1) loopups.
2. Initilize `longest` to track the length of the longest consecutive sequence.
3. For each num in num_set:
   - Check if num - 1 not in num_set
     - If True, num is the start of the sequence
     - Initialize length = 1
     - while n + length in nums: length += 1
   - Update longest with the maximum length found
4. return `longest`

**Approach: Hash Map**

1. Create a hashmap `mp` that store the longest sequence found
2. Initialize `res = 0` to store the longest sequence found
3. For each element:
   - If n not in mp:
     - `left = mp.get(n - 1, 0)`
     - `right = mp.get(n + 1, 0)`
     - length = left + 1 + right
     - update `mp[n] = length`
     - Update the boundaries:
       - `mp[n - left] = length`
       - `mp[n + right] = length`
     - Update longest with the maximum length found
4. return `longest`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
