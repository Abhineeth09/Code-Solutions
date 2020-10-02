# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.tree1=''
        tree2=''
        def dfs(p,q):
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val!=q.val:
                return False
            return dfs(p.left,q.left) and dfs(p.right,q.right)
                    
        return dfs(p,q)
                    