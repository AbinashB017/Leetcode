class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rev=s[::-1]
        cnt=0
        started = False
        for i in rev:
            if i==" ":
                if started:
                    break
            else:
                started=True
                cnt+=1
        return cnt        