class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
      n=len(nums)
      nums.sort()
      st=set()
      for i in range(n) :
        j=i+1
        k=n-1
        while j<k:
            sum=nums[i]+nums[j]+nums[k]
            if i!=j and j!=k and sum==0:
                st.add((nums[i],nums[j],nums[k]))
                j+=1
                k-=1
            elif sum>0:
                k-=1
            else :
                j+=1

      ans= []
      for x in st:
        ans.append(list(x))

      return ans                    
