# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #every node between the LCA and root are common ancestors
    
        if root == p or root == q or not root:
            return root
        else:
            right = self.lowestCommonAncestor(root.right, p, q)
            left =  self.lowestCommonAncestor(root.left, p, q)

            # if have the left and right children -> return the root
            if left and right:
                return root
            # if children are on one side -> return the side that is not None    
            else:
                return left or right



        
