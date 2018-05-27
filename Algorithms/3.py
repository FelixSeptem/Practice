# -*- coding:utf-8 -*-  


'''
1. 任一节点要么是红色要么是黑色
2. 根节点为黑色
3. 所有的叶节点（NIL节点）为黑色
4. 如果一个节点为红色则它的两个子节点都是黑色
5. 对任一节点，从它出发到所有叶子节点的路径上包含相同数量的黑色节点。
'''
import string

RED = 0
BLACK = 1
DOUBLY_BLACK = 2

class Node:
    def __init__(self, key, color = RED):
        self.key = key;
        self.color = color;
        self.left = self.right = self.parent = None

    def set_left(self, x):
        self.left = x
        if x != None:
            x.parent = self

    def set_right(self, x):
        self.right = x
        if x != None:
            x.parent = self

    def set_children(self, x, y):
        self.set_left(x)
        self.set_right(y)

    def replace_by(self, y):
        replace(self.parent, self, y)

    def sibling(self):
        if self.parent.left == self:
            return self.parent.right
        else:
            return self.parent.left

    def uncle(self):
        return self.parent.sibling()

    def grandparent(self):
        return self.parent.parent

# common helpfer operations
def set_color(nodes, colors):
    for (n, c) in zip(nodes, colors):
        n.color = c

# change from: parent --> x to: parent --> y
def replace(parent, x, y):
    if parent is None:
        if y is not None:
            y.parent = None
    elif parent.left == x:
        parent.set_left(y)
    else:
        parent.set_right(y)
    if x is not None:
        x.parent = None
    return y

# rotations

# (a x (b y c)) ==> ((a x b) y c)
def left_rotate(t, x):
    (parent, y) = (x.parent, x.right)
    (a, b, c)   = (x.left, y.left, y.right)
    x.replace_by(y)
    x.set_children(a, b)
    y.set_children(x, c)
    if parent is None:
        t=y
    return t

# (a x (b y c)) <== ((a x b) y c)
def right_rotate(t, y):
    (parent, x) = (y.parent, y.left)
    (a, b, c)   = (x.left, x.right, y.right)
    y.replace_by(x)
    y.set_children(b, c)
    x.set_children(a, y)
    if parent is None:
        t = x
    return t

# insertion and deletion

def rb_insert(t, key): #returns the new root
    root = t
    x = Node(key)
    parent = None
    while(t):
        parent = t
        if(key < t.key):
            t = t.left
        else:
            t = t.right
    if parent is None: #tree is empty
        root = x
    elif key < parent.key:
        parent.set_left(x)
    else:
        parent.set_right(x)
    return rb_insert_fix(root, x)

# Fix the red->red violation
def rb_insert_fix(t, x):
    while(x.parent and x.parent.color==RED):
        if x.uncle().color == RED:
            #case 1: ((a:R x:R b) y:B c:R) ==> ((a:R x:B b) y:R c:B)
            set_color([x.parent, x.grandparent(), x.uncle()],
                      [BLACK, RED, BLACK])
            x = x.grandparent()
        else:
            if x.parent == x.grandparent().left:
                if x == x.parent.right:
                    #case 2: ((a x:R b:R) y:B c) ==> case 3
                    x = x.parent
                    t=left_rotate(t, x)
                # case 3: ((a:R x:R b) y:B c) ==> (a:R x:B (b y:R c))
                set_color([x.parent, x.grandparent()], [BLACK, RED])
                t=right_rotate(t, x.grandparent())
            else:
                if x == x.parent.left:
                    #case 2': (a x:B (b:R y:R c)) ==> case 3'
                    x = x.parent
                    t = right_rotate(t, x)
                # case 3': (a x:B (b y:R c:R)) ==> ((a x:R b) y:B c:R)
                set_color([x.parent, x.grandparent()], [BLACK, RED])
                t=left_rotate(t, x.grandparent())
    t.color = BLACK
    return t

# Querying function for deletion, we can reuse those in binary search tree (bstree.py)

def tree_search(t, x):
    while(t!=None and t.key != x):
        if(x < t.key): t = t.left
        else: t = t.right
    return t

def tree_min(t):
    while(t!=None and t.left != None):
        t = t.left
    return t

def remove_node(x):
    if (x is None): return
    x.parent = x.left = x.right = None

def is_leaf(x):
    if x is None: return False
    return (x.left is None) and (x.right is None)

def make_black(parent, x):
    if parent is None and x is None:
        return None
    if x is None:
        return replace(parent, x, Node(0, DOUBLY_BLACK))
    x.color = x.color + 1
    return x

def rb_delete(t, x):
    if x is None: return t
    (parent, db) = (x.parent, None)
    if x.left is None:
        x.replace_by(x.right)
        db = x.right
    elif x.right is None:
        x.replace_by(x.left)
        db = x.left
    else:
        y = tree_min(x.right)
        (parent, db)=(y.parent, y.right)
        x.key = y.key
        y.replace_by(y.right)
        x = y
    if x.color == BLACK:
        t = rb_delete_fix(t, make_black(parent, db), db is None)
    remove_node(x)
    return t

def is_red(x):
    if x is None: return False
    return x.color == RED

def is_black(x):
    return x is None or x.color == BLACK

def rb_delete_fix(t, db, is_db_empty):
    db_empty = db if is_db_empty else None
    if db is None: return None # remove the root from a leaf tree
    while(db!=t and db.color==DOUBLY_BLACK):
        if db.sibling() != None:
            # case 1:  the sibling is red, (transform to make the sibling black)
            if is_red(db.sibling()):
                set_color([db.parent, db.sibling()],[RED, BLACK])
                if(db == db.parent.left):
                    t=left_rotate(t, db.parent)
                else:
                    t=right_rotate(t, db.parent)
            # case 3, 4: the sibling is black, and one nephew is red
            elif is_black(db.sibling()) and is_red(db.sibling().left):
                if db == db.parent.left:
                    colors=[BLACK, BLACK, db.parent.color]
                    set_color([db, db.parent, db.sibling().left], colors)
                    t=right_rotate(t, db.sibling())
                    t=left_rotate(t, db.parent)
                else:
                    colors=[BLACK, BLACK, db.parent.color, BLACK]
                    set_color([db, db.parent, db.sibling(), db.sibling().left], colors)
                    t=right_rotate(t, db.parent)
            elif is_black(db.sibling()) and is_red(db.sibling().right):
                if db == db.parent.left:
                    colors=[BLACK, BLACK, db.parent.color, BLACK]
                    set_color([db, db.parent, db.sibling(), db.sibling().right], colors)
                    t=left_rotate(t, db.parent)
                else:
                    colors=[BLACK, BLACK, db.parent.color]
                    set_color([db, db.parent, db.sibling().right], colors)
                    t=left_rotate(t, db.sibling())
                    t=right_rotate(t, db.parent)
            # case 2: the sibling and both nephews are black. (move the blackness up)
            elif is_black(db.sibling()) and (not is_red(db.sibling().left)) and (not is_red(db.sibling().right)):
               set_color([db, db.sibling()], [BLACK, RED])
               db.parent.color=db.parent.color+1
               db = db.parent
            # a sibling without child is invalid case, because it violate property 5
        else: # no sibling, we can move blackness up
            db.color = BLACK
            db.parent.color = db.parent.color+1
            db = db.parent
    t.color=BLACK
    if db_empty is not None:
        db_empty.replace_by(None)
    return t

# Helper functions for test

def rbtree_clone(t):
    n = None
    if t != None:
        n = Node(t.key, t.color)
        n.set_children(rbtree_clone(t.left), rbtree_clone(t.right))
    return n

def rbtree_to_str(t):
    if t is None:
        return "."
    else:
        color = {RED:"R", BLACK:"B"}
        return "("+rbtree_to_str(t.left)+ " " + str(t.key) +":"+color[t.color]+" " + rbtree_to_str(t.right)+")"

def list_to_tree(l):
    tree = None
    for x in l:
        tree = rb_insert(tree, x)
    return tree

CLR = {'R':RED, 'B':BLACK}

def node(x, c):
    return Node(x, CLR[c] if c in CLR else DOUBLY_BLACK)

def tr(l, x, c, r):
    t = node(x, c)
    t.set_children(l, r)
    return t

def is_rbt(t):
    if t is None:
        return True
    if not is_black(t):
        print "root is not black"
        return False
    if has_adjacent_red(t):
        print "has adjacent red nodes"
        return False
    if num_of_blacks(t) < 0:
        print "different number of black nodes"
        return False
    return True

def has_adjacent_red(t):
    if t is None:
        return False
    if is_red(t) and (is_red(t.left) or is_red(t.right)):
        print "adjacent red at", t.key
        return True
    return has_adjacent_red(t.left) or has_adjacent_red(t.right)

def num_of_blacks(t):
    if t is None:
        return 1
    a, b = num_of_blacks(t.left), num_of_blacks(t.right)
    if a != b:
        print "Node", t.key, "has different black desendants: l=", a, ", r=", b
        return -1000
    return a + (1 if is_black(t) else 0)

def assert_rbt(t):
    if not is_rbt(t):
        exit(-1)

