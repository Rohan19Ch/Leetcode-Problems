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