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

'''
反转部分单向链表
给定一个单向列表头结点，两个整数from和to，反转from到to的部分
例如：
input:
1->2->3->4->5->null, from=2, to=4
output:
1->4->3->2->5->null
'''
def reversePart(h, from, to):
    if from<0 or from>=to:
        return h
    length = 0
    n1 = h
    fPre, tPos = None, None
    while n.next!=None:
        length++
        fPre = n1 if from - 1 == length else fPre 
        tPos = n1 if to + 1 == length else tPos
        n1 = n1.next
    if to>length:
        return h
    n1 = head if not fPre else fPre.next
    n2 = n1.next
    n1.next = tPos
    next = None
    while n2!=tPos:
        next = n2.next
        n2.next = n1
        n1 = n2
        n2 = next
    if not fPre:
        fPre.next = n1
        return h
    return n1

'''
环形单链表的约瑟夫环问题
'''
def getLive(i, m):
    if i==1:
        return 1
    return (getLive(i-1, m) + m - 1)%i + 1

def jKill(h, m):
    if not h or h.next==h or m<1:
        return h
    cur = h.next
    length = 1
    while cur!=h:
        length++
        cur = cur.next
    loc = getLive(length, m)
    while --loc!=0:
        h = h.next
    h.next = h
    return h

'''
判断一个链表是否为回文结构
example:
input:      output:
1->2->1     true
1->2->2->1  true
1->2->3     false
'''
def isPalind(h):
    if not h or not h.next:
        return True
    n1,n2 = h
    # find middle node
    while n2.next and n2.next.next:
        n1 = n1.next
        n2 = n2.next.next
    n2 = n1.next
    n1.next = None
    while n2:
        n3 = n2.next
        n2.next = n1
        n1 = n2
        n2 = n3
    n3 = n1
    n2 = h
    isPa = True
    while n1 and n2:
        if n1.value!=n2.value:
            isPa = False
            break
        n1 = n1.next
        n2 = n2.next
    n1 = n3.next
    n3.next = None
    while n1:
        n2 = n1.next
        na.next = n3
        n3 = n1
        n1 = n2
    return isPa

'''
将单向链表按给定值划分为左边小中间相等右边大的三个部分
给定链表头结点h,值pivot，将给定链表调整为左边小于，中间相等，右边大于的三部分
'''
def listPartition(h, pivot):
    sH, sT = None, None
    eH, sT = None, None
    bH, bT = None, None
    while head:
        next = h.next
        h.next = None
        if h.value<pivot:
            if not sH:
                sH = h
                sT = h
            else:
                sT.next = h
                st = h
        elif h.value==pivot:
            if not eH:
                eH = h
                eT = h
            else:
                eT.next = h
                eT = h
        else:
            if not bH:
                bH = h
                bT = h
            else:
                bT.next = h
                bT = h
        h = next
    if sT:
        sT.next = eH
        eT = sT if not eT else eT
    if eT:
        eT.next = bH
    if sH:
        return sH
    elif eH:
        return eH
    return bH

'''
单链表相加
给定两个链表节点h1,h2，输出相加值的链表
example:
input: h1 9->3->7 h2 6->3
output: 1->0->0->0
'''
def reverseList(h):
    pre,next = None, None
    while h:
        n = h.next
        h.next = pre
        pre = h
        h = next
    return pre

def addList(h1, h2):
    h1, h2 = reverseList(h1), reverseList(h2)
    ca, n1, n2 n = 0, 0, 0, 0
    c1, c2, node, pre = h1, h2, None, None
    while c1 or c2:
        n1 = c1.value if c1 else 0
        n2 = c2.value if c2 else 0
        n = n1 + n2 + ca
        pre = node
        node = Node(n%10)
        node.next = pre
        ca = n/10
        c1 = c1.next if c1 else None
        c2 = c2.next if c2 else None
    if ca==1:
        pre = node
        node = Node(1)
        node.next = pre
    reverseList(h1)
    reverseList(h2)
    return node

'''
给定两个单链表h1,h2，如果相交，返回相交节点
'''
# 判断链表是否有环，如果有，则返回入环的第一个节点
def getLoopNode(h):
    if not h or not h.next:
        return None
    n1, n2 = h.next, h.next.next
    while n1!=n2:
        if not n2.next or not n2.next.next:
            return None
        n2 = n2.next.next
        n1 = n1.next
    n2 = h
    while n1!=n2:
        n1 = n1.next
        n2 = n2.next
    return n1

# 判断两个无环链表是否相交，相交则返回第一个节点
def noLoop(h1, h2):
    if not h1 or not h2:
        return None
    cur1, cur2 = h1, h2
    length1, length2 = 0, 0
    while cur1.next:
        length1++
        cur1 = cur1.next
    while cur2.next:
        length2++
        cur2 = cur2.next
    if cur1!=cur2:
        return None
    cur1, cur2 = h1, h2
    if length1>length2:
        for _ in range(length1-length2):
            cur1 = cur1.next
    elif length1<length2:
        for _ in range(length2-length1):
            cur2 = cur2.next
    while cur1!=cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

# 判断两个有环链表是否相交，相交则返回第一个节点
def bothLoop(h1, h2, l1, l2):
    cur1, cur2 = None, None
    if l1==l2:
        cur1, cur2 = h1, h2
        n = 0
        while cur1!=l1:
            n++
            cur1 = cur1.next
        while cur2!=l2:
            n--
            cur2 = cur2.next
        cur1 = h1 if n>0 else h2
        cur2 = h2 if cur1==h1 else h1
        n = abs(n)
        while n:
            n--
            cur1 = cur1.next
        while cur1!=cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = l1.next
        while cur1!=l1:
            if cur1==l2:
                return l1
            cur1 = cur1.next
        return None

# 综合上面代码
def getIntersecrNode(h1, h2):
    if not h1 or not h2:
        return None
    l1, l2 = getLoopNode(h1), getLoopNode(h2)
    if not l1 and not l2:
        return noLoop(h1, h2)
    if l1 and l2:
        return bothLoop(h1, h2, l1, l2)
    return None

'''
将单链表的每k个节点之间逆序
example:
input: 1->2->3->4->5->6->7->8->null K=3
output: 3->2->1->6->5->4->7->8->null
'''
def reverseKNode(h, k):
    if k<2:
        return h
    cur, start, pre, next = h, None, None, None
    count = 1
    while cur:
        next = cur.next
        if count==k:
            start = h if not pre else pre.next
            h = cur if not pre else h
            resign(pre, start, cur, next)
            pre = start
            count = 0
        count += 1
        cur = next
    return h

def resign(left, start, end, right):
    pre, cur, next = start, start.next, None
    while cur!=right:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    if left:
        left.next = end
    start.next = right

'''
删除无序单链表中值重复出现的节点
example:
input: 1->2->3->3->4->4->1->2->null  
output: 1->2->3->4->null
'''
def removeRep(h):
    if not h or not h.next:
        return h
    s = set(h.value)
    pre = h
    cur = h.next
    while cur:
        if cur.value in set:
            pre.next = cur.next
        else:
            s.add(cur.value)
            pre = cur
        cur = cur.next
    return h

'''
在单链表中删除给定值的节点
给定链表头结点和固定值num，删除链表中所有值为num的节点
input: 1->2->3->4->3->null num=3
output: 1->2->4->null
'''
def removeNode(h, num):
    if not h:
        return h
    while h:
        if h.value!=num:
            break
        h = h.next
    pre, cur = h, h
    while cur:
        if cur.value==num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return h
        
'''
将搜索二叉树转化成双向链表
将搜索二叉树转化成有序的二叉链表
'''
from collections import deque
def inOrderToQueue(head, queue):
    if not head:
        return
    inOrderToQueue(h.left, queue)
    queue.Add(head)
    inOrderToQueue(h.right, queue)
def convert(h):
    queue = deque()
    inOrderToQueue(h, queue)
    if len(queue)==0:
        return h
    h = queue.pop()
    pre = h
    pre.left, cur = None, None
    while queue:
        cur = queue.pop()
        pre.right = cur
        cur.left = pre
        pre = cur
    pre.right = None
    return h

'''
单链表选择排序
'''
def getsmallPre(h):
    smallPre = None
    small = h
    pre = h
    cur = h.next
    while cur:
        if cur.value<small.value:
            smallPre = pre
            small = cur
        pre = cur
        cur = cur.next
    return smallPre
def selectSort(h):
    tail = None
    cur = h
    smallPre, small = None, None
    while cur:
        small = cur
        smallPre = getsmallPre(cur)
        if smallPre:
            small = smallPre.next
            smallPre.next = small.next
        cur = cur.next if cur==small else cur
        if tail:
            h = small
        else:
            tail.next = small
        tail = small
    return h

'''
向有序环状单链表中插入节点，使其依然保持有序
'''
def  insertNode(h, value):
    node=Node(value)
    if not h:
        node.next = node
        return node
    pre = h
    cur = h.next
    while  cur!=h:
        if pre.value<=value and cur.value>=value:
            break
        pre = pre.next
        cur = cur.next
    pre.next = node
    node.next = cur
    if h.value<value:
        return h
    return node

'''
合并两个有序的单链表
'''
def mergeList(h1, h2):
    if not h1:
        return h2
    if not h2:
        return h1
    cur1, cur2 =  h1, h2
    pre, next = None, None
    if h1.value<=h2.value:
        h = h1.value
        cur1 = cur1.next
    else:
        h = h2.value
        cur2 = cur.next
    while cur1 and cur2:
        if cur1.value<=cur2.value:
            pre = cur1
            cur1 = cur1.next
        else:
            next = cur2.next
            pre.next = cur2
            cur2.next = cur1
            pre = cur2
            cur2 = next
    if not cur1:
        pre.next = cur2
    else:
        pre.next = cur1
    return h
