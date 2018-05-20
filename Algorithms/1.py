# -*- coding:utf-8 -*-  

# 最小ID
# 寻找数组中未出现的最小非负整数,数组内包含无重复非负整数
# 例如：
# Input:
# [18, 4, 8, 9, 16, 1, 14, 7, 19, 3, 0, 5, 2, 11, 6]
# Output:
# 10

# O(n^2)
def find_min_1(array):
    x = 0
    while True:
        if x not in array:
            return x
        x += 1

# O(n) 需要额外空间
def find_min_2(array):
    length = len(array)
    x = [0 for _ in xrange(length)]
    for i in array:
        if i < length-1:
            x[i] = 1
    return x.index(0)

# O(n) 不需要额外空间
def find_min_3(array):
    length = len(array)
    left, right = 0, length - 1
    n = 1
    while n:
        mid = (left+right)/2
        front = 0
        for tail in range(len(array)):
            if array[tail] <= mid:
                array[tail], array[front] = array[front], array[tail]
                front += 1
        if left == mid-left+1:
            array = array[left:]
            n = n-left
            left = mid+1
        else:
            n = front
            right = mid
    return left

# 丑数
# 只包含2,3,5三个因子的自然数叫做丑数，找出第1500个丑数，第一个丑数是1

def is_ugly(num):
    while num%2==0:
        num /= 2
    while num%3==0:
        num /= 3
    while num%5==0:
        num /= 5
    return num==1

def find_ugly_1(n):
    start, count = 0, 0
    if is_ugly(start):
        count += 1
        if count == n:
            return start
        start += 1

def find_ugly_2(n):
    if n <= 0:  
        return 0  
    if n == 1:  
        return 1  
    numbers = [1]  
    i2, i3, i5 = 0, 0, 0  
    for k in range(n-1):  
        n2, n3, n5 = numbers[i2] * 2, numbers[i3] * 3, numbers[i5] * 5  
        Min = min(n2, n3, n5)  
        numbers.append(Min)  
        i2 += (Min == n2)  
        i3 += (Min == n3)  
        i5 += (Min == n5)  
    return Min  

        
