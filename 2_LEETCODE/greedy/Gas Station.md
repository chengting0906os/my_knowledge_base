# Gas Station

## Problem Description

There are `n` gas stations along a circular route. You are given two integer arrays `gas` and `cost` where:

- `gas[i]` is the amount of gas at the `i`th station.
- `cost[i]` is the amount of gas needed to travel from the `i`th station to the `(i + 1)`th station. (The last station is connected to the first station)

You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return `-1`.

It's guaranteed that at most one solution exists.

## Examples

### Example 1

```text
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation: Start at station 3 and you can complete the circuit.
```

### Example 2

```text
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation: There is no valid starting station.
```

## Constraints

- `1 <= gas.length <= 10^5`
- `gas.length == cost.length`
- `0 <= gas[i], cost[i] <= 10^4`

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

1. base case
    - if `sum(gas) < sum(cost)`, return `-1`
2. init
    - `n = len(gas)`
    - `cur_gas = 0`
    - `res = 0`
3. traverse (if `cur_gas` drops below 0, none of the previous stations can be a valid start, so reset)
    - `cur_gas = cur_gas + gas[i] - cost[i]`
    - if `cur_gas < 0`:
        - `cur_gas = 0`
        - `res = i + 1`
4. return `res`
    



```python

```

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
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
