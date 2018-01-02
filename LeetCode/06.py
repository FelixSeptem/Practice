# -*- coding:utf-8 -*-  


'''
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = ["()", "[]", "{}"]
        for i in xrange(0, len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2]+stack[-1] in d:
                stack.pop()
                stack.pop()
        return len(stack) == 0


'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next
        

'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, path, res, n):
            if len(path) == 2 * n:
                if left == 0:
                    res.append("".join(path))
                return
            
            if left < n:
                path.append("(")
                dfs(left + 1, path, res, n)
                path.pop()
            if left > 0:
                path.append(")")
                dfs(left - 1, path, res, n)
                path.pop()
            
        res = []
        dfs(0, [], res, n)
        return res


'''
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, 
only nodes itself can be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return None
        
        dummy = p0 = ListNode(-1)
        dummy.next = head
        
        while p0.next and p0.next.next:
          p1, p2 = p0.next, p0.next.next
          p0.next, p1.next, p2.next = p2, p2.next, p1
          p0 = p0.next.next
         
        return dummy.next