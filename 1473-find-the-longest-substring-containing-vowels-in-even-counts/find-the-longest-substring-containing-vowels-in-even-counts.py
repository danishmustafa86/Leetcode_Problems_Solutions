class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        hsh = {"a":0,"e":0,"i":0,"o":0,"u":0}
        lastSeenIndex = {0:-1,}
        maxl,musk = 0, 0
        
        for i in range(len(s)):
            if s[i] in "aeiou":
                musk ^= 1 << "aeiou".index(s[i])
            if musk in lastSeenIndex:
                maxl = max(maxl, i - lastSeenIndex[musk])
            else:
                lastSeenIndex[musk] = i
        return maxl

        





























































