# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root is None:
            return []
        q=deque()
        flag=False
        q.append(root)
        while q:
            n=len(q)
            level=[]
            for i in range(n):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag==True:
                level=level[::-1]   
            res.append(level) 
            flag = not flag
        return res           

        