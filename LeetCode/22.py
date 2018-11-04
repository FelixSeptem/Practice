# -*- coding:utf-8 -*-  
'''
91. Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in xrange(1, len(s)):
            pre = int(s[i-1])
            cur = int(s[i])
            num = pre * 10 + cur
            if cur != 0:
                dp[i+1] += dp[i]
            if pre != 0 and 0 < num <= 26:
                dp[i+1] += dp[i - 1]
        return dp[-1]


'''
92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        def reverse(root, prep, k):
            cur = root
            pre = None
            next = None
            while cur and k > 0:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
                k -= 1
            root.next = next
            prep.next = pre
            return pre
            
        dummy = ListNode(-1)
        dummy.next = head
        k = 1
        p = dummy
        start = None
        while p:
            if k == m:
                start = p
            if k == n + 1:
                reverse(start.next, start, n - m + 1)
                return dummy.next
            k += 1
            p = p.next


'''
93. Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        n = len(s)
        def isValid(num):
            if len(num) == 1:
                return True
            if len(num) > 1 and num[0] != "0" and int(num) <= 255:
                return True
            return False
            
        for i in range(0, min(3, n - 3)):
            a = s[:i+1]
            if not isValid(a):
                break
            for j in range(i + 1, min(i + 4, n - 2)):
                b = s[i+1:j+1]
                if not isValid(b):
                    break
                for k in range(j + 1, min(j + 4, n - 1)):
                    c = s[j+1:k+1]
                    d = s[k+1:]
                    if not isValid(c):
                        break
                    if not isValid(d):
                        continue
                    ans.append("{}.{}.{}.{}".format(a, b, c, d))
        return ans


'''
94. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], [(1, root)]
        while stack:
            p = stack.pop()
            if not p[1]: continue
            stack.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)]) if p[0] != 0 else res.append(p[1].val)
        return res