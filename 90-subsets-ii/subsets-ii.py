class Solution:
    def solve(self,index,nums,ans,temp):
        ans.append(temp.copy())
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            temp.append(nums[i])
            self.solve(i+1,nums,ans,temp)
            temp.pop()    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp=[]
        ans=[]
        self.solve(0,nums,ans,temp)
        return ans
        