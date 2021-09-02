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