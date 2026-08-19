class Solution:
    def solve(self,index,target,nums,ans,temp):
        if index==len(nums):
            if target==0:
                ans.append(temp.copy())
                return
        if index==len(nums):
            return 
        if nums[index]<=target:
            temp.append(nums[index])
            self.solve(index,target-nums[index],nums,ans,temp)
            temp.pop()
        self.solve(index+1,target,nums,ans,temp)                
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp=[]
        ans=[]
        self.solve(0,target,candidates,ans,temp)
        return ans