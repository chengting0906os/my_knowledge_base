from typing import List


def bubble_sort(arr: List[int]) -> None:
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:  # already sorted — early exit
            break


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("before:", data)
    bubble_sort(data)
    print("after: ", data)

# Time Complexity
# Best:    O(n)
#   array is already sorted → inner loop makes no swaps → exits after one pass
#
# Average / Worst: O(n²)
#   each of the n passes bubbles the largest unsorted element to its place
#   inner loop does n-i-1 comparisons per pass → total ≈ n²/2 comparisons
#
# Space Complexity: O(1)
#   fully in-place — only a constant number of variables used
#
# Note: stable — equal elements are never swapped (strict > comparison)
