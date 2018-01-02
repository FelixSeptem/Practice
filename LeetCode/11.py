# -*- coding:utf-8 -*-  


'''
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                ans[i + j] += int(n1) * int(n2)
                ans[i + j + 1] += ans[i + j] / 10
                ans[i + j] %= 10
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return "".join(map(str, ans[::-1]))


'''
46. Permutations
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.get_permute([], nums, result)
        return result

    def get_permute(self, current, num, result):
        if not num:
            result.append(current + [])
            return
        for i, v in enumerate(num):
            current.append(num[i])
            self.get_permute(current, num[:i] + num[i + 1:], result)
            current.pop()

'''
a version via dfs
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = set([])
        def dfs(nums, path, res, visited):
            if len(path) == len(nums):
                res.append(path + [])
                return
            
            for i in xrange(0, len(nums)):
                # if i > 0 and nums[i - 1] == nums[i]:
                #     continue
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    dfs(nums, path, res, visited)
                    path.pop()
                    visited.discard(i)
                    
        dfs(nums, [], res, visited)
        return res
'''


'''
47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.get_permute([], nums, result)
        return result

    def get_permute(self, current, num, result):
        if not num:
            result.append(current + [])
            return
        for i, v in enumerate(num):
            if i - 1 >= 0 and num[i] == num[i - 1]:
                continue
            current.append(num[i])
            self.get_permute(current, num[:i] + num[i + 1:], result)
            current.pop()

'''
a dfs version
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def dfs(nums, res, path, visited):
            if len(path) == len(nums):
                res.append(path + [])
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
                    continue
                visited |= {i}
                path.append(nums[i])
                dfs(nums, res, path, visited)
                path.pop()
                visited -= {i}
            
        dfs(nums, res, [], set())
        return res
'''