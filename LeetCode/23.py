# -*- coding:utf-8 -*-  
'''
95. Unique Binary Search Tree 
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def clone(root, offset):
            if root:
                newRoot = TreeNode(root.val + offset)
                left = clone(root.left, offset)
                right = clone(root.right, offset)
                newRoot.left = left
                newRoot.right = right
                return newRoot
                
        if not n:
            return []
        dp = [[]] * (n + 1)
        dp[0] = [None]
        for i in range(1, n + 1):
            dp[i] = []
            for j in range(1, i + 1):
                for left in dp[j - 1]:
                    for right in dp[i - j]:
                        root = TreeNode(j)
                        root.left = left
                        root.right = clone(right, j)
                        dp[i].append(root)
        return dp[-1]

'''
96. Unique Binary Search Tree
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution(object):
    def _numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]
        
    def numTrees(self, n):
        ans = 1
        for i in range(1, n + 1):
            ans = ans * (n + i) / i
        return ans / (n + 1)
            

'''
97. Interleavig String
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        d = {}
        s3 = list(s3)
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(s1, i, s2, j, d, path, s3):
            if (i, j) in d:
                return d[(i, j)]
            
            if path == s3:
                return True
            
            if i < len(s1):
                if s3[i + j] == s1[i]:
                    path.append(s1[i])
                    if dfs(s1, i + 1, s2, j, d, path, s3):
                        return True
                    path.pop()
                    d[(i+1, j)] = False
            
            if j < len(s2):
                if s3[i + j] == s2[j]:
                    path.append(s2[j])
                    if dfs(s1, i, s2, j + 1, d, path, s3):
                        return True
                    path.pop()
                    d[(i, j+1)] = False

            
            return False
            
        return dfs(s1, 0, s2, 0, d, [], s3)