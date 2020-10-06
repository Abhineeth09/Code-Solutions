# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    	#Check if the right child of the left subtree and left child of the right subtree are equal
    	#Similarly check if the remaining two nodes are equal
    	#If thats the case, try for all nodes 
    	#Else return False
        def dfs(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val==right.val and dfs(left.right,right.left) and dfs(left.left,right.right)
        return dfs(root,root)