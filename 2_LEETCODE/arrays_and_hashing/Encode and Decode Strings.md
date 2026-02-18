# Encode and Decode Strings

## Problem Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

```cpp
string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
```

Machine 2 (receiver) has the function:

```cpp
vector<string> decode(string s) {
    // ... your code
    return strs;
}
```

So Machine 1 does:

```cpp
string encoded_string = encode(strs);
```

And Machine 2 does:

```cpp
vector<string> strs2 = decode(encoded_string);
```

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the `encode` and `decode` methods.

## Examples

### Example 1

```text
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

### Example 2

```text
Input: dummy_input = [""]
Output: [""]
```

## Constraints

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains any possible characters out of `256` valid ASCII characters

Follow-up: Could you write a generalized algorithm to work on any possible set of characters?

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

**def encode**

1. Init: res = ""
2. For each word:
   `res += str(len(s))`
   `res += "#"`
   `res += word`
3. `return res`

**def decode**

1. Init:
   - `i=0`
   - `res=[]`
2. while i:
   - `init j = i every round`
   - while s[j] != "#" j pointer move forward since s[i:j] = length
   - append s[i:i+length] after "#"
   - `i = j` at the end, and we need to move forward to find number next round
3. `return res`

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
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
