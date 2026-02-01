# Hand of Straights

## Problem Description

You are given an integer array `hand` where `hand[i]` is the value written on the ith card and an integer `groupSize`.

You want to rearrange the cards into groups so that each group is of size `groupSize`, and card values are consecutively increasing by 1.

Return `true` if it's possible to rearrange the cards in this way, otherwise, return `false`.

## Examples

### Example 1

```text
Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4
Output: true
```

**Explanation:** The cards can be rearranged as `[1,2,3,4]` and `[2,3,4,5]`.

### Example 2

```text
Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4
Output: false
```

**Explanation:** The closest we can get is `[1,2,3,4]` and `[3,5,6,7]`, but the cards in the second group are not consecutive.

## Constraints

- `1 <= hand.length <= 1000`
- `0 <= hand[i] <= 1000`
- `1 <= groupSize <= hand.length`

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

1. base case: if len(hand) cannot be devided by groupSize
2. count frequency of each card using Counter
3. use min heap 
4. for each smallest card:
    - try to form a group of groupSize consecutive cards
    - decrement count for each card used
    - if any card is missing or counf < 0, return False

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
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
