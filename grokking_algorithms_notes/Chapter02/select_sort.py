# -*- coding:utf-8 -*-  
def get_min(arr):
    if len(arr) == 0:
        return
    if len(arr) == 1:
        return arr[0]
    miniest = arr[0]
    for i in range(arr[1:]):
        if arr[i] < miniest:
            miniest = arr[i]
    return miniest

def select_sort(arr):
    result = []
    while len(arr)>0:
        result.append(arr.pop(get_min(arr)))
    return result