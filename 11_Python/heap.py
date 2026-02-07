import heapq

nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
h_queue = []

for value in nums:
    heapq.heappush(h_queue, value)

result = [heapq.heappop(h_queue) for _ in range(len(h_queue))]


if __name__ == "__main__":
    print("This script demonstrates the use of the heapq module to create a min-heap.")
    print("Original list:", nums)
    print("Sorted list using heapq:", result)
    print("IDs of original and sorted lists:", id(nums), id(result))
    print(f"Are the nums and result the same object? {id(nums) == id(result)}")
    print("The heapq module provides an efficient way to maintain a priority queue.")
    print("End of script.")
    print(
        "The heapq module is useful for implementing algorithms that require a priority queue."
    )
    print("It allows for efficient insertion and extraction of the smallest element.")
    print("This is particularly useful in algorithms like Dijkstra's shortest path.")
