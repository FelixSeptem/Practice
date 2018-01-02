# -*- coding:utf-8 -*-  


def insert_sort(lists):
    '''
    插入排序
    Best: O(n)
    Average: O(n^2)
    Worst: O(n^2)
    '''
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


def shell_sort(lists):
    '''
    希尔排序
    Best: O(nlog(n))
    Average:　O(nlog(n)^2)
    Worst: O(nlog(n)^2)
    '''
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists


def bubble_sort(lists):
    '''
    冒泡排序
    Best: O(n)
    Avergae: O(n^2)
    Worst: O(n^2)
    '''
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def quick_sort(lists, left, right):
    '''
    快速排序
    Best: O(nlog(n))
    Average: O(nlog(n))
    Worst: O(n^2)
    '''
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
'''
def quicksort(seq):
    if len(seq) <= 1: 
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)

def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi
'''


def select_sort(lists):
    '''
    选择排序
    Best: O(n^2)
    Average: O(n^2)
    Worst: O(n^2)
    '''
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)
def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)
def heap_sort(lists):
    '''
    堆排序
    Best: O(nlog(n))
    Average: O(nlog(n))
    Worst: O(nlog(n))
    '''
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
def merge_sort(lists):
    '''
    归并排序
    Best: O(nlog(n))
    Average: O(nlog(n))
    Worst: O(nlog(n))
    '''
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


import math
def radix_sort(lists, radix=10):
    '''
    基数排序
    Best: O(nk)
    Average: O(nk)
    Worst: O(nk)
    '''
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists


def timsort(the_array):
    '''
    timsort
    Best: O(n)
    Averagr: O(nlog(n))
    Worst: O(nlog(n))
    Python中的sorted()方法
    '''
    runs, sorted_runs = [], []
    l = len(the_array)
    new_run = [the_array[0]]
    for i in range(1, l):
        if i == l-1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        if the_array[i] < the_array[i-1]:
            if not new_run:
                runs.append([the_array[i-1]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(the_array[i])
    for each in runs:
        sorted_runs.append(insert_sort(each))
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)
    print sorted_array


def bucket_sort(seq):
    '''
    桶排序
    Best: O(n+k)
    Average: O(n+k)
    Worst: O(n^2)
    '''
    biggest = 0
    for number in seq:
        if number > biggest:
            biggest = number
    buckets = []
    buckets.append([]) * (biggest / 10 + 1)
    for number in seq:
        buckets[number / 10].append(number)
    for index, bucket in enumerate(buckets):
        #Using quicksort to sort individual buckets
        buckets[index] = quick_sort(bucket)
    new_list = [number for number in bucket for bucket in buckets]
    return new_list


def counting_sort(array):
    '''
    计数排序
    Best: O(n+k)
    Average: O(n+k)
    Worst: O(n+k)
    '''
    maxval = max(array)
    m = maxval + 1
    count = [0] * m              
    for a in array:
        count[a] += 1           
    i = 0
    for a in range(m):            
        for c in range(count[a]):
            array[i] = a
            i += 1
    return (array,count)
