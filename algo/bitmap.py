# -*- coding:utf-8 -*-
class Bitmap:
    def __init__(self, num_bits):
        self._num_bits = num_bits
        self._bytes = bytearray(num_bits // 8 + 1)
    
    def setbit(self, k):
        if k > self._num_bits or k < 1: return
        self._bytes[k // 8] |= (1 << k % 8)
    
    def getbit(self, k):
        if k > self._num_bits or k < 1: return
        return self._bytes[k // 8] & (1 << k % 8) != 0
