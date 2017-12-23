# -*- coding:utf-8 -*-  

class Node(object):
    def __init__(self, data, next=None):
        self._data = data
        self.next = None

    def __str__(self):
        return 'Node:{}'.format(self._data)

    def __bool__(self):
        return self.next!=None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next(self):
        return self.next

    def set_next(next):
        self.next = next


class LinkedList(self):
    def __init__(self, head=None):
        self._head = head

    def set_head(self, head):
        self._head = head

    def __len__(self):
        count = 0
        current = self._head
        while current:
            count += 1
            current = current.get_next()
        return count

    def size(self):
        return self.__len__()

    def empty(self):
        return bool(self._head)

    def value_at(self, index):
        current = self._head
        if index<0:
            raise IndexError("Not implement minus index.")
        while index:
            index -= 1
            current = current.get_next()
            if not current:
                raise IndexError("Index out of range!")
        return current

    def push_front(self, node):
        node.set_next(self._head)
        self.set_head(node)

    def pop_front(self):
        if self._head:
            self.set_head(self._head.get_next())
        else:
            raise IndexError("Unable pop an item from empty linkedlist.")

    def contains(self, value):
        current = self._head
        while current:
            if current.get_data() == value:
                return True
            current = current.get_next()
        return False

    def append(self, node):
        current = self._head
        if not current:
            self.set_head(node)
            return 
        while current.get_next():
            current = current.get_next()

        current.set_next(node)

    def pop_back(self):
        current = self._head
        if not current:
            raise IndexError("Unable delete an item from empty linkedlist.")
        while current.get_next().get_next():
            current = current.get_next()
        tmp = current.get_next()
        current.set_next(None)
        return tmp

    def delete(self, index):
        if index == 0:
            if not self._head:
                raise IndexError("Unable delete an item from empty linkedlist.")
            self.set_head(self._head.get_next())
            return self._head
        current = self._head
        while index>1:
            index -= 1
            current = current.get_next()
            if not current:
                raise IndexError("Index out of range.")
        current.set_next(current.get_next().get_next())
        return self._head

    def remove(self, value):
        current = self._head
        if not current:
            raise IndexError("Unable remove an item from empty linkedlist.")
        if self._head.get_data() == value:
            self.set_head(self._head.get_next())
        while current:
            if current.get_next().get_data() == value:
                current.set_next(current.get_next().get_next())
                return self._head
            current = current.get_next()
        return current

    def getKthToTail(self, k):
        if k<=0:
            raise IndexError("Unable accept a zero or minus index.")
        q = p = self._head
        for i in range(k-1):
            q = q.get_next()
            if not q:
                raise IndexError("Index out of range.")
        while q.get_next():
            q = q.get_next()
            p = p.get_next()
        return p
    
