# -*- coding:utf-8 -*-  



class TreeNode:
    def __init__(self, val, left=None, right=None):
        this.val = val
        this.left, this.right = left, right

    def lookup(self, root):
        # 层序遍历
        stack = [root]
        results = []
        while stack:
            current = stack.pop(0)
            results.append(current)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return results

    def bfs(self, tree):
        if not tree.root:
            return []
        queue = [tree.root]
        results = []
        while queue:
            node = queue.pop(0)
            results.append(node)
            queue.append(node.left)
            queue.append(node.right)
        return queue

    def dfs(self, tree):
        if not tree.root:
            return []
        stack = [tree.root]
        results = []
        while stack:
            node = stack.pop()
            results.append(node)
            stack.append(node.right)
            stack.append(node.left) 
        return results

    def maxDepth(self, tree):
        if not tree.root:
            return 0
        return max(self.maxDepth(tree.left), self.maxDepth(tree.right)) + 1

    def mid_travelsal(root):
        if root.left is not None:
            mid_travelsal(root.left)
        #访问当前节点
        print(root.value)
        if root.right is not None:
            mid_travelsal(root.right)

    def pre_travelsal(root):
        print (root.value)
        if root.left is not None:
            pre_travelsal(root.left)
        if root.right is not None:
            pre_travelsal(root.right)

    def post_trvelsal(root):
        if root.left is not None:
            post_trvelsal(root.left)
        if root.right is not None:
            post_trvelsal(root.right)
        print (root.value)

    

    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                print node.elem,
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild                  #开始查看它的右子树


    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            print node.elem,
            node = node.rchild                  #开始查看它的右子树


    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                   #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
            print myStack2.pop().elem,