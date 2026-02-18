# Top K Frequent Elements

## Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

## Examples

### Example 1

```text
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]
```

### Example 2

```text
Input: nums = [7,7], k = 1
Output: [7]
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `1 <= k <=` number of distinct elements in `nums`

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

**Approach: max heap**

1. use mp = Counter(nums)
2. max_heap = []
3. res = []
4. for n, count in mp.items(), max_heap.append(count, n)
5. heapify_max(max_heap)
6. traverse to idx k-1 res.append(heap_item[1])

**Approach: bucket sort**

1. use mp = Counter(nums)
2. create bucket with lists idx = count, value in mp = idx and you need to append key into `bucket[idx]`
3. Init a list = []
4. traverse mp and append key into bucket[value]
5. traverse from the end and return while `len(res) == k`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
