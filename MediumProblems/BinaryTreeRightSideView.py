"""
LeetCode Problem 199: Binary Tree Right Side View

Problem Description:
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) for the queue and result array

Example:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []

Approach: Level order traversal, then take the rightmost element from each level.
"""

def rightSideView(self, root: TreeNode) -> List[int]:
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
            result.append(ans)
        final = []   
        for i in result:
            final.append(i[-1])
            
        return final