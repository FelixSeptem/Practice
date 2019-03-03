# -*- coding:utf-8 -*-  
'''
实现一个特殊的栈，在实现基本功能的基础上，还需要实现返回最小元素的方法
* pop,push,getMin的时间复杂度都是O(1)
'''
class Stack:
    def __init__(self):
        self.stackData = []
        self.minStack = []

    def Len(item):
        return len(self.stackData)
    
    def Push(item):
        self.stackData.append(item)
        if len(self.minStack)==0:
            self.minStack.append(item)
        elif item<self.minStack[-1]:
            self.minStack.append(item)
    
    def Pop():
        if len(self.stackData)==0:
            return None
        v = self.stackData.pop()
        if v==self.minStack[-1]:
            self.minStack.pop()
        
    def GetMin():
        if len(self.minStack)==0:
            return None
        return self.minStack[-1]

'''
用两个栈实现队列，实现队列的基本操作
'''
class Queue:
    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    def Add(item):
        self.stackPush.append(item)

    def Poll():
        if len(self.stackPush)==0 and len(self.stackPop)==0:
            return None
        if len(self.stackPop)==0:
            while len(self.stackPush):
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()
    
    def Peek():
        if len(self.stackPush)==0 and len(self.stackPop)==0:
            return None
        if len(self.stackPop)==0:
            while len(self.stackPush):
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop[-1]

'''
如何仅用递归函数和栈操作逆序一个栈
一个栈依次入栈1,2,3；从栈顶到栈底是3,2,1;逆序之后从栈顶到栈底是1,2,3;不允许使用其他数据结构
'''
def getAndRemoveLastItem(stack):
    i = stack.pop()
    if len(stack)==0:
        return i
    else:
        last = getAndRemoveLastItem(stack)
        stack.append(i)
        return last

def reverse(stack):
    if len(stack)==0:
        return stack
    i = getAndRemoveLastItem(stack)
    reverse(stack)
    stack.append(i)

'''
用一个栈实现另一个栈的排序
如何把一个栈内的元素排序，只允许额外申请一个栈和变量
'''
def sortStack(stack):
    if len(stack)==0:
        return stack
    help = []
    while len(stack):
        cur = stack.pop()
        if len(help)==0:
            help.append(cur)
        if cur<=help[-1]:
            help.append(cur)
        else:
            while help[-1]>cur and len(help)>0:
                stack.append(help.pop())
            help.append(cur)

'''
用栈实现汉诺塔问题
最上层为1层，其次2层，以此类推
'''
def hanoi(n, left, mid, right):
    if n<1:
        return None
    return move(n, left, mid, right, left, right)

def move(n, left, mid, right, from, to):
    if n==1:
        if from==mid or to==mid:
            print("Move 1 from {} to {}".format(from, to))
        else:
            print("Move 1 from {} to {}".format(from, mid))
            print("Move 1 from {} to {}".format(mid, to))
    if from==mid or to==mid:
        another=(from==left || to==left)?right:left
        part1 = move(n-1, left, mid, right, from, another)
        part2 = 1
        print("Move {} from {} to {}".format(n, from, to))
        part3 = move(n-1, left, mid, right, another, to)
    else:
        part1 = move(n-1, left, mid, right, from, to)
        part2 = 1
        print("Move {} from {} to {}".format(n, from, mid))
        part3 = move(n-1, left, mid, right, to, from)
        part4 = 1
        print("Move {} from {} to {}".format(n, mid, to))
        part5 = move(n-1, left, mid, right, from, to)

'''
生成窗口最大值数组
有一个整数数组arr和一个大小为w的窗口，从数组最左滑动到最右：
例如，有数组[4,3,5,4,3,3,6,7],窗口大小为3：
[4 3 5] 4 3 3 6 7 max = 5
4 [3 5 4] 3 3 6 7 max = 5
4 3 [5 4 3] 3 6 7 max = 5
4 3 5 [4 3 3] 6 7 max = 4
4 3 5 4 [3 3 6] 7 max = 6
4 3 5 4 3 [3 6 7] max = 7
input: arr=[4,3,5,4,3,3,6,7], n=3
output:[5,5,5,4,6,7]
'''
def getMaxWindow(arr, w):
    from collections import deque
    if not arr || w < 1:
        return None
    if len(arr)<w:
        return max(arr)
    qmax = deque(maxlen=w)
    res = []
    for i in range(len(arr)):
        while (not qmax) and arr[qmax[-1]]<arr[i]:
            qmax.pop()
        qmax.append(i)
        if qmax[0] == i-w:
            qmax.popleft()
        if i>=w-1:
            res.append(arr[qmax[0]])
    return res

'''
求最大子矩阵的大小
给定一个整形矩阵map,其中值为0和1，求全为1的矩阵区域中，最大矩形区域1的数量。
例如:
input:
1 1 1 0
output:
3
input:
1 0 1 1
1 1 1 1
1 1 1 0
output:
6
'''
def maxRecFromBottom(height):
    if not height:
        return 0
    maxArea = 0
    stack = []
    for i in range(len(height)):
        while stack and height[i]<=height[stack[-1]]:
            j = stack.pop()
            k = -1 if not stack else stack[-1]
            curArea = (i - k - 1)*height[j]
            maxArea = max(maxArea, curArea)
        stack.append(i)
    while stack:
        j = stack.pop()
        k = -1 if not stack else stack[-1]
        curArea = (len(height) - k - 1)*height[j]
        maxArea = max(maxArea, curArea)
    return maxArea

def maxRecSize(map):
    if (not map) or (not map[0]):
        return 0
    maxArea = 0
    height = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            height[j] = 0 if map[i][j]==0 else height[j] + 1
        maxArea = max(maxRecFromBottom(height), maxArea)
    return maxArea

'''
最大值减去最小值小于或等于num的子数组数量
给定数组arr和整数num，共返回多少子数组满足：
max(arr[i..j]) - min(arr[i..j])<=num
'''
def getNum(arr, num):
    from collections import deque
    if not arr:
        return 0
    qmin, qmax = deque(), deque()
    i,j,res = 0,0,0
    while i<len(arr):
        while j<len(arr):
            while qmin && arr[qmin[-1]] > arr[j]:
                qmin.popleft()
            qmin.append(j)
            while qmax && arr[qmax[-1]] <= arr[j]:
                qmax.popleft()
            qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j++
        if qmin[0]==i:
            qmin.popleft()
        if qmax[0]==i:
            qmax.popleft()
        res += j - i
        i++
    return res
