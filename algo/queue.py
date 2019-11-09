# -*- coding:utf-8 -*-  
class ArrayQueue:
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True
    
    def dequeue(self):
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self._next = next

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node
    
    def dequeue(self):
        if self._head:
            value = self._head.data
            self._head = self._head._next
            if not self._head:
                self._tail = None
            return value

class CircularQueue:
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity + 1
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        if (self._tail + 1) % self._capacity == self._head:
            return False
        self._items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self):
        if self._head != self._tail:
            item = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            return item

class DynamicArrayQueue:
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0
    
    def enqueue(self, item):
        if self._tail == self._capacity:
            if self._head == 0: 
                return False
            self._items[0 : self._tail - self._head] = self._items[self._head : self._tail]
            self._tail -= self._head
            self._head = 0
        if self._tail == len(self._items):
            self._items.append(item)
        else:
            self._items[self._tail] = item
        self._tail += 1
        return True

    def dequeue(self):
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item

