# Linear

## Array

| Operation           | Time Complexity | Note                       |
| ------------------- | --------------- | -------------------------- |
| Access by index     | O(1)            | Direct memory address      |
| Search (unsorted)   | O(n)            |                            |
| Search (sorted)     | O(log n)        | Binary search              |
| Insert at end       | O(1)            | Amortized (resize 時 O(n)) |
| Insert at beginning | O(n)            | Shift all elements         |
| Delete at end       | O(1)            |                            |
| Delete at beginning | O(n)            | Shift all elements         |

**Common Questions:**

- What's the difference between array and linked list?
  - Linket List insert O(1), delete O(1), Search O(n)

- When would you use an array vs a linked list?
  - Array: frequent random access, fixed size, cache-friendly
  - Linked List: frequent insert/delete, dynamic size, no random access needed

- How does dynamic array (e.g., Python list) resize?
  - **Grow**: when full → allocate 1.5x~2x capacity → copy elements → free old array
  - **Shrink**: when < 1/4 full → resize to 1/2 capacity (prevents thrashing)
  - Amortized O(1) for insert/delete

- What is the difference between static array and dynamic array?
  - **Static**: fixed size at compile time, stack memory, no resize
  - **Dynamic**: can grow/shrink at runtime, heap memory, amortized O(1) insert

- Why is array access O(1)?
  - Contiguous memory + fixed element size
  - `address = base + (index × size)` → direct calculation

- What happens when you insert into a full dynamic array?
  - Allocate new array (1.5x~2x) → copy all elements → insert new element → free old array
  - This single insert is O(n), but amortized over many inserts → O(1)

- What is cache locality and why are arrays cache-friendly?
  - CPU loads nearby memory into cache together (64 bytes per cache line)
  - Array: contiguous → next element already in cache → fast (spatial locality)
  - Linked List: scattered → each access may cause cache miss → slow

- How would you find duplicates in an array?
  - Use a HashSet. Iterate through array, check if element exists in set - if yes, found duplicate. Otherwise, add it. O(n) time, O(n) space.
  - **Follow-up**: No extra space? → Sort first O(n log n), compare adjacent
  - **Follow-up**: Array is sorted? → Just compare `nums[i] == nums[i+1]`

- How would you rotate an array by k positions?
  - **Slicing (Python)**: `nums[-k:] + nums[:-k]` → O(n) time, O(n) space
  - **Three-reverse (optimal)**: reverse all → reverse first k → reverse rest → O(n) time, O(1) space

- How would you find the missing number in array [0, n]? (e.g., [3,0,1] → missing 2)
  - **Counter**: count each number, iterate 0 to n, return the one with count 0 → O(n) time, O(n) space
  - **Math (optimal)**: `n*(n+1)/2 - sum(nums)` → O(n) time, O(1) space

- How would you move all zeros to the end? (keep relative order of non-zeros)
  - **Two pointers**: slow = next non-zero position, fast scans. When non-zero found, swap. O(n) time, O(1) space

- How would you find the intersection of two arrays?
  - **Set**: `list(set(nums1) & set(nums2))` → O(n+m) time, O(n+m) space
  - **Follow-up**: Arrays are sorted? (e.g., [1,2,2,4,5] & [2,2,4,6] → [2,4])

  ```python
  n = len(nums1)
  m = len(nums2)
  i = 0
  j = 0
  while i < n and j < m:


  ```

  - **Follow-up**: Keep duplicates?

- How would you find the maximum subarray sum?

- How would you merge two sorted arrays in-place?

---

## String

| Operation       | Time Complexity |
| --------------- | --------------- |
| Access by index |                 |
| Concatenation   |                 |
| Substring       |                 |
| Search (find)   |                 |

**Common Questions:**

- Are strings mutable or immutable in Python/Java?
- What's the time complexity of string concatenation in a loop?

---

## Linked List

| Operation                          | Time Complexity |
| ---------------------------------- | --------------- |
| Access by index                    |                 |
| Search                             |                 |
| Insert at head                     |                 |
| Insert at tail (with tail pointer) |                 |
| Insert at middle (given node)      |                 |
| Delete at head                     |                 |
| Delete at tail                     |                 |
| Delete at middle (given node)      |                 |

**Common Questions:**

- How do you detect a cycle in a linked list?
- How do you reverse a linked list?
- What's the difference between singly and doubly linked list?

---

## Stack

| Operation  | Time Complexity |
| ---------- | --------------- |
| Push       |                 |
| Pop        |                 |
| Peek / Top |                 |
| Search     |                 |

**Common Questions:**

- What data structure can you use to implement a stack?
- What's LIFO?
- Give an example of when to use a stack.

---

## Queue

| Operation    | Time Complexity |
| ------------ | --------------- |
| Enqueue      |                 |
| Dequeue      |                 |
| Peek / Front |                 |
| Search       |                 |

**Common Questions:**

- What's FIFO?
- How do you implement a queue using two stacks?
- What's the difference between queue and deque?

---

## Deque

| Operation    | Time Complexity |
| ------------ | --------------- |
| Add front    |                 |
| Add back     |                 |
| Remove front |                 |
| Remove back  |                 |
| Peek front   |                 |
| Peek back    |                 |

**Common Questions:**

- When would you use a deque over a queue?
- How is deque implemented in Python?
