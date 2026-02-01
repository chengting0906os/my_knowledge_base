# Daily Temperatures

## Problem Description

You are given an array of integers `temperatures` where `temperatures[i]` represents the daily temperatures on the ith day.

Return an array `result` where `result[i]` is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set `result[i]` to `0` instead.

## Examples

### Example 1

```text
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]
```

### Example 2

```text
Input: temperatures = [22,21,20]
Output: [0,0,0]
```

### Example 3

```text
Input: temperatures = [1,2,3,4,5]
Output: [1,1,1,1,0]
```

## Constraints

- `1 <= temperatures.length <= 1000`
- `1 <= temperatures[i] <= 100`

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

**Key Observations:**

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:** Monotonic Stack

**Approach:** Use a deque/stack to store indices. When encountering a temperature larger than previous temperatures in the stack, pop them and calculate the difference in indices.

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

1. **Initialize:**
   - `stack = []` (stores indices)
   - `result = [0] * len(temperatures)` (default to 0 for no warmer day)

2. **For loop** through temperatures with `enumerate(i, temp)`:
   - **While** `stack` is not empty AND `temp > temperatures[stack[-1]]`:
     - `prev_idx = stack.pop()`
     - `result[prev_idx] = i - prev_idx`
   - Append current index: `stack.append(i)`

3. **Return** result

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)

    return result
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

**Test with Example 1:**

```text
temperatures = [30,38,30,36,35,40,28]

i=0, temp=30: stack=[] → stack=[0]
i=1, temp=38: 38>30 → pop(0), result[0]=1 → stack=[1]
i=2, temp=30: 30<38 → stack=[1,2]
i=3, temp=36: 36>30 → pop(2), result[2]=1, 36<38 → stack=[1,3]
i=4, temp=35: 35<36 → stack=[1,3,4]
i=5, temp=40: 40>35 → pop(4), result[4]=1
              40>36 → pop(3), result[3]=2
              40>38 → pop(1), result[1]=4 → stack=[5]
i=6, temp=28: 28<40 → stack=[5,6]

result = [1,4,1,2,1,0,0] ✓
```

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**
`O(n)`

- Each element is pushed and popped at most once

**Space Complexity:**
`O(n)`

- Stack can contain up to n elements in worst case (decreasing sequence)



---

DP
