# Min Stack

## Problem Description

Design a stack class that supports the `push`, `pop`, `top`, and `getMin` operations.

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

Each function should run in `O(1)` time.

## Examples

### Example 1

```text
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null, null, null, null, 0, null, 2, 1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- `pop`, `top`, and `getMin` will always be called on non-empty stacks.

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

**Approach: Two Stacks**

1. Initialize two stack:
   - `self.stack = deque()`
   - `self.min_stack = deque()`
2. On `push(val)`:
   - push `val` onto stack
   - Compute the new minimum (between `val` and `self.min_stack[-1])
   - append `new_min_val`
3. On `pop()`
   - Pop from both `stack` and `min_stack` to keep them aligned.
4. On `top()`
   - Return the top of `self.stack`
5. On `get_min()`:
   - Return the top of `self.min_stack`

**Approach: One Stack**

1. Initialize one stack and one current minimum:
   - `self.stack = deque()`  (store differences, not raw values)
   - `self.min_n = 0`
2. On `push(val)`:
   - if not self.stack:
     - `self.stack.append(0)`
     - `self.min_n = val`
   - else:
     - `diff = val - self.min_n`
     - `self.stack.append(diff)`
     - if `diff < 0`, update current min: `self.min_n = val`
3. On `pop()`
   - `diff = self.stack.pop()`
   - if `diff < 0`, restore previous min: `self.min_n = self.min_n - diff`
4. On `top()`
   - let `diff = self.stack[-1]`
   - if `diff < 0`, top value is current min: `return self.min_n`
   - else, top value is `return self.min_n + diff`
5. On `get_min()`:
   - Return `self.min_n`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
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
