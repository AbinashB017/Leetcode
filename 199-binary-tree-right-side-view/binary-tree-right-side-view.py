# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rrl(self,node,level,res):
        if node is None:
            return 
        if level==len(res):
            res.append(node.val)
        self.rrl(node.right,level+1,res)
        self.rrl(node.left,level+1,res)    

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        level=0
        self.rrl(root,level,res)
        return res
        