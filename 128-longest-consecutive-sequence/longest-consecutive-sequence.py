class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        longest=1
        st=set()
        for x in nums:
            st.add(x)
        for it in st:
            if (it-1) not in st:
                cnt=1
                x=it
                while (x+1) in st:
                    x+=1
                    cnt+=1
                longest=max(longest,cnt)

        return longest            
                     
