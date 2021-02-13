def searchInsert(nums, target) -> int:
    high_end = len(nums) - 1
    low_end = 0
    mid = (high_end + 1 - low_end) // 2

    if target < nums[0]:
        return 0
    elif target > nums[high_end]:
        return high_end + 1

    while True:
        if target == nums[mid]:
            return mid
        elif high_end == low_end:
            return high_end
        elif nums[high_end] == target:
            return high_end
        elif nums[low_end] == target:
            return low_end
        elif high_end == low_end + 1:
            return low_end + 1
        if target < nums[mid]:
            high_end = mid
            mid -= (high_end - low_end) // 2
        if target > nums[mid]:
            low_end = mid
            mid += (high_end - low_end) // 2

#tests
print(searchInsert([1,3,5,6], 7))


