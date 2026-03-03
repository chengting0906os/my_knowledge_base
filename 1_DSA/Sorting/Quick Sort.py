import random
from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    left, mid, right = [], [], []
    pivot = random.choice(arr)

    for val in arr:
        if val < pivot:
            left.append(val)
        elif val == pivot:
            mid.append(val)
        else:
            right.append(val)

    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("before:", data)
    data = quick_sort(data)
    print("after: ", data)

# Time Complexity
# Best / Average:  O(n log n)
#   pivot splits the array into two halves → recursion depth is log n
#   each level scans all n elements to partition → O(n) per level
#   total: O(n log n)
#
# Worst:           O(n²)
#   pivot is always the min or max → one side has n-1, the other 0
#   recursion depth degrades to n levels, each still O(n) → O(n²)
#   using random.choice() greatly reduces the chance of this happening
#
# Space Complexity: O(n)
#   each call creates new left / mid / right lists
#   total extra space across all levels = O(n)
#   in-place partition (pointer swap) would reduce this to O(log n) (call stack only)
