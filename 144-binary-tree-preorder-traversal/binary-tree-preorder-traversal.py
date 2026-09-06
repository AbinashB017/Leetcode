# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,node,res):
        if node is None:
            return 
        res.append(node.val)
        self.solve(node.left,res)
        self.solve(node.right,res)    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         res=[]
         self.solve(root,res)
         return res
        