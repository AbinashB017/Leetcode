class Solution:
    def solve(self,index,nums,ans,temp):
        if index==len(nums):
            ans.append(temp.copy())
            return
        temp.append(nums[index])
        self.solve(index+1,nums,ans,temp)
        temp.pop()
        self.solve(index+1,nums,ans,temp)    

    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        ans=[]
        self.solve(0,nums,ans,temp)
        return ans
        