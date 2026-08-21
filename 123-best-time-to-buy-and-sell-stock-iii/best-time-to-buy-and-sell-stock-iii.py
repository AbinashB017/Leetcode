class Solution:
    def solve(self,index,buy,cnt,nums,dp):
        if index==len(nums):
            return 0
        if cnt==0:
            return 0    
        if dp[index][buy][cnt]!=-1:
            return dp[index][buy][cnt]
        profit=0    
        if buy==1:
            profit=max(-nums[index]+self.solve(index+1,0,cnt,nums,dp),self.solve(index+1,1,cnt,nums,dp))    
        else:
            profit=max(nums[index]+self.solve(index+1,1,cnt-1,nums,dp),self.solve(index+1,0,cnt,nums,dp))    

        dp[index][buy][cnt]=profit
        return dp[index][buy][cnt]        
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
        return self.solve(0,1,2,prices,dp)
        