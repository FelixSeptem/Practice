# -*- coding:utf-8 -*-  
'''
71. Simplify Path
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path2 = []
        for x in path.split('/'):
            if not x =='':path2.append(x)
        for x in path2:
            if x == '.':continue
            elif x == '..':
                if len(stack)==0:continue
                else:stack.pop()
            else:stack.append(x)
        return '/'+ '/'.join(stack)


'''
73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        colZeroFlag = False
        for i in xrange(0, len(matrix)):
            if matrix[i][0] == 0:
                colZeroFlag = True
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        
        for i in reversed(xrange(0, len(matrix))):
            for j in reversed(xrange(1, len(matrix[0]))):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if colZeroFlag:
                matrix[i][0] = 0


'''
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        column = len(matrix[0])
        row = len(matrix)
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        start_row = 0
        start_column = column - 1
        while start_row < row and start_column >= 0:
            if matrix[start_row][start_column] == target:
                return True
            elif matrix[start_row][start_column] > target:
                start_column -= 1
            elif matrix[start_row][start_column] < target:
                start_row += 1
        return False


'''
75. Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place 
so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x = y = z = -1
        for i in xrange(0, len(nums)):
            if nums[i] == 0:
                x += 1
                y += 1
                z += 1
                if z != -1:
                    nums[z] = 2
                if y != -1:
                    nums[y] = 1
                nums[x] = 0
            elif nums[i] == 1:
                y += 1
                z += 1
                nums[z] = 2
                if x != -1:
                    nums[x] = 0
                if y != -1:
                    nums[y] = 1
            elif nums[i] == 2:
                z += 1
                if y != -1:
                    nums[y] = 1
                if x != -1:
                    nums[x] = 0
                nums[z] = 2


'''
76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
'''
class Solution(object):
    import collections
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        score = 0
        wanted = collections.Counter(t)
        start, end = len(s), 3 * len(s)
        d = {}
        deq = collections.deque([])
        for i, c in enumerate(s):
            if c in wanted:
                deq.append(i)
                d[c] = d.get(c, 0) + 1
                if d[c] <= wanted[c]:
                    score += 1
                while deq and d[s[deq[0]]] > wanted[s[deq[0]]]:
                    d[s[deq.popleft()]] -= 1
                if score == len(t) and deq[-1] - deq[0] < end - start:
                    start, end = deq[0], deq[-1]
        return s[start:end + 1]