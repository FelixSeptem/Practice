# -*- coding:utf-8 -*-  
class MyArray:
    def __init__(self, capacity):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position):
        return self._data[position]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index):
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index):
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index, value):
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def get_all(self):
        return self._data