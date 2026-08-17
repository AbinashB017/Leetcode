class Solution:
    def sumOfMultiples(self, n: int) -> int:
        arr=[]
        for x in range(n+1):
            if x%3==0 or x%5==0 or x%7==0:
                arr.append(x)
        sum=0        
        for i in arr:
            sum+=i
        return sum            
        