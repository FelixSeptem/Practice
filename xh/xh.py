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
                
"""
122. Best Time to Buy and Sell Stock II
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
"""
class Solution:
    def maxProfit1(self, prices):
        if len(prices)<2:
            return 0
        dp = [[0, -prices[0]]]
        for i in range(1, len(prices)):
            dp.append([max(dp[i-1][0], dp[i-1][1]+prices[i]), max(dp[i-1][0]-prices[i], dp[i-1][1])])
        return dp[len(prices)-1][0]

    def maxProfit2(self, prices):
        if len(prices)<2:
            return 0
        profile = 0
        for i in range(len(prices)-2):
            profile += max(0, prices[i+1]-prices[i])
        return profile
        
"""
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        step = k%len(nums)
        for i in range(len(nums)/2):
            nums[i], nums[length-i-1] = nums[length-i-1], nums[i]
        
        for i in range(step/2):
            nums[i], nums[step-i-1] = nums[step-i-1], nums[i]

        for i in range(step, (length+step)/2):
            nums[i], nums[length-i-1+step] = nums[length-i-1+step], nums[i]

"""
27. Remove Element
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,3,0,0], your answer will be accepted.
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
class Solution:
    def removeElement(self, nums, val):
        while val in nums: nums.remove(val)

"""
26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
 

Constraints:

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.
"""
class Solution:
    def removeDuplicates(self, nums):
        if not nums: 
            return 0
        
        next_new = 0
        for j in range(1, len(nums)):
            if nums[next_new] != nums[j]:
                nums[next_new + 1] = nums[j]
                next_new += 1
        nums = nums[:next_new+1]
        return len(nums)

"""
66. Plus One
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
class Solution:
    def plusOne(self, digits):
        if len(digits)==0:
            return digits
        length = len(digits)
        pivot = 0
        for d in range(length-1, -1, -1):
            if digits[d]==9:
                digits[d] = 0
                pivot = 1
            else:
                digits[d] += 1
                break
        if pivot==1 and digits[0]==0:
            res = [1]
            res.extend(digits)
            return res
        return digits

"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
class Solution:
    def twoSum(self, nums, target):
        m = {}
        for i, n in enumerate(nums):
            m[n] = i
        for i, n in enumerate(nums):
            idx = m.get(target-n, -1)
            if idx>=0 and idx!=i:
                return [i, idx]
        return None