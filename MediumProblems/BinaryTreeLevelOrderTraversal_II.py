"""
LeetCode Problem 107: Binary Tree Level Order Traversal II

Problem Description:
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) for the queue and result array

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

Approach: Standard BFS level order traversal, then reverse the result.
"""

def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        result = []
        while len(queue) != 0:
            ans = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.left != None:
                    queue.append(curr.left)
                if curr.right != None:
                    queue.append(curr.right)
                ans.append(curr.val)
            result.append(ans)
        result.reverse()
        return result    