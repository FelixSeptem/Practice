# -*- coding:utf-8 -*-  

'''
8. String to Integer (atoi)
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases. 
If you want a challenge, please do not see below and ask yourself what are the possible input cases.
'''
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        sign = 1
        if not s:
            return 0
        if s[0] in ["+", "-"]:
            if s[0] == "-":
                sign = -1
            s = s[1:]
        ans = 0
        for c in s:
            if c.isdigit():
                ans = ans * 10 + int(c)
            else:
                break
        ans *= sign
        if ans > 0x7fffffff:
            return 0x7fffffff
        if ans < -0x80000000:
            return -0x80000000
        return ans


'''
9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x /= 10
        return x == half or half / 10 == x


'''
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = left = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans


'''
12. Integer to Roman
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        literals = ["M", "D", "C", "L", "X", "V", "I"]
        for idx in [0, 2, 4]:
            k = num / values[literals[idx]]
            re = (num % values[literals[idx]]) / values[literals[idx + 2]]
            ans += k * literals[idx]
            if re >= 9:
                ans += literals[idx + 2] + literals[idx] 
            elif re >= 5:
                ans += literals[idx + 1] + (re - 5) * literals[idx + 2]
            elif re == 4:
                ans += literals[idx + 2] + literals[idx + 1]
            else:
                ans += re * literals[idx + 2]
            num %= values[literals[idx + 2]]
        return ans


'''
13. Roman to Integer
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1, "V": 5, "X":10,"L":50,"C":100, "D":500, "M":1000}
        ans = 0
        for i in xrange(0, len(s) - 1):
            c = s[i]
            cafter = s[i + 1]
            if d[c] < d[cafter]:
                ans -= d[c]
            else:
                ans += d[c]
        ans += d[s[-1]]
        return ans