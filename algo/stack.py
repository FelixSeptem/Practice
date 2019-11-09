# -*- coding:utf-8 -*-  
class Node:
    def __init__(self, data, next):
        self._data = data
        self._next = next
    
class LinkedStack:
    def __init__(self):
        self._top = None
    
    def push(self, value):
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top
    
    def pop(self):
        if self._top:
            value = self._top._data
            self._top = self._top._next
            return value

class NewLinkedStack(LinkedStack):
    def is_empty(self):
        return not self._top

class Browser():
    def __init__(self):
        self.forward_stack = LinkedStack()
        self.back_stack = LinkedStack()

    def can_forward(self):
        if self.back_stack.is_empty():
            return False
        return True

    def can_back(self):
        if self.forward_stack.is_empty():
            return False
        return True

    def open(self, url):
        self.forward_stack.push(url)

    def back(self):
        if self.forward_stack.is_empty():
            return
        top = self.forward_stack.pop()
        self.back_stack.push(top)
        return top

    def forward(self):
        if self.back_stack.is_empty():
            return
        top = self.back_stack.pop()
        self.forward_stack.push(top)
        return top

