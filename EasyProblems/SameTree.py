"""
LeetCode Problem 100: Same Tree

Problem Description:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.

Time Complexity: O(min(m,n)) where m and n are the number of nodes in each tree
Space Complexity: O(min(m,n)) for the recursion stack

Example:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

def isSameTree(self, p, q):
	if p == None and q == None:
		return True
	if p == None or q == None or p.val != q.val:
		return False
	return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

