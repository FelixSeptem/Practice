# -*- coding:utf-8 -*-
class TrieNode:
    def __init__(self, data: str):
        self._data = data
        self._children = [None] * 26
        self._is_ending_char = False
    

class Trie:
    def __init__(self):
        self._root = TrieNode("/")

    def insert(self, text: str) -> None:
        node = self._root
        for index, char in map(lambda x: (ord(x) - ord("a"), x), text):
            if not node._children[index]:
                node._children[index] = TrieNode(char)
            node = node._children[index]
        node._is_ending_char = True
    
    def find(self, pattern: str) -> bool:
        node = self._root
        for index in map(lambda x: ord(x) - ord("a"), pattern):
            if not node._children[index]: return False
            node = node._children[index]
        return node._is_ending_char