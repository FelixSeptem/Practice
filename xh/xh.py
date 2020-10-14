# -*- coding:utf-8 -*-  
"""
350. Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
# 基础版
class Solution:
    def intersect(self, nums1, nums2):
        m1 = {}
        for k in nums1:
            m1[k] = m1.get(k, 0) + 1
        result = []
        for k in nums2:
            if m1.get(k, 0):
                m1[k] -= 1
                result.append(k)
        return result

# 进阶1 
def intersect(nums1, nums2):
    i, j, k = 0, 0, 0
    length1, length2 = len(nums1), len(nums2)
    result = []
    while i<length1 and j<length2:
        if nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]>nums2[j]:
            j+=1
        else:
            result.append(nums1[i])
            i+=1
            j+=1
    return result

    """
    14. Longest Common Prefix
    Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        def compareTwoStr(s1, s2):
            idx = 0
            l1, l2 = len(s1), len(s2)
            if l1==0 or l2==0:
                return ""
            for i in range(min([l1, l2])):
                if s1[i]==s2[i]:
                    idx = i+1
                else:
                    break
            return s1[:idx]
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        return reduce(compareTwoStr, strs)
                
