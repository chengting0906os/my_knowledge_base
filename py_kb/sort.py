nums = [3, 2, 1, 5, 4]

nums.sort()
sort_nums = nums.sort()
sorted_nums = sorted(nums)

if __name__ == "__main__":
    print(
        "This script sorts a list of numbers and demonstrates the use of sort and sorted functions."
    )
    print("Original list:", nums)
    print("sort_nums  using sort():", nums)
    print("sorted_num  using sorted():", sorted_nums)
    print("IDs of original and sorted lists:", id(nums), id(sorted_nums))
    print(
        f"Are the nums and sorted_nums the same object? {id(nums) == id(sorted_nums)}"
    )
    print(
        "The sort() method modifies the list in place, while sorted() returns a new sorted list."
    )
    print("End of script.")
