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
        if root.left is None:
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

    

    