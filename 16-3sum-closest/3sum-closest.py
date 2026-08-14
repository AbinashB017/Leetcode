class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if abs(sum-target)< abs(res-target):
                    res=sum
                if target==sum:
                    return sum
                if sum<target:
                    l+=1
                else:
                    r-=1
        return res                

        