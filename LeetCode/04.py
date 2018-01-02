# -*- coding:utf-8 -*-  

'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        longest = strs[0]
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]


'''
15. 3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Example:
Given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in xrange(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1  
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    res.append((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return res
  

'''
16. 3Sum Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.
Example:
Given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        diff = 0x7fffffff
        for i in xrange(0, len(nums)):
            start, end = i + 1, len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum > target:
                    if abs(target - sum) < diff:
                        diff = abs(target - sum)
                        ans = sum
                    end -= 1
                else:
                    if abs(target - sum) < diff:
                        diff = abs(target - sum)
                        ans = sum
                    start += 1
        return ans