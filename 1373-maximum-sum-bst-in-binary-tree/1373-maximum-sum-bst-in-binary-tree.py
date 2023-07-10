# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def postorder(root):
            if root!=None:
                leftsubtree=postorder(root.left)
                rightsubtree=postorder(root.right)
                 
                if root.val>leftsubtree[1] and root.val<rightsubtree[2]:
                    sm=leftsubtree[0]+rightsubtree[0]+root.val
                    ans[0]=max(sm,ans[0])
                    mx=max(rightsubtree[1],root.val)
                    mn=min(leftsubtree[2],root.val)
                else:
                    sm=max(leftsubtree[0],rightsubtree[0])
                    mx=99999
                    mn=-99999
                # print([sm,mx,mn,root.val])
                
                return [sm,mx,mn]
                 
                     
            else:
                # print([0,-99999,99999,root])
                return [0,-99999,99999]
            
        postorder(root)
        return ans[-1]
    
            