# -*- coding:utf-8 -*-  


def insert_sort_1(lists):
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


def insert_sort_2(lists):
    n = len(lists)
    for i in range(1, n):
        x = lists[i]
        p = binary_search(lists[:i], x)
        for j in range(i, p, -1):
            lists[j] = lists[j-1]
        lists[p] = x
    return lists

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


def insert_sort_3(lists):
    n = len(lists)
    next = [-1]*(n+1)
    for i in range(n):
        insert1(lists, next, i)
    return reorder(lists, next)

def insert1(xs, next, i):
    j = -1
    while next[j] != -1 and xs[next[j]] < xs[i]:
        j = next[j]
    next[j], next[i] = i, next[j]

def reorder(xs, next):
    i = -1
    ys = []
    while next[i] != -1:
        ys.append(xs[next[i]])
        i = next[i]
    return ys