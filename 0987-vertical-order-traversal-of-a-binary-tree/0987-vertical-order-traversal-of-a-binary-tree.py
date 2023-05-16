# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        l=[]
        # print(root)
        def traverse(node,level,order):
            # print(node)
            if node==None:
                return 
            else:
                l.append((node.val,level,order))
                if node.left:
                    traverse(node.left,level+1,order-1)
                if node.right:
                    traverse(node.right,level+1,order+1)
                    
            
        traverse(root,0,0)
        l.sort(key=lambda x:(x[2],x[1],x[0]))
        d={}
        for i,j,k in l:
            if k not in d:
                d[k]=[i]
            else:
                d[k].append(i)
        # print(l,d)
        return d.values()