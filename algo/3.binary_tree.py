'''
用递归和非递归方式完成二叉树的前序，中序，后序遍历
'''
def preOrderRecur(root):
    if not root:
        return None
    print(root.value)
    preOrderRecur(root.left)
    preOrderRecur(root.right)

def preOrderNonRecur(root):
    if not root:
        return None
    stack = []
    stack.append(root)
    while stack:
        n = stack.pop()
        print(n.value)
        if n.right:
            stack.append(n)
        if n.left:
            stack.append(n.left)
        
def midOrderRecur(root):
    if not root:
        return None
    preOrderRecur(root.left)
    print(root.value)
    preOrderRecur(root.right)

def midOrderNonRecur(root):
    if not root:
        return None
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.value)
            root = root.right

def posOrderRecur(root):
    if not root:
        return None
    preOrderRecur(root.left)
    preOrderRecur(root.right)
    print(root.value)

def posOrderNonRecur(root):
    if not root:
        return None
    stack = [root]
    n = None
    while stack:
        c = stack[-1]
        if c.left and h!=c.left and h!=c.right:
            stack.append(c.left)
        elif c.right and h!=c.right:
            stack.append(c.right)
        else:
            print(stack.pop())
            h = c

'''
二叉树序列化与反序列化
'''
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def serialByPre(head):
    if not head:
        return "#!"
    s = str(head.value) + "!"
    s += serialByPre(head.left)
    s += serialByPre(head.right)
    return s

def reconPreString(s):
    values = s.split("!")
    nodes = []
    for i in range values:
        nodes.append(Node(value=i))
    return reconPreNode(nodes)

def reconPreNode(n):
    v = n.pop()
    if v.value=="#":
        return None
    head = v
    head.left = reconPreNode(n)
    head.right = reconPreNode(n)
    return head

'''
在二叉树中找到累加和为指定值的最长路径长度
'''
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def getMaxLength(head, sum):
    sumMap = {0:0}
    return preOrder(head, sum, 0, 1, 0, sumMap)

def preOrder(head, sum, preSum, level, maxLen, sumMap):
    if not head:
        return maxLen
    curSum = preSum + head.value
    if sumMap.get(curSum, None) == None:
        sumMap[curSum] = level
    if sumMap.get((curSum - sum), None) == None:
        maxLen = max(level - sumMap.get(curSum - sum), maxLen)
    maxLen = preOrder(head.left, sum, curSum, level+1, maxLen, sumMap)
    maxLen = preOrder(head.right, sum, curSum, level+1, maxLen, sumMap)
    if level == sumMap.get(curSum):
        sumMap.remove(curSum)
    return maxLen
