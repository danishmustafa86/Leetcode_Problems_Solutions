from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tcount = Counter(t)
        window = {}

        have, need = 0, len(tcount)
        res, minlen = [-1, -1], float("inf")
        r = 0
        
        for l in range(len(s)):
            c = s[l]
            window[c] = 1 + window.get(c, 0)
            
            if c in tcount and window[c] == tcount[c]:
                have += 1
            
            while have == need:
                if (l - r + 1) < minlen:
                    res = [r, l]
                    minlen = l - r + 1
                
                window[s[r]] -= 1
                if s[r] in tcount and window[s[r]] < tcount[s[r]]:
                    have -= 1
                
                r += 1
        
        r, l = res
        return s[r:l+1] if minlen != float("inf") else ""
