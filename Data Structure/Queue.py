# -*- coding:utf-8 -*-  

class Queue(object):
    def __init__(self, data=None, max_len=16):
        if len(list(data))>max_len:
            raise IndexError("Data size out of range.")
        self._data = list(data) if data else []
        self.max_len = max_len

    def enqueue(self, value):
        self._data.append(value)
        self._data = self._data[-self.max_len:]

    def empty(self):
        return bool(self._data)

    def length(self):
        return len(self._data)

    def capacity(self):
        return self.max_len

    def dequeue(self):
        return self._data.pop(0)
        
    def full(self):
        return len(self._data) == self.max_len
