# -*- coding:utf-8 -*-  
'''
77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution(object):
    def combine(self, n, k):
        if k==1:
            return [[i] for i in range(1,n+1)]
        elif k==n:
            return [[i for i in range(1,n+1)]]
        else:
            rs = []
            rs += self.combine(n-1,k)
            part = self.combine(n-1,k-1)
            for ls in part:
                ls.append(n)
            rs += part
            return rs


'''
78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, index, path, ans):
            ans.append(path)
            [dfs(nums, i + 1, path + [nums[i]], ans) for i in xrange(index, len(nums))]
        ans = []
        dfs(nums, 0, [], ans)
        return ans


'''
79. Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        if word == "":
            return True
        if len(board) == 0:
            return False
        visited = [[0] * len(board[0]) for i in xrange(0, len(board))]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j, board, visited, word, index):
            if word[index] != board[i][j]:
                return False
            if len(word) - 1 == index:
                return True
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if ni >= 0 and ni < len(board) and nj >= 0 and nj < len(board[0]):
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        if dfs(ni, nj, board, visited, word, index + 1):
                            return True
                        visited[ni][nj] = 0
            return False
            
        for i in xrange(0, len(board)):
            for j in xrange(0, len(board[0])):
                visited[i][j] = 1
                if dfs(i, j, board, visited, word, 0):
                    return True
                visited[i][j] = 0
        return False