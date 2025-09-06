"""
LeetCode Problem 101: Symmetric Tree

Problem Description:
Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree (recursion stack)

Example:
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
"""

def isSame(p, q):
    if p == None and q == None:
        return True
    if p == None or q == None or p.val != q.val:
        return False
    return (isSame(p.left, q.right) and isSame(p.right, q.left))
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        answer = isSame(root.left, root.right)
        return answer