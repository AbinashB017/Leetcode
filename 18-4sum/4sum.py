class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        st=set()
        for i in range(n-2):
            for j in range(i+1,n-1):
                k=j+1
                l=n-1
                while k<l:
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==target:
                        st.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif sum>target:
                        l-=1
                    else:
                        k+=1

        ans=[]
        for x in st:
            ans.append(list(x))
        return ans                        


        