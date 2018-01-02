# -*- coding:utf-8 -*-  


'''
36. Valid Sudoku
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cacheCol = [[0] * 9 for _ in xrange(0, 10)]
        cacheRow = [[0] * 9 for _ in xrange(0, 10)]
        cacheBox = [[0] * 9 for _ in xrange(0, 10)]
        
        for i in xrange(0, 9):
            for j in xrange(0, 9):
                ib = (i/3)*3 + j/3
                if board[i][j] == ".":
                    continue
                num = int(board[i][j]) - 1
                if cacheRow[i][num] != 0 or cacheCol[j][num] != 0 or cacheBox[ib][num] != 0:
                    return False
                cacheRow[i][num] = 1
                cacheCol[j][num] = 1
                cacheBox[ib][num] = 1
        return True


'''
38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        n -= 1
        while n > 0:
            res = ""
            pre = ans[0]
            count = 1
            for i in range(1, len(ans)):
                if pre == ans[i]:
                    count += 1
                else:
                    res += str(count) + pre
                    pre = ans[i]
                    count = 1
            res += str(count) + pre
            ans = res
            n -= 1
        return ans


'''
39. Combination Sum
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        dp = [[[]]] + [[] for i in xrange(target)]
        for i in xrange(1, target + 1):
            for number in candidates:
                if number > i: break
                for L in dp[i - number]:
                    if not L or number >= L[-1]: dp[i] += L + [number],
        return dp[target]


'''
40. Combination Sum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        dp = [set() for i in xrange(target+1)]
        dp[0].add(())
        for num in candidates:
            for t in xrange(target, num-1, -1):
                for prev in dp[t-num]:
                    dp[t].add(prev + (num,))
        return list(dp[-1])