# -*- coding:utf-8 -*-  
'''
第一章主要介绍了大O表示法（https://en.wikipedia.org/wiki/Time_complexity）
'''
def binary_search(list, item):
    low, high = 0, len(list) - 1
    while low <= high:
        mid = low + (high - low)/2
        piv = list[mid]
        if piv == item:
            return mid
        if piv > item:
            high = mid - 1
        else:
            low = mid + 1
        return -1
