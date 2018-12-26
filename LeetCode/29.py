# -*- coding:utf-8 -*-  
'''
118. Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
      def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ans = [[1] * n for n in range(1, numRows + 1)]
    for i in range(1, numRows + 1):
      for j in range(0, i - 2):
        ans[i - 1][1 + j] = ans[i - 2][j] + ans[i - 2][j + 1]
    return ans

'''
119. Pascal's Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Example:

Input: 3
Output: [1,3,3,1]
'''
class Solution(object):
      def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    fact = [1] * (rowIndex + 1)
    ans = [1] * (rowIndex + 1)
    for i in range(1, rowIndex + 1):
      fact[i] = fact[i - 1] * i
    for i in range(1, rowIndex):
      ans[i] = fact[-1] / (fact[i] * fact[rowIndex - i])
    return ans

'''
120. Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''
class Solution(object):
      def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = [0] * len(triangle)
    dp[0] = triangle[0][0]
    for i in range(1, len(triangle)):
      pre = dp[0]
      for j in range(len(triangle[i])):
        tmp = dp[j]
        if j == 0:
          dp[j] = pre
        elif j == len(triangle[i]) - 1:
          dp[j] = pre
        else:
          dp[j] = min(dp[j], pre)
        dp[j] += triangle[i][j]
        pre = tmp
    return min(dp)