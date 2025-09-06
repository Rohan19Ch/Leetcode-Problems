"""
LeetCode Problem 94: Binary Tree Inorder Traversal

Problem Description:
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Inorder traversal visits nodes in the order: Left -> Root -> Right

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) for the result array and O(h) for recursion stack

Example:
Input: root = [1,null,2,3]
Output: [1,3,2]

Note: This implementation also validates if the tree is a valid BST by checking 
if the inorder traversal is sorted.
"""

def helper(root, result):
	if root:
		helper(root.left, result)
		result.append(root.val)
		helper(root.right, result)
class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		result = []
		helper(root, result)
		for i in range(1, len(result)):#Inorder traversal of a BST should be Sorted
			if result[i] <= result[i-1]:
				return False
		return True