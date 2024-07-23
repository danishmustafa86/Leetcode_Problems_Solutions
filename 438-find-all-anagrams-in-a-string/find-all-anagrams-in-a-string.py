class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr = []
        p = sorted(p)
        pl = len(p)
        n = len(s)
        for i in range(n-pl+1):
            if sorted(s[i:i+pl]) == p :
                arr.append(i)
        return arr