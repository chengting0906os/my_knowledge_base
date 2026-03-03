# Sorting Algorithms Cheat Sheet

Sorting algorithms are non-negotiable for coding interviews. You must understand how different sorting algorithms stack up against each other — their time and space complexities and whether or not they're **stable**.

![Sorting Algorithms Cheatsheet](image/sorting%20cheetsheet.png)

---

## Complexity Summary

| Algorithm      | Best       | Average        | Worst      | Space (Worst) | Stable? |
| -------------- | ---------- | -------------- | ---------- | ------------- | ------- |
| Quick Sort     | O(n log n) | O(n log n)     | O(n²)      | O(n)          | No      |
| Merge Sort     | O(n log n) | O(n log n)     | O(n log n) | O(n)          | Yes     |
| Heap Sort      | O(n log n) | O(n log n)     | O(n log n) | O(1)          | No      |
| Insertion Sort | O(n)       | O(n²)          | O(n²)      | O(1)          | Yes     |
| Timsort        | O(n)       | O(n log n)     | O(n log n) | O(n)          | Yes     |
| Bubble Sort    | O(n)       | O(n²)          | O(n²)      | O(1)          | Yes     |
| Shellsort      | O(n log n) | depends on gap | O(n²)      | O(1)          | No      |
| Bucket Sort    | O(n + k)   | O(n)           | O(n²)      | O(n)          | Yes     |
| Radix Sort     | O(nk)      | O(nk)          | O(nk)      | O(n + k)      | Yes     |
| Counting Sort  | O(n + k)   | O(n + k)       | O(n + k)   | O(k)          | Yes     |
| Selection Sort | O(n²)      | O(n²)          | O(n²)      | O(1)          | No      |

> **k** = number of buckets / digits / value range depending on algorithm

---

## Notes

- **Stable sort** preserves the relative order of equal elements.
- **Quick Sort** is fastest in practice (cache-friendly) but worst-case O(n²).
- **Merge Sort** is preferred when stability is required.
- **Heap Sort** is in-place but not stable.
- **Timsort** is Python's built-in sort (hybrid of Merge + Insertion Sort).
- **Counting / Radix / Bucket Sort** are non-comparison sorts — can beat O(n log n) lower bound under specific conditions.
