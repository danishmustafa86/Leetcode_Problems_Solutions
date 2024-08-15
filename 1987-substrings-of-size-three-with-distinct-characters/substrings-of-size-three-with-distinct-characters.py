class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        if len(s)<3:
            return 0
        swin = list(s[:3])

        if len(set(swin)) == 3:
            count += 1
        for i in range(3, len(s)):
            swin.pop(0)
            swin.append(s[i])
            if len(set(swin)) == 3:
                count += 1
        return count 


