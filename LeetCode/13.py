# -*- coding:utf-8 -*-  


'''
51. N-Queens
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''
class Solution(object):
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


'''
52. N-Queens II
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''
class Solution(object):
    def totalNQueens(self, n):
        def dfs(board, row):
            if row == n: return 1
            count = 0
            for x in set_n - set(board):
                # check diagonal conflict
                if all(row - i != abs(x - y) for i, y in enumerate(board[:row])):
                    board[row] = x
                    count += dfs(board, row + 1)
                    board[row] = '.'
            return count
        set_n = {i for i in xrange(n)}
        return dfs(['.'] * n, 0)
        

'''
53. Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''        
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        preSum = maxSum = nums[0]
        for i in xrange(1, len(nums)):
            preSum = max(preSum + nums[i], nums[i])
            maxSum = max(maxSum, preSum)
        return maxSum