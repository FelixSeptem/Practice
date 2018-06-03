# -*- coding:utf-8 -*-  
'''
66. Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digit = (digits[i] + carry) % 10
            carry = 1 if digit < digits[i] else 0
            digits[i] = digit
        if carry == 1:
            return [1] + digits
        return digits


'''
67. Add Binary
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = abs(len(a) - len(b))
        if len(a) > len(b):
            b = "0" * diff + b
        else:
            a = "0" * diff + a
            
        ret = ""
        carry = 0
        ai, bi = len(a) - 1, len(b) - 1
        al, bl = len(a), len(b)
        while ai >= 0 and bi >= 0:
            ac, bc = a[ai], b[bi]
            if ac == "1" and bc == "1":
                if carry == 1:
                    ret += "1"
                else:
                    ret += "0"
                carry = 1
            elif ac == "0" and bc == "0":
                if carry == 1:
                    ret += "1"
                else:
                    ret += "0"
                carry = 0
            else:
                if carry == 1:
                    ret += "0"
                else:
                    ret += "1"

            ai -= 1
            bi -= 1

        if carry == 1:
            ret += "1"
        return ret[::-1]


'''
69. Sqrt(x)
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo = 0
        hi = x
        while lo <= hi:
            mid = (hi + lo) / 2
            v = mid * mid
            if v < x:
                lo = mid + 1
            elif v > x:
                hi = mid - 1
            else:
                return mid
        return hi


'''
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        pre, ppre = 1, 1
        for i in xrange(2, n + 1):
            pre, ppre = ppre+pre, pre
        return pre