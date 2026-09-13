class Solution:
    def dfs(self,node,adj,vis):
        vis[node]=1
        for i in adj[node]:
            if vis[i]!=1:
                self.dfs(i,adj,vis)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj=[[]*(n) for _ in range(n)]
        vis=[0]*n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
                
        cnt=0
        for i in range(n):
            if vis[i]!=1:   
                vis[i]=1
                self.dfs(i,adj,vis)
                cnt+=1
        return cnt             
        