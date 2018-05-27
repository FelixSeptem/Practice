# -*- coding:utf-8 -*-  

'''
58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s = s.split()
        if len(s) > 0:
            return len(s[-1])
        return 0


'''
59. Spiral Matrix II
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dirToIndex(x, y, d):
            if d == "r": return (x, y + 1, d) if y + 1 < n and matrix[x][y + 1] == 0 else (x + 1, y, "d")
            elif d == "d": return (x + 1, y, d) if x + 1 < n and matrix[x + 1][y] == 0 else (x, y - 1, "l")
            elif d == "l": return (x, y - 1, d) if y > 0 and matrix[x][y - 1] == 0 else (x - 1, y, "u")
            else: return (x - 1, y, d) if x > 0 and matrix[x - 1][y] == 0 else (x, y +1, "r")
        matrix = [[0 for i in range(1, n + 1)] for j in range(n)]
        num, dir, i, j = 1, "r", 0, 0
        while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1
            i, j, dir = dirToIndex(i, j, dir)
        return matrix 


'''
60. Permutation Sequence
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''
class Solution:
    import math
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if(n==1):
            return str(n)
        s=''
        A=[x for x in range(1,n+1)]
        while(k!=0):
            if(k%math.factorial(n-1)==0):
                x=k//math.factorial(n-1)
                k=k-x*math.factorial(n-1)
                n=n-1
            else:
                x=k//math.factorial(n-1)+1
                k=k-(x-1)*math.factorial(n-1)
                n=n-1
            s=s+str(A[x-1])
            A.pop(x-1)
            if(k==0):
                A.sort(reverse=True)
                for d in A:
                    s=s+str(d)
        return s
        


'''
61. Rotate List
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        nodeCount = 0
        node = head
        while node:
            nodeCount += 1
            node = node.next
        k = k % nodeCount
        
        if k == 0:
            return head
        
        currCount = 0
        node = head
        while currCount < nodeCount - k - 1:
            node = node.next
            currCount += 1
        
        # we should now be at the node at the end of where the new list would be
        leftStart = head
        leftEnd = node
        
        rightStart = node.next
        rightEnd = rightStart
        while rightEnd.next:
            rightEnd = rightEnd.next
        
        rightEnd.next = leftStart
        leftEnd.next = None
        
        head = rightStart
        
        return head