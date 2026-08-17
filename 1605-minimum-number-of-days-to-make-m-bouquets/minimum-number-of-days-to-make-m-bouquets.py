class Solution:
    def possible(self,arr,day,m,k):
        cnt=0
        noB=0
        for i in range(len(arr)):
            if arr[i]<=day:
                cnt+=1
            else:
                noB+=cnt//k
                cnt=0
        noB+=cnt//k
        if noB>=m:
            return True
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while low<=high:
            mid=int(low+(high-low)/2)
            if self.possible(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans        
