# -*- coding:utf-8 -*-  
'''
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n

        for i in xrange(1, m):
            pre = 1
            for j in xrange(1, n):
                dp[j] = dp[j] + pre
                pre = dp[j]
        return dp[-1]


'''
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''
class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        if grid[0][0] == 1:
            return 0
        dp = [[0] * len(grid[0]) for _ in xrange(0 ,len(grid))]
        dp[0][0] = 1 if grid[0][0] == 0 else 0
        for i in xrange(1, len(grid)):
            if grid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        
        for j in xrange(1, len(grid[0])):
            if grid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


'''
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        dp = [0 for _ in xrange(0, len(grid[0]))]
        dp[0] = grid[0][0]
        
        for j in xrange(1, len(grid[0])):
            dp[j] = dp[j - 1] + grid[0][j]
            
        for i in xrange(1, len(grid)):
            pre = dp[0] + grid[i][0]
            for j in xrange(1, len(grid[0])):
                dp[j] = min(dp[j], pre) + grid[i][j]
                pre = dp[j]
            dp[0] += grid[i][0]
        
        return dp[-1]