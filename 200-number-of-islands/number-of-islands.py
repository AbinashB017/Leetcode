class Solution:
    def dfs(self,row,col,grid,vis):
        vis[row][col]=1
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for i in range(4):
            nr=row+dr[i]
            nc=col+dc[i]
            if (0<=nr<len(grid)) and (0<=nc<len(grid[0])) and grid[nr][nc]=="1" and vis[nr][nc]!=1:
                self.dfs(nr,nc,grid,vis)

    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        vis=[[0]*(n)for _ in range(m)]
        cnt=0
        for i in range(m) :
            for j in range(n):     
                if vis[i][j]!=1 and grid[i][j]=="1":
                    cnt+=1
                    self.dfs(i,j,grid,vis)
                          
        return cnt