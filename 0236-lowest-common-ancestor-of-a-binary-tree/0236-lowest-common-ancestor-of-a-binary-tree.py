# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def preorder(root,p,q):
            if root:
                if root==p or root==q:
                    return root
                left=preorder(root.left,p,q)
                right=preorder(root.right,p,q)
                if left and right:
                    return root
                elif left==None and right:
                    return right
                elif left and right==None:
                    return left
            return None
        return preorder(root,p,q)
                    