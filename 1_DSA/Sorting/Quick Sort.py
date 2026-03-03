from typing import List


def quick_sort(arr: List[int], s: int = 0, e: int = None) -> None:
    if e is None:
        e = len(arr) - 1
    if e - s + 1 <= 1:
        return

    pivot = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    arr[e] = arr[left]
    arr[left] = pivot

    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1, e)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("before:", data)
    quick_sort(data)
    print("after: ", data)
