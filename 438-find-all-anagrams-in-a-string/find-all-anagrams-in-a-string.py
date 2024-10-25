class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        arr = []
        for i in range(len(s) - len(p) + 1 ):
            if sorted(s[i:i+ len(p)]) == p :
                arr.append(i)

        return arr

