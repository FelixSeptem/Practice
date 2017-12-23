# -*- coding:utf-8 -*-  

import array

class MyArray(object):
    def __init__(self, data, max_len=16):
        if len(data)>max_len:
            raise Exception("DataLengthOverflow", "Data Length longer than the max_len:{}".format(str(max_len)))
        self.myArray = array.array('i')
        self.max_len = max_len

    def size(self):
        return len(self.myArray)

    def capacity(self):
        return self.max_len

    def is_empty(self):
        return bool(self.myArray)

    def push(self, value):
        self.resize()
        return self.myArray.append(value)

    def insert(self, index, value):
        self.resize()
        return self.myArray.insert(index, value)

    def prepend(self, value):
        self.resize()
        return self.myArray.insert(0, value)

    def remove(self, value):
        return self.myArray.remove(value)

    def delete(self, index):
        return self.myArray.pop(index)

    def find(self, value):
        return self.myArray.index(value)

    def resize(self):
        if len(self.myArray)==self.max_len:
            self.max_len *= 2
            self.myArray = array.array('i', self.myArray)
        return 
        
    
            

