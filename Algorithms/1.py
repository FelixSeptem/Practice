# -*- coding:utf-8 -*-  

# 二叉搜索树基本数据结构
class Node(object):
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

# 节点插入树
def tree_insert(tree, node):
    if not tree.root:
        return node
    pivot = tree.root
    while pivot:
        node_parent = pivot
        if node.key < pivot.key:
            pivot = pivot.left
        else:
            pivot = pivot.right
    node.parent = node_parent
    if node.key < node_parent.key:
        node_parent.left = node
    elif node.key == node_parent.key:
        node.left, node.right, node.parent = node_parent.left, node_parent.right, node_parent.parent
    else:
        node_parent.right = node
    return tree.root

# 中序遍历
def in_order_walk(tree):
    if tree:
        in_order_walk(tree.left)
        yield tree.key
        in_order_walk(tree.right)


def list_to_tree(arr):
    tree = None
    for x in arr:
        tree = tree_insert(tree, x)
    return tree


def tree_to_str(t):
    if t:
        return "("+tree_to_str(t.left)+"), " + str(t.key) + ", (" + tree_to_str(t.right)+")"
    else:
        return "empty"


def tree_search(t, node):
    pivot = t.root
    while pivot:
        if node.key > pivot.key:
            pivot = pivot.right
        elif node.key == pivot.key:
            return pivot
        else:
            pivot = pivot.left
    return None


def tree_min(t):
    pivot = t.root
    while pivot and pivot.left:
        pivot = pivot.left
    return pivot

def tree_max(t):
    pivot = t.root
    while pivot and pivot.right:
        pivot = pivot.right
    return pivot

def pred(node):
    if not node: 
        return node
    if node.left: 
        return tree_max(node.left)
    p = node.parent
    while p and p.right != node:
        node = p
        p = p.parent
    return p 

def succ(node):
    if not node: 
        return node
    if node.right: 
        return tree_min(node.right)
    p = node.parent
    while p and p.left != node:
        node = p
        p = p.parent
    return p


def remove_node(x):
    if not x: 
        return
    x.parent = x.left = x.right = None


def tree_delete(t, node):
    if not node or not t:
        return t
    if (not node.left) and (not node.right):
        remove_node(node)
    if node.left and (not node.right):
        node.left.parent = node.parent
        remove_node(node)
    elif node.right and (not node.right):
        node.right.parent = node.parent
        remove_node(node)
    else:
        replace_node = tree_max(node.left)
        replace_node.left = node.left
        replace_node.right = node.right
        replace_node.parent = node.parent
        tree_delete(t, replace_node)
    return t


