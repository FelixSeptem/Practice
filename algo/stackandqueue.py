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
        if len(self.stackPush)==0 && len(self.stackPop)==0:
            return None
        if len(self.stackPop)==0:
            while len(self.stackPush):
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()
    
    def Peek():
        if len(self.stackPush)==0 && len(self.stackPop)==0:
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
        if from==mid || to==mid:
            print("Move 1 from {} to {}".format(from, to))
        else:
            print("Move 1 from {} to {}".format(from, mid))
            print("Move 1 from {} to {}".format(mid, to))
    if from==mid || to==mid:
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

