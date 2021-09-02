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