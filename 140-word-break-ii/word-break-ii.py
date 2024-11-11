class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(i):
            if i == len(s):
                return res.append(" ".join(cur))
            for j in range(i, len(s)):
                curSt = s[i:j+1]
                if curSt in wordDict:
                    cur.append(curSt)
                    backtrack(j + 1)
                    cur.pop()
                    
        cur = []
        res = []
        backtrack(0)
        return res