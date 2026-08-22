class Solution:
    def dfs(self,row,col,image,ans,color,inicolor):
        ans[row][col]=color
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for i in range(4):
            nr=row+dr[i]
            nc=col+dc[i]
            if (0<=nr<len(image)) and (0<=nc<len(image[0])) and image[nr][nc]==inicolor and ans[nr][nc]!=color:
                self.dfs(nr,nc,image,ans,color,inicolor)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        inicolor=image[sr][sc]
        ans=image
        self.dfs(sr,sc,image,ans,color,inicolor)
        return ans