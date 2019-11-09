# -*- coding:utf-8 -*-  
def bsearch(nums, target) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

def bsearch(nums, target):
    return bsearch_internally(nums, 0, len(nums)-1, target)


def bsearch_internally(nums, low, high, target):
    if low > high:
        return -1

    mid = low+int((high-low) >> 2)
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return bsearch_internally(nums, mid+1, high, target)
    else:
        return bsearch_internally(nums, low, mid-1, target)


def bsearch_left(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low < len(nums) and nums[low] == target:
        return low
    else:
        return -1


def bsearch_right(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and nums[high] == target:
        return high
    else:
        return -1


def bsearch_left_not_less(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low < len(nums) and nums[low] >= target:
        return low
    else:
        return -1

def bsearch_right_not_greater(nums, target) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and nums[high] <= target:
        return high
    else:
        return -1