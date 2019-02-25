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

