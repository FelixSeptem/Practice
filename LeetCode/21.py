# -*- coding:utf-8 -*-  
'''
86. Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        sHead = sDummy = ListNode(-1)
        p = dummy
        while p and p.next:
            if p.next.val < x:
                sDummy.next = p.next
                p.next = p.next.next
                sDummy = sDummy.next
            else:
                p = p.next
            # if you change p.next then make sure you wouldn't change p in next run
        sDummy.next = dummy.next
        return sHead.next


'''
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1
        m -= 1
        n -= 1
        while end >= 0 and m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[end] = nums1[m]
                m -= 1
            else:
                nums1[end] = nums2[n]
                n -= 1
            end -= 1
                
        while n >= 0:
            nums1[end] = nums2[n]
            end -= 1
            n -= 1


'''
89. Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return [0]
        ans = [0] * (2 ** n) 
        ans[1] = 1
        mask = 0x01
        i = 1
        while i < n:
            mask <<= 1
            for j in range(0, 2**i):
                root = (2**i)
                ans[root + j] = ans[root - j - 1] | mask
            i += 1
        return ans


'''
90. Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start, nums, path, res, visited):
            res.append(path + [])
            
            for i in xrange(start, len(nums)):
                if start != i and nums[i] == nums[i - 1]:
                    continue
                if i not in visited:
                    visited[i] = 1
                    path.append(nums[i])
                    dfs(i + 1, nums, path, res, visited)
                    path.pop()
                    del visited[i]
        
        nums.sort()
        res = []
        visited = {}
        dfs(0, nums, [], res, visited)
        return res