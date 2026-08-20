class Solution:
    def solve(self,index,target,nums,ans,temp):
        if target==0:
            ans.append(temp.copy())
            return
       
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            if nums[index]>target:
                break
            temp.append(nums[i])
            self.solve(i+1,target-nums[i],nums,ans,temp)      
            temp.pop()               
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp=[]
        ans=[]
        candidates.sort()
        self.solve(0,target,candidates,ans,temp)
        return ans