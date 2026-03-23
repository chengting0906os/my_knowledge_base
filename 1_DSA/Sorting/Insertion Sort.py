from typing import List


def insertion_sort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("before:", data)
    insertion_sort(data)
    print("after: ", data)

# Time Complexity
# Best:    O(n)
#   array is already sorted → inner while loop never runs
#
# Average / Worst: O(n²)
#   each element i may need to shift past all i previous elements
#   total shifts ≈ 1 + 2 + ... + (n-1) = n(n-1)/2 → O(n²)
#
# Space Complexity: O(1)
#   fully in-place — shifts elements within the array
#
# Note: stable — strict > comparison ensures equal elements keep original order
#   also adaptive: faster on nearly-sorted input
