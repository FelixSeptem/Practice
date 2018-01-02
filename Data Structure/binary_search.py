# -*- coding:utf-8 -*-  

def binary_search(array, target):
    first = 0
    last = len(array) - 1

    while first <= last:
        i = first + (last - first) / 2

        if array[i] == target:
            return i
        elif array[i] > target:
            last = i - 1
        elif array[i] < target:
            first = i + 1
    return -1