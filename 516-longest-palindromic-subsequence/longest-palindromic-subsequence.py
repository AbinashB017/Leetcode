class Solution:
    def lcs(self,i,j,s1,s2,dp):
        if i==0 or j==0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]    
        if s1[i-1]==s2[j-1]:
            dp[i][j]=1+self.lcs(i-1,j-1,s1,s2,dp) 
        else:
            dp[i][j]=max(self.lcs(i-1,j,s1,s2,dp),self.lcs(i,j-1,s1,s2,dp))
        return dp[i][j]           
    def longestPalindromeSubseq(self, s: str) -> int:
        s2=s[::-1]
        n=len(s)
        m=len(s2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.lcs(n,m,s,s2,dp)
        