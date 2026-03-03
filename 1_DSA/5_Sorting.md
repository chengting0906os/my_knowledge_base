# Sorting Algorithms Cheat Sheet

Sorting algorithms are non-negotiable for coding interviews. You should know each algorithm's time/space complexity and whether it is stable.

| # | Algorithm | Best | Average | Worst | Space (Worst) | Stable |
|---|---|---|---|---|---|---|
| 1 | Quick Sort | `O(n log n)` | `O(n log n)` | `O(n^2)` | `O(n)` | No |
| 2 | Merge Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes |
| 3 | Heap Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(1)` | No |
| 4 | Insertion Sort | `O(n)` | `O(n^2)` | `O(n^2)` | `O(1)` | Yes |
| 5 | Timsort | `O(n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes |
| 6 | Bubble Sort | `O(n)` | `O(n^2)` | `O(n^2)` | `O(1)` | Yes |
| 7 | Shellsort | `O(n log n)` | Depends on gap sequence | `O(n^2)` | `O(1)` | No |
| 8 | Bucket Sort | `O(n + k)` | `O(n)` | `O(n^2)` | `O(n)` | Depends |
| 9 | Radix Sort | `O(nk)` | `O(nk)` | `O(nk)` | `O(n + k)` | Yes (if stable sub-sort is used) |
| 10 | Counting Sort | `O(n + k)` | `O(n + k)` | `O(n + k)` | `O(k)` | Yes |
| 11 | Selection Sort | `O(n^2)` | `O(n^2)` | `O(n^2)` | `O(1)` | No |

`k` notes:
- Bucket Sort: number of buckets
- Radix Sort: number of digits
- Counting Sort: size of value range
