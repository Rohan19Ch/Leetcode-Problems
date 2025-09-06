"""
LeetCode Problem 110: Balanced Binary Tree

Problem Description:
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the left and right subtrees 
of every node differ in height by no more than 1.

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree (due to recursion stack)

Example:
Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
"""

def isBalanced(self, root):
	if root == None:
		return True
	