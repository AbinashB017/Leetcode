class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        res=[]
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for i in freq:
            if freq[i]==2:
                res.append(i)
        return res            