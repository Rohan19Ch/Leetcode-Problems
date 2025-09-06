"""
LeetCode Problem 103: Binary Tree Zigzag Level Order Traversal

Problem Description:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) for the queue and result array

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

Approach: Level order traversal, reverse alternate levels (odd-indexed levels).
"""

def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        level = 0
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
            if level%2 != 0:
                ans.reverse()
            result.append(ans)
            level += 1
        return result  