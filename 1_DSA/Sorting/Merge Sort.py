from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("before:", data)
    data = merge_sort(data)
    print("after: ", data)

# Time Complexity
# Best / Average / Worst: O(n log n)
#   always splits the array in half → recursion depth is always log n
#   each level merges all n elements → O(n) per level
#   total: O(n log n) regardless of input
#
# Space Complexity: O(n)
#   creates new left / right / result lists at each level
#   total extra space = O(n)
#   unlike Quick Sort, there is no in-place variant that avoids this
