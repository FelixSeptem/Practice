# -*- coding:utf-8 -*-  
def bucket_sort(arr):
    range_small, range_big = min(arr), max(arr)
    temp = [0 for _ in range(range_small, range_big+1)]
    result = []
    for i in range arr:
        temp[i-range_small] += 1
    for i, v in range temp.items():
        for _ in range temp:
            result.append(i)
    return result

def bubble_sort(arr):
    count = len(arr)
    for i in range(0, count):
        for j in range(i + 1, count-i+1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def qsort(arr):
    if len(arr)<1:
        return arr
    pivot = arr[0]
    small = [x for x in arr if x < pivot]
    big = [x for x in arr if x >= pivot]
    return qsort[small] + [pivot] + qsort[big]

def qsort2(arr):
    def partition(arr, left, right, pivot):
        target = arr[pivot]
        while left!=right:
            while arr[right]>=pivot:
                right -= 1
            while arr[left]<=target:
                left += 1
            if left<right:
                arr[left], arr[right] = arr[right], arr[left]
        arr[pivot] = arr[left]
        return left
    
    pivot = partition(arr, 0, len(arr), arr[0])
    qsort2(arr[:pivot], 0, pivot-1, arr[0])
    qsort2(arr[pivot+1:], pivot, len(arr), arr[pivot+1])  

# 有序列表去重
def dedup(arr):
    pivot = 0
    deleted = 0
    stop = len(arr)
    while pivot+deleted < stop:
        if arr[pivot]==arr[pivot+1]:
            remove(arr, pivot+1)
        else:
            pivot += 1
    return arr

# 并查集
class UnionFindSet(object):
    """并查集"""
    def __init__(self, data_list):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find_head(self, node):
        """使用递归的方式来查找父节点

        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        father = self.father_dict[node]
        if(node != father):
            father = self.find_head(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find_head(node_a) == self.find_head(node_b)

    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find_head(node_a)
        b_head = self.find_head(node_b)

        if(a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if(a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size