# Simplify Path

## Problem Description

You are given an absolute path for a Unix-style file system, which always begins with a slash `/`. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

- A single period `.` represents the current directory.
- A double period `..` represents the previous/parent directory.
- Multiple consecutive slashes such as `//` and `///` are treated as a single slash `/`.
- Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, `...` and `....` are valid directory or file names.

The simplified canonical path should follow these rules:

- The path must start with a single slash `/`.
- Directories within the path must be separated by exactly one slash `/`.
- The path must not end with a slash `/`, unless it is the root directory.
- The path must not have any single or double periods (`.` and `..`) used to denote current or parent directories.

Return the simplified canonical path.

## Examples

### Example 1

```text
Input: path = "/neetcode/practice//...///../courses"
Output: "/neetcode/practice/courses"
```

### Example 2

```text
Input: path = "/..//"
Output: "/"
```

### Example 3

```text
Input: path = "/..//_home/a/b/..///"
Output: "/_home/a"
```

## Constraints

- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `.`, slash `/` or `_`.
- `path` is a valid absolute Unix path.

---

## UMPIRE

### U - Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a "happy path" test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

### M - Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category.

**Pattern:**

### P - Plan

> - Sketch visualizations and write pseudocode.
> - Walk through a high level implementation with an existing diagram.

### I - Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants).

```python
def simplifyPath(path: str) -> str:
    pass
```

### R - Review

> - Re-check that your algorithm solves the problem by running through important examples.
> - Go through it as if you are debugging it, assuming there is a bug.

**Test with Example 1:**

### E - Evaluate

> - Finish by giving space and run-time complexity.
> - Discuss any pros and cons of the solution.

**Time Complexity:**

**Space Complexity:**
