
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        if len(s) < 3:
            return 0
        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                count += 1
        return count

















        # count = 0
        # if len(s)<3:
        #     return 0
        # swin = list(s[:3])

        # if len(set(swin)) == 3:
        #     count += 1
        # for i in range(3, len(s)):
        #     swin.pop(0)
        #     swin.append(s[i])
        #     if len(set(swin)) == 3:
        #         count += 1
        # return count 
