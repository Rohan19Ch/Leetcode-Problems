"""
LeetCode Problem 104: Maximum Depth of Binary Tree

Problem Description:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree (recursion stack)

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
"""

def maxDepth(self, root):
	if root == None:
		return 0
	if root.left == None and root.right == None:
		return 1
	return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))