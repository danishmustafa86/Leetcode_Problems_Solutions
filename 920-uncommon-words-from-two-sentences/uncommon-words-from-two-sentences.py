class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(), s2.split()
        hsh = {}
        res = []

        for val in s1 + s2:
            hsh[val] = hsh.get(val, 0) + 1
        
        for val in hsh:
            if hsh[val] == 1:
                res.append(val)

        return res