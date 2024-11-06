class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        resLen = 0
        lstIndex = 0
        for i in range(len(s)):
            for j in range(lstIndex, len(t)):
                if s[i] == t[j]:
                    resLen += 1
                    lstIndex = j + 1
                    break
        return resLen == len(s)








        # hsh = {}
        # resLen = 0
        # for i in t:
        #     hsh[i] = i

        # for i in s:
        #     if i in hsh:
        #         resLen += 1
        # return resLen == len(s)



