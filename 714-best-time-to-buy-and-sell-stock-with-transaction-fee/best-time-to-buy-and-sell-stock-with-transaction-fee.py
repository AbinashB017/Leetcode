class Solution:
    def solve(self,index,buy,fee,nums,dp):
        if index>=len(nums):
            return 0
        if dp[index][buy]!=-1:
            return dp[index][buy]
        profit=0
        if buy==1:
            profit=max(-nums[index]+self.solve(index+1,0,fee,nums,dp),self.solve(index+1,1,fee,nums,dp))        
        else:
            profit=max(nums[index]-fee +self.solve(index+1,1,fee,nums,dp),self.solve(index+1,0,fee,nums,dp)) 
        dp[index][buy]=profit
        return dp[index][buy]

       
        
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*(2)for _ in range(n)]
        return self.solve(0,1,fee,prices,dp)