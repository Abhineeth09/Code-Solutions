# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insertBST(prevnode,node,root,val):
            if node:
                #print(node.val)
                prevnode=node
                if val>node.val:
                    insertBST(prevnode,node.right,root,val)
                else:
                    insertBST(prevnode,node.left,root,val)
            else:
                if val>prevnode.val:
                    prevnode.right=TreeNode(val=val)
                else:
                    prevnode.left=TreeNode(val=val)
                #print(prevnode)
                return root
        if not root:
            return TreeNode(val)
        else:
            insertBST(None,root,root,val)
            return root