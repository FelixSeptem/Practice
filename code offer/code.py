# -*- coding:utf-8 -*-  
# 在二维数组中查找
# 二维数组行内左向右递增，列内上到下递增
def find_matrix(m, target):
    row = len(m)
    col = len(m[0])
    found = False
    if m and row>0 and col>0:
        r = 0
        c = col - 1
        while r<row and c>0:
            if m[r][c]==target:
                found = True
                break
            elif m[r][c]>target:
                c -= 1
            else:
                r += 1
    return found

# 链表逆序
def reverse_linkedlist(head):
    reverse_head, node, prev = None, head, None
    while node:
        tmp = node.next
        if tmp:
            reverse_head = node
        node.next = prev
        prev = node
        node = tmp
    return reverse_head

# 两个栈实现队列
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, data):
        self.stack1.append(data)
    
    def pop(self):
        if len(self.stack2):
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if len(self.stack2):
            return self.stack2.pop()
        return None

# 两个队列实现栈
class Stack:
    def __init__(self):
        from collections import Queue
        self.queue1 = Queue()
        self.queue2 = Queue()
    
    def put(self, data):
        if len(self.queue2):
            self.queue2.push(data)
        else:
            self.queue1.push(data)

    def pop(self):
        if len(self.queue1)==0 and len(self.queue2)==0:
            return None
        if len(self.queue1)==1:
            return self.queue1.pop()
        if len(self.queue2)==1:
            return self.queue2.pop()
        if len(self.queue1):
            while len(self.queue1)>1:
                self.queue2.push(self.queue1.pop())
            return self.queue1.pop()
        else:
            while len(self.queue2)>1:
                self.queue1.push(self.queue2.pop())
            return self.queue2.pop()

# 旋转数组中最小数字
def minInOrder(arr, idx1, idx2):
    res = arr[idx1]
    for i in range(idx1, idx2):
        if arr[i]<res:
            res = arr[i]
    return res

def RotateMin(arr):
    if not arr:
        return None
    idx1, idx2 = 0, len(arr) - 1
    idxMin = idx1
    while arr[idx1] >= arr[idx2]:
        if idx2 - idx1 == 1:
            idxMin = idx2
            break
        idxMin = (idx1 + idx2)/2
        if arr[idx1]==arr[idx2] && arr[idx2]==arr[idxMin]:
            return minInOrder(arr, idx1, idx2)
        if arr[idxMin]>=arr[idx1]:
            idx1 = idxMin
        else:
            idx2 = idxMin
    return arr[idxMin]

# 二进制中1的个数
def countOnes(n):
    nums = 0
    while n:
        nums += 1
        n = n&(n-1)

# 数值的整数次方
def power(base, exp):
    if exp==0:
        return 1
    if exp==1:
        return base
    res = power(base, exp>>1)
    res *= res
    if exp & 1 ==1:
        res *= base
    return res

# O(1)时间内删除链表
def delNode(node, head):
    if (not head) or (not head.next):
        return None
    if node==head:
        return head.next
    if node.next:
        if node.next.next:
            node.data = node.next.data
            node.next, node.next.next = node.next.next, None
            return head
        else:
            node.next = None
            return head
    else:
        tmp = head
        while tmp:
            if tmp.next==node:
                tmp.next, node.next = node.next, None
                return head
            tmp = tmp.next
    
# 调整数组顺序使奇数位于偶数前面
def isFront(n):
    return n%1==0
def reorder(arr):
    if not arr:
        return arr
    if len(arr)=1:
        return arr
    front, tail = 0, len(arr) - 1
    while front<tail:
        while front<tail and isFront(arr[front]):
            front += 1
        while front<tail and !isFront(arr[tail]):
            tail -= 1
        if front<tail:
            arr[front], arr[tail] = arr[tail], arr[front]
     
    
# 链表中倒数第k个节点
def find_kth_node_to_tail(linked_list, k):
    if k<=0 or not linked_list:
        return None
    before, after = linked_list, linked_list
    for i in range(k-1):
        if before.next!=None:
            before = before.next
        else:
            return None
    while before.next:
        before = before.next
        after = after.next
    return after

# 合并两个排序的链表
def merge_array(head1, head2):
    if not head1:
        return head2
    elif not head2:
        return head1
    merge_head = None
    if head1.value < head2.value:
        merge_head = head1
        merge_head.next = merge_array(head1.next, head2)
    else:
        merge_head = head2
        merge_head.next = merge_array(head1, head2.next)
    return merge_head

# 树的子结构
def has_subtree(t1, t2):
    if not t2:
        return True
    if not t1:
        return False
    if t1.value!=t2.value:
        return False
    return has_subtree(t1.left, t2.left) && has_subtree(t1.right, t2.right) 

# 二叉树的镜像
def mirror_recursively(root):
    if not root:
        return
    if (not root.left) and (not root.right):
        return

    root.left, root.right = root.right, root.left

    mirror_recursively(root.left)
    mirror_recursively(root.right)

# 顺时针打印矩阵
def visite_in_circle(numbers, start):
    result = []
    cols = len(numbers[0])
    rows = len(numbers)
    endX, endY = cols - 1 - start, rows - 1 - start

    # 横向
    for i in range(start, endX+1):
        num = numbers[start][i]
        result.append(num)

    # 纵向
    if start < endY:
        for i in range(start+1, endY+1):
            num = numbers[i][endY]
            result.append(num)

    # 横向
    if start < endX and start < endY:
        for i in range(endX-1, start-1, -1):
            num = numbers[endY][i]
            result.append(num)

    # 纵向
    if start < endX and start < endY - 1:
        for i in range(endY-1, start-1, -1):
            num = numbers[i][start]
            result.append(num)

    return result

def visite_in_clockwisely(numbers):
    if not numbers or not numbers[0]:
        return
    
    cols = len(numbers[0])
    rows = len(numbers)
    start = 0
    while cols > start * 2 and rows > start * 2:
        visite_in_circle(numbers, start)
        start += 1      

# 包含min函数的栈
class min_stack:
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, v):
        self.data.append(v)
        if not self.min or v<self.min[-1]:
            self.min.append(v)
        else:
            self.min.append(self.min[-1])

    def pop(self):
        if not self.data:
            return
        v = self.data.pop()
        self.min.pop()
        return v

    def min(self):
        if not self.min:
            return
        return self.min[-1]

# 栈的压入、弹出序列
def is_pop_order(push, pop):
    possible = False
    if not push or not pop or len(push)!=len(pop):
        return possible
    length = len(push)
    push_next, pop_next = 0, 0
    stack = []
    while pop_next < length:
        while not stack or stack[-1] != pop[pop_next]:
            if push_next == length:
                break
            stack.append(push[push_next])
            push_next += 1
        if stack[-1] != pop_next:
            break
        stack.pop()
        pop_next += 1
    if not stack and pop_next == length:
        possible = True
    return possible

# 从上往下打印二叉树（层序打印二叉树）
def visite_tree_in_order(root):
    from collections import deque
    if not root:
        return
    pivot = root
    queue = deque()
    queue.appendleft(root)
    result = []
    while len(queue):
        n = queue.pop()
        result.append(n)
        if n.left:
            queue.appendleft(n.left)
        if n.right:
            queue.appendleft(n.right)
    return result

# 二叉搜索树的后序遍历序列
def verify_sequence_of_bst(sequence):
    if not sequence:
        return False
    root = sequence[-1]
    pivot = 0
    for i,v in enumerate(sequence):
        if v>root:
            pivot = i
            break
    if len([x for x in sequence[pivot:] if x<root]):
        return False

    left, right = True, True
    if pivot>0:
        left = verify_sequence_of_bst(sequence[:pivot])
    
    if pivot<len(sequence)-1:
        right = verify_sequence_of_bst(sequence[pivot:])
    return left and right

# 二叉树中和为某一值的路径    
def find_path(root, expected_sum):
    if not root:
        return
    current_sum = root.value
    path = [root]
    is_leaf = not (root.left or root.right)
    if is_leaf and current_sum==expected_sum:
        return True
    if root.left:
        exist = find_path(root.left, expected_sum - current_sum)
    if root.right:
        exist = find_path(root.left, expected_sum - current_sum)
    path.pop()
    return exist 

# 复杂链表的复制
def clone_nodes(head):
    node = head
    while node:
        tmp = Node()
        tmp.value = node.value
        tmp.next = node.next
        tmp.sibling = None
        node.next = tmp
        node = tmp.next
    return node

def connect_sibling(head):
    node = head
    while node:
        tmp = Node()
        if node.sibling:
            tmp.sibling = node.sibling
        node = tmp.next

def reconnect_nodes(head):
    node = head
    tmp_head, tmp_node = None, None
    if node:
        tmp_head , tmp_node = node.next, node.next
        node.next = tmp_node.next
        node = node.next
    while tmp_node:
        tmp_node.next = node.next
        tmp_node = tmp_node.next
        node.next = tmp_node.next
        node = node.next
    return tmp_head

def clone(head):
    clone_nodes(head)
    connect_sibling(head)
    return reconnect_nodes(head)

# 二叉搜索树与双向链表
def convert_node(node, last_node_in_list):
    if not node:
        return
    current = node
    if current.left:
        convert_node(node.left, last_node_in_list)

    current.left = last_node_in_list
    if last_node_in_list:
        last_node_in_list.right = current

    last_node_in_list = current
    if current.right:
        convert_node(current.right, last_node_in_list)


def convert(root):
    last_node_in_list = None
    convert_node(root, last_node_in_list)
    head = last_node_in_list
    while head and head.left:
        head = head.left
    return head

# 字符串的排列
def permutation(string):
    return itertools.permutations(string, len(string))
    

