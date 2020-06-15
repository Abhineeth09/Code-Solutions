# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getStringRep(self,tree):
        if tree == None:
            return ['']
        return ['('] + self.getStringRep(tree.left)+ [str(tree.val)]+self.getStringRep(tree.right)+ [')']
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        s = ''.join(self.getStringRep(s))
        t = ''.join(self.getStringRep(t))
        return s.find(t)!=-1