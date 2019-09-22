# -*- coding:utf-8 -*-  
def qsort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        small = [x for x in arr[1:] if x<pivot]
        big = [x for x in arr[1:] if x>pivot]
    return qsort(small) + pivot + qsort(big)