class Solution:
    def minimumChairs(self, s: str) -> int:
        count=0
        maxcount=0
        for i in range(len(s)):
            if s[i]=="E":
                count+=1
                maxcount=max(maxcount,count)
            else:
                count-=1
        return maxcount