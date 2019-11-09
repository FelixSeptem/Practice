# -*- coding:utf-8 -*-  
class Node:
    
    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node


class SinglyLinkedList:

    def __init__(self):
        self._head = None

    def find_by_value(self, value):
        p = self._head
        while p and p.next_node!=None:
            if p.value == value:
                return p
        return None

    def find_by_index(self, index):
        p = self._head
        position = 0
        while p and position != index:
            p = p._next
            position += 1
        return p

    def insert_node_to_head(self, new_node):
        if new_node:
            new_node._next = self._head
            self._head = new_node

    def insert_node_after(self, node, new_node):
        if not node or not new_node:
            return
        new_node._next = node._next
        node._next = new_node

    def insert_node_before(self, node, new_node):
        if not self._head or not node or not new_node:
            return
        if self._head == node:
            self.insert_node_to_head(new_node)
            return
        current = self._head
        while current._next and current._next != node:
            current = current._next
        if not current._next:  # node is not even in the list
            return
        new_node._next = node
        current._next = new_node

    def delete_by_node(self, node):
        if node.next_node == None: # if node is tail
            node = None
        node.value = node.next_node.value
        node.next_node = node.next_node.next_node

    def delete_by_value(self, value: int):
        if not self._head or not value:
            return
        fake_head = Node(value + 1)
        fake_head._next = self._head
        prev, current = fake_head, self._head
        while current:
            if current.data != value:
                prev._next = current
                prev = prev._next
            current = current._next
        if prev._next:
            prev._next = None
        self._head = fake_head._next  # in case head.data == value

    def delete_tail(self):
        if not self._head:
            return 
        if not self._head.next_node:
            self._head = None
            return
        pre, tail = self._head, self._head.next_node
        while tail:
            pre = pre.next_node
            tail = tail.next_node
        pre.next_node = None
        tail = None

    def __iter__(self):
        node = self._head
        while node:
            yield node.data
            node = node._next

# 回文字符串判断
def reverse(head):
    reverse_head = None
    while head:
        next_node = head.next_node
        head.next_node = reverse_head
        reverse_head = head
        head = next_node
    return reverse_head

def is_palindrome(l):
    if not l or not l.next_node:
        return True
    reversed_l = reverse(l)
    p1, p2 = l, reversed_l
    while p1!=None and p2!=None:
        if p1.value != p2.value:
            return False
        p1 = p1.next_node
        p2 = p2.next_node
    return True

# LRU
class CacheData:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRU:
    def __init__(self, capacity):
        self.data = SinglyLinkedList()
        self.cache = {}
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            v = self.cache[key]
            c = self.data.find_by_value(CacheData(key, v))
            self.data.delete_by_node(c)
            self.data.insert_node_to_head(CacheData(key, v))
            return v
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            old_v = self.cache[key]
            c = self.data.find_by_value(CacheData(key, old_v))
            self.data.delete_by_node(c)
            self.data.insert_node_to_head(CacheData(key, value))
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                c = self.data.delete_tail()
            self.data.insert_node_to_head(CacheData(key, value))
            self.cache[key] = value
           
# 链表反转
def reverse(head):
    if not head or not head.next_node:
        return head
    current = head
    reverse_head = None
    while current:
        reverse_head, reverse_head.next, current = current, reverse_head, current.next_node
    return reverse_head

# 检测环
def has_circle(head):
    if not head or not head.next_node:
        return False
    fast, slow = head.next_node, head
    while fast:
        if fast == slow:
            return True
        slow = slow.next_node
        fast = fast.next_node.next_node
    return False

# 有序链表合并
def merge_ordered_linked_list(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    p1, p2 = l1, l2
    if p1.value<p2.value:
        result = p1
        p1 = p1.next_node
    else:
        result = p2
        p2 = p2.next_node
    while p1 and p2:
        if p1<p2:
            result.next_node = p1
            p1 = p1.next_node
        else:
            result.next_node = p2
            p2 = p2.next_node
    if p1:
        result.next_node = p1
        return result
    result.next_node = p2
    return result

# 删除倒数第k个节点
def remove_kth_from_end(head, k):
    fast = head
    count = 0
    while fast and count < n:
        fast = fast.next_node
        count += 1
    if not fast and count < n:  # not that many nodes
        return head
    if not fast and count == n:
        return head.next_node
    
    slow = head
    while fast._next:
        fast, slow = fast._next, slow._next
    slow._next = slow._next._next
    return head

# 寻找链表中间节点
def find_middle_node(head):
    if not head or not head.next_node or not head.next_node.next_node:
        return head
    slow, fast = head, head.next_node
    while fast and fast.next_node:
        slow, fast = slow.next_node, fast.next_node.next_node
    return slow