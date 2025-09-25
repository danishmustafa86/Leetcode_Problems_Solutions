class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        l = len(s)
        pos = l+1
        for i in range(l):
            if s[i] == c:
                pos = i
            ans.append(abs(pos - i))        
        for i in range(l-1,-1,-1):
            if s[i] == c:
                pos = i
            ans[i] = min(ans[i],abs(pos - i))
        return ans       
