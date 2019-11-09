# -*- coding:utf-8 -*-  
def  bubble_sort(arr):
    length = len(arr)
    if length<2:
        return arr
    for i in range(length):
        is_sorted = True
        for j in range(length - i - 1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted:
            break

def insert_sort(arr):
    length = len(arr)
    if length<2:
        return arr
    for i in range(1, length):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value

def select_sort(arr):
    length = len(arr)
    if length < 2:
        return
    for i in range(length):
        min_index = i
        min_val = arr[i]
        for j in range(i, length):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def merge_sort(a):
    _merge_sort_between(a, 0, len(a) - 1)


def _merge_sort_between(a, low, high):
    # The indices are inclusive for both low and high.
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort_between(a, low, mid)
        _merge_sort_between(a, mid + 1, high)
        _merge(a, low, mid, high)


def _merge(a, low, mid, high):
    # a[low:mid], a[mid+1, high] are sorted.
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp


def quick_sort(a):
    _quick_sort_between(a, 0, len(a) - 1)


def _quick_sort_between(a, low, high):
    if low < high:
        # get a random position as the pivot
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]

        m = _partition(a, low, high)  # a[m] is in final position
        _quick_sort_between(a, low, m - 1)
        _quick_sort_between(a, m + 1, high)


def _partition(a, low, high):
    pivot, j = a[low], low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]  # swap
    a[low], a[j] = a[j], a[low]
    return j

def q_sort(a):
    if len(a)<2:
        return a
    pivot = a[0]
    small = [i for i in range(a) if i<pivot]
    big = [i for i in range(a) if i>pivot]
    return q_sort(small) + [pivot] + q_sort(big)

def QuickSort(arr):
    # 双向排序: 提高非随机输入的性能
    # 不需要额外的空间,在待排序数组本身内部进行排序
    # 基准值通过random随机选取
    # 入参: 待排序数组, 数组开始索引 0, 数组结束索引 len(array)-1
    import random
    if len(arr) < 2:
        return arr

    def QuickSort_TwoWay(arr, low, upper):
        # 小数组排序i可以用插入或选择排序
        # if upper-low < 50 : return arr
        # 基线条件: low index = upper index; 也就是只有一个值的区间
        if low >= upper:
            return arr
        # 随机选取基准值, 并将基准值替换到数组第一个元素
        pivot = random.uniform(low, upper))
        arr[low], arr[pivot] = arr[pivot], arr[low]
        temp = arr[low]
        # 缓存边界值, 从上下边界同时排序
        i, j = low, upper
        while True:
            # 第一个元素是基准值,所以要跳过
            i += 1
            # 在小区间中, 进行排序
            # 从下边界开始寻找大于基准值的索引
            while i <= upper and arr[i] <= temp:
                i += 1
            # 从上边界开始寻找小于基准值的索引
            # 因为j肯定大于i, 所以索引值肯定在小区间中
            while arr[j] > temp:
                j -= 1
            # 如果小索引大于等于大索引, 说明排序完成, 退出排序
            if i >= j:
                break
            swap(arr, i, j)
        # 将基准值的索引从下边界调换到索引分割点
        swap(arr, low, j)
        QuickSort_TwoWay(arr, low, j - 1)
        QuickSort_TwoWay(arr, j + 1, upper)
        return arr

    return QuickSort_TwoWay(arr, 0, len(arr) - 1)



def _partition(nums, l, r):
    ind = random.randint(l, r)
    nums[l], nums[ind] = nums[ind], nums[l]
    base = nums[l]
    lt = l  # nums[l+1...lt] < base
    gt = r + 1  # nums[gt...r] > base
    i = l + 1  # nums[lt+1...i] == base
    while (i < gt):
        # i==gt时表示已经比较结束
        if (nums[i] < base):
            nums[i], nums[lt+1] = nums[lt+1], nums[i]
            lt += 1
            i += 1
        elif (nums[i] > base):
            nums[i], nums[gt-1] = nums[gt-1], nums[i]
            gt -= 1
        else:  # nums[i] == base
            i += 1
        print(nums)
    nums[l], nums[lt] = nums[lt], nums[l]
    print(nums)
    return lt, gt


def _quick_sort(nums, l, r):
    if l < r:
        lt, gt = _partition(nums, l, r)
        _quick_sort(nums, l, lt - 1)
        _quick_sort(nums, gt, r)


def quick_sort_threeway(nums):
    l, r = 0, len(nums) - 1
    _quick_sort(nums, l, r)


def counting_sort(a):
    if len(a) <= 1: 
        return
    
    counts = [0] * (max(a) + 1)
    for num in a:
        counts[num] += 1
    counts = list(itertools.accumulate(counts))

    a_sorted = [0] * len(a)
    for num in reversed(a):
        index = counts[num] - 1
        a_sorted[index] = num
        counts[num] -= 1    
    a[:] = a_sorted