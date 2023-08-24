# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(root,key,l):
            
            if root.val==key:
                l.append(root)
                return l
            elif root.val>key:
                
                l.append(root)
                
                return search(root.left,key,l)
            else:
                l.append(root)
                return search(root.right,key,l)
        
        lt=search(root,p.val,[])
    
        lt2=search(root,q.val,[])
        m=min(len(lt),len(lt2))
        for i in range(m-1,-1,-1):
            if lt[i]==lt2[i]:
                return lt[i]
        
        