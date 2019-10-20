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
    
# 数组中出现次数超过一半的数字
def more_than_half_num(numbers):
    if not numbers or not len(numbers):
        return None
    result = numbers[0]
    times = 1
    for i in range(1, len(numbers)):
        if times==0:
            result = numbers[i]
            times = 1
        elif numbers[i] == result:
            times += 1
        else:
            times -= 1
    if len([x for x in numbers if x==result])>len(numbers)/2:
        return result
    return None

# 最小的k个数
def get_least_numbers(data, least_numbers, k):
    import heapq
    if not data or len(data)<k:
        return data
    if k<0:
        return None
    h = []
    for d in data:
        heapq.heappush(h, d)
    return [heappop(h) for _ in range(k)]

# 连续子数组最大和
def max_sub_sum(arr):
    if not arr:
        return 0 
    cur_sum, max_sum = 0, 0
    for i in arr:
        if cur_sum<=0:
            cur_sum = i
        else:
            cur_sum += i
        if cur_sum>max_sum:
            max_sum = cur_sum
    return max_sum

# 把数组排成最小的数
def min_number(arr):
    if not arr:
        return 0
    arr.sort(cmp=lambda m,n:''.join([m,n]) < ''.join([n,m]))
    return ''.join(arr)

# 丑数
def get_ugly_num(index):
    if index<0:
        return None
    ugly_num = [0, 1]
    next_index = 1
    num2, num3, num5 = ugly_num, ugly_num, ugly_num
    while next_index<index:
        min_num = min([num2*2, num3*3, num5*5])
        while num2*2<=ugly_num[next_index]:
            num2+=1
        while num3*3<=ugly_num[next_index]:
            num3+=1
        while num5*5<=ugly_num[next_index]:
            num5+=1
        next_index += 1
    return ugly_num[index]
# 第一个只出现一次的字符
def first_once_char(string):
    chars = {}
    for c in string:
        chars[c] = chars.get(c, 0) + 1
    for c in string:
        if chars[c]==1:
            return c

# 数组中的逆序对
def inverse_pairs(arr):
    if not arr or len(arr)<1:
        return 0
    c = [i for i in arr]
    num = inverse_pairs_core(arr, c, 0, len(arr) - 1)
    return num

def inverse_pairs_core(arr, c, start, end):
    if start==end:
        c[start] = arr[start]
        return 0 
    mid = (end - start) / 2 
    left, right = inverse_pairs_core(c, arr, start, start+mid), inverse_pairs_core(c, arr, start+mid, end)
    i, j = start+mid, end
    indexCopy = end
    num = 0
    while i>=start and j >=start+mid+1:
        if arr[i]>arr[j]:
            c[indexCopy] = arr[i]
            indexCopy -= 1
            i -= 1
            num += j - (start + mid)
        else:
            c[indexCopy] = arr[j]
            indexCopy -= 1
            j -= 1
    while i>=start:
        c[indexCopy] = arr[i]
        indexCopy -= 1
        i -= 1
    while j > start+mid+1:
        c[indexCopy] = arr[j]
        indexCopy -= 1
        j -= 1
    return left + right + num

# 两个链表的第一个公共结点
def find_first_commo0n_node(list1, list2):
    length1, length2 = 0, 0
    tmp = list1
    while tmp:
        length1 += 1
        tmp = tmp.next
    tmp = list2
    while tmp:
        length2 += 1
        tmp = tmp.next

    p1, p2 = list1, list2
    while length1 - length2>0:
        p1 = p1.next
        length1 -= 1
    while length2 - length1 >0:
        p2 = p2.next
        length2 -= 1

    while p1 and p2:
        if p1==p2:
            return p1
        p1 = p1.next
        p2 = p2.next
    return None

# 数字在排序数组中出现的次数
def get_first_k(data, k, start, end):
    if start > end:
        return -1
    mid = (start + end) / 2
    if data[mid]==k:
        if (mid > 0 and data[mid-1]!=k) or mid==0:
            return mid
        else:
            end = mid - 1
    elif data[mid]>k:
        end = mid - 1
    else:
        start = mid + 1
    return get_first_k(data, k, start, end)

def get_last_k(data, k, start, end):
    if start > end:
        return -1
    mid = (start + end) / 2
    if data[mid]==k:
        if (mid < len(data)-1 and data[mid-1]!=k) or mid==len(data)-1:
            return mid
        else:
            start = mid + 1
    elif data[mid]<k:
        start = mid + 1
    else:
        end = mid - 1
    return get_last_k(data, k, start, end)

def get_number_of_k(data, k):
    if not data or len(data)==0:
        return 0
    if k<data[0] or k>data[0]:
        return 0
    first, last = get_first_k(data, k, 0, len(data) - 1), get_last_k(data, k, 0, len(data) - 1)
    if first>-1 and last>-1:
        return last - first + 1
    return 0

# 二叉树的深度
def tree_depth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    d_left, d_right = tree_depth(root.left), tree_depth(root.right)
    return d_left+1 if d_left>d_right else d_right

# 数组中只出现一次的数字
def separate_two_group(num, index_bit):
    mask = 1
    while index_bit>0:
        mask = mask>>1
    return [i for i in num if i&mask==0], [i for i in num if i&mask!=0]
def find_nums_appear_once(data):
    if not data:
        return None, None
    if len(data)<2:
        return None, None
    if len(data)==2:
        if data[0]!=data[1]:
            return data[0], data[1]
        return None, None
    res = reduce(lambda x,y:x^y, data)
    index_bit = 0
    while res>0:
        if res%2!=0:
            break
        else:
            res = res << 1
    num1, num2 = separate_two_group(data, index_bit)
    return reduce(lambda x,y:x^y, num1), reduce(lambda x,y:x^y, num2)

# 和为s的两个数字
def find_nums_with_sum(data, given_sum):
    if not data or len(data)<2:
        return False
    if len(data)==2 and data[0] + data[1]!=given_sum:
        return False
    head, tail = 0, len(data) - 1
    while head<tail:
        tmp = data[head] + data[tail]
        if tmp==given_sum:
            return True
        elif tmp<given_sum:
            head += 1
        else:
            tail -= 1
    return False

# 和为s的连续正数序列
def find_con_sequence(given_sum):
    if given_sum<3:
        return None
    result = []
    small, big = 1, 2
    middle = (given_sum + 1)/2
    tmp = 1+2
    while small<middle:
        if tmp==given_sum:
            result.append([x for x in range(small, big)])
        while tmp>given_sum and small<middle:
            tmp -= small
            small += 1
            if tmp == given_sum:
                result.append([x for x in range(small, big+1)])
        big += 1
        tmp += big
    return result

# n个骰子的点数
def print_probability(num):
    max_value=6
    if num<1:
        return
    p = [
        [1 for _ in range(max_value+1)],
        [0 for _ in range(max_value+1)]
    ]
    flag = 0
    for k in range(2, num+1):
        for i in range(k):
            p[1-flag][i] = 0
        for i in range(k, k*max_value):
            p[1-flag][i] = 0
            for j in range(1, i):
                if j<=max_value:
                    p[1-flag][i]+=p[flag][i-j]
        flag = 1-flag
    total = pow(max_value, num)
    for i in range(num, max_value*num):
        ratio = p[flag][i] / total
        print(ratio)

# 扑克牌的顺子
def is_continuous(nums):
    if not nums:
        return False
    nums.sort()
    zero_count = 0
    for i in nums:
        if i==0:
            zero_count += 1
        else:
            break
    if zero_count==len(nums):
        return True
    pre, tail = zero_count, zero_count + 1
    gap = 0
    while tail<len(nums):
        if nums[pre] == nums[tail]:
            return False
        gap += nums[tail] - nums[pre] - 1
        pre, tail = tail, tail+1
    return gap<=zero_count

# 圆圈中最后剩下的数字 约瑟夫环
def last_remain(n, m):
    if n<1 or m<1:
        return None
    last = 0
    for i in range(2, n+1):
        last = (last+m)%i
    return last

# 树中两个结点的最低公共祖先
def find_least_common_parent(root, node1, node2):
    if node1>=node2:
        node1, node2 = node2, node1
    if not root or not node1 or not node2:
        return None
    if (root.value == node1.value or root.value == node2.value) or (node1.value<root.value and root.value<node2.value):
        return root
    if root.value > node2.value:
        return find_least_common_parent(root.left, node1, node2)
    if root.value < node1.value:
        return find_least_common_parent(root.right, node1, node2)

# dfs
def find_node_path(root, node):
    if not root or not node:
        return
    stack = [root]
    if root == node:
        return stack

    while stack:
        tmp = stack.pop()
        if tmp.right:
            stack.append(tmp.right)
            if tmp.right==node:
                return stack
        if tmp.left:
            stack.append(tmp.left)
            if tmp.left==node:
                return stack
    return None

# bfs
def find_node_level(root, node):
    from collections import deque
    if not root or not node:
        return
    q = deque()
    q.append(root)
    if root == node:
        return q
    
    while q:
        tmp = q.popleft()
        if tmp.left:
            q.append(tmp.left)
            if tmp.left == node:
                return q
        if tmp.right:
            q.append(tmp.right)
            if tmp.right == node:
                return q
    return None

# 之字遍历
def zigzagLevelOrder(self, root): 
    from collections import deque
    if not root:
        return None
    queue = deque()
    queue.append(root)
        
    res = []
    flag = True
        
    while queue:
        cnt = len(queue)
        temp = []
        for i in range(cnt):
            cur = queue.popleft()
            temp.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
                    
        if flag:
            res.append(temp)
            flag = not flag
            continue
                
        if not flag:
            res.append(temp[::-1])
            flag = not flag
                
    return res

# 数组中重复的数字
def duplicate(nums):
    if not nums or len(nums)<2:
        return None
    if len(nums) == 2:
        return nums[0] if nums[0] == nums[1] else None
    for i in range(len(nums))):
        while nums[i]!=i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
    return None

# 链表中环的入口节点
def is_has_circle(linked_list):
    if not linked_list or not linked_list.next or not linked_list.next.next:
        return None
    fast, slow = linked_list.next.next, linked_list.next
    while fast and slow:
        if fast == slow:
            return fast
        fast = fast.next
        if not fast:
            break
        fast = fast.next
        slow = slow.next
    return None

def count_circle_length(linked_list, node_in_circle):
    if not linked_list:
        return 0
    if not node_in_circle:
        return 0
    l = 0
    tmp = node_in_circle
    while tmp:
        tmp = tmp.next
        l += 1
        if tmp == node_in_circle:
            break
    if not tmp:
        return 0
    return l

def find_circle_start(linked_list):
    meet_node = is_has_circle(linked_list)
    if not meet_node:
        return None
    circle_length = count_circle_length(linked_list, meet_node)
    if not circle_length:
        return None
    prev, after = linked_list, linked_list
    while circle_length:
        prev = prev.next
        circle_length -= 1
    while prev and after:
        prev = prev.next
        after = after.next
        if prev == after:
            return prev
    return None

# 删除链表中重复的结点
def remove_duplicate_nodes(linked_list):
    if not linked_list or not linked_list.next:
        return linked_list
    pre, node = None, linked_list
    while node:
        next_node = node.next
        need_delete = False
        if next_node and next_node.value == node.value:
            need_delete = True
        if need_delete:
            pre = node
            node = node.next_node
        else:
            value = node.value
            tobedel = node
            while tobedel and tobedel.value == value:
                next_node = tobedel.next
                tobedel = next_node
            if pre:
                linked_list = next_node
            else:
                pre.next = next_node
            node = next_node
    return linked_list

# 二叉树的下一个结点
def find_next(root, target):
    if not root or not target:
        return None
    next_node = None
    if target.right:
        right = target.right:
        while right.left:
            right = right.left
        next_node = next_node
    elif target.parent:
        current = target
        parent = target.parent
        if current == parent.left:
            next_node = parent
        else:
            while parent and current == parent.right:
                current = parent
                parent = parent.parent
            next_node = parent
    return next_node

# 对称的二叉树
def is_symmetrical(root):
    return is_symmetrical_helper(root, root)

def is_symmetrical_helper(root1, root2):
    if not root1 and root2:
        return True
    if not root1 or not root2:
        return False
    if root1.value!=root2.value:
        return False
    return is_symmetrical_helper(root1.left, root2.right) and is_symmetrical_helper(root1.right, root2.left)

# 把二叉树打印成多行
def level_visit(root):
    if not root:
        return None
    queue = [root]
    next_level = 0
    to_be_visit = 1
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
            next_level += 1
        if node.right:
            queue.append(node.right)
            next_level += 1
        to_be_visit -= 1
        if to_be_visit==0:
            print('\n')
            to_be_visit = next_level
            next_level = 0
    
# 按之字形顺序打印二叉树
def zigzagLevelOrder(self, root): 
    if not root:
        return None
    levels = [[], []]
    current, next = 0, 1
    levels[current].append(root)
    while levels[0] or levels[1]:
        node = levels[current].pop()
        if current == 0:
            if node.left:
                levels[next].append(node.left)
            if node.right:
                levels[next].append(node.right)
        else:
            if node.right:
                levels[next].append(node.right)
            if node.left:
                levels[next].append(node.left)
        if not levels[current]:
            current = 1-current
            next = 1-next

# 二叉搜索树的第K个结点
def kth_node(root, k):
    if not root or k<0:
        return None
    return kth_node_core(root, k)

def kth_node_core(root, k):
    target = None
    if root.left:
        target = kth_node(root.left, k)
    if target:
        if k==1:
            target = root
            k -= 1
    if not target and root.left:
        target = kth_node_core(root.right, k)
    return target

# 滑动串口的最大值
def max_in_window(nums, size):
    from collections import deque
    result = []
    if len(nums) > size and size >= 1:
        index = deque()
        for i in range(size):
            while len(index) and nums[i]>nums[index[-1]]:
                index.pop()
            index.append(i)
        for i in range(size, len(nums)):
            result.append(nums[index[0]])
            while index and nums[i] >= nums[index[-1]]:
                index.pop()
            if index and index[0]<= i-size:
                index.popleft()
            index.append(i)
        result.append(nums[index[0]])
    return result

