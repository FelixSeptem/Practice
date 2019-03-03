# -*- coding:utf-8 -*-  
'''
打印两个有序链表的公共部分
给定两个有序链表的头指针h1,h2，打印链表的公共部分
'''
def printCommonPart(h1, h2):
    if (not h1) or (not h2):
        return None
    res = []
    while h1 and h2:
        if h1.value<h2.value:
            h1 = h1.next
        elif h1.value>h2.value:
            h2 = h2.next
        else:
            res.append(h1.value)
            h1 = h1.next
            h2 = h2.next
    
'''
在单链表和双链表中删除倒数第k个节点
实现两个函数，分别实现删除单链表、双链表的倒数第k个节点
'''
def removeLastKthNode(head, k):
    if k<1:
        return None
    fast = head
    while k:
        if fast.next:
            fast = fast.next
            k -= 1
        else:
            return
    slow = head
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    slow.next.prev = slow # this line for delink

'''
删除链表中间节点和a/b处节点
给定链表头结点h，实现删除链表中间节点的函数。
例如：
1->2 不删除
1->2->3 删除2
1->2->3->4 删除2
进阶：
给定链表头结点h，整数a,b，删除链表a/b处节点
链表 1->2->3->4->5 a/b = r
如果r=0，不删除任何节点
如果0<r<=1/5，删除节点1
如果1/5<r<=2/5，删除节点2
如果2/5<r<=3/5，删除节点3
如果3/5<r<=4/5，删除节点4
如果4/5<r<=1，删除节点5
如果r>1，不删除任何节点
'''
def removeMidNode(h):
    if not h or h.next==None:
        return h
    if h.next.next==None:
        return h.next
    pre, cur = h, h.next.next
    while cur.next && cur.next.next:
        pre = pre.next
        cur = cur.next.next
    pre.next = pre.next.next
    return h

def removeByRatio(h, a, b):
    from math import ceil
    if b==0 or a/b>1 or a/b<=0:
        return h
    n = 0
    cur = h
    while cur:
        cur = cur.next
        n += 1
    n = ceil(float(a*n)/b)
    if n==1:
        return h.next
    if n>1:
        cur = h
        while --n!=1:
            cur = cur.next
        cur.next = cur.next.next
    return h

'''
反转单向和双向链表
'''
def reverseSingleList(h):
    next, pre = None, None
    while head:
        next = h.next
        h.next = pre
        pre = h
        h = next
    return pre

def reverseDoubleList(h):
    next, pre = None, None
    while h:
        next = h.next
        h.next = pre
        h.prev = next
        pre = h
        h = next
    return pre