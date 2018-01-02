# -*- coding:utf-8 -*-  

class Stack(object):
    def __init__(self, data=None, max_len=16):
        if len(list(data))>max_len:
            raise IndexError("Data size out of range.")
        self._data = list(data) if data else []
        self.max_len = max_len

    def insert(self, value):
        if self.size()==self.max_len:
            raise IndexError("Data size out of range.")
        self._data.append(value)
        return self._data

    def pop(self):
        return self._data.pop()

    def size(self):
        return len(self._data)

    def capacity(self):
        return self.max_len