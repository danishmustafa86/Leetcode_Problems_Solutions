class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}
        def backtrack(i):
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]
                
            res = []
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w not in wordDict:
                    continue
                string = backtrack(j+1)
                # if not string:
                #     continue
                for substr in string:
                    sentence = w
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)
            cache[i] = res
            return res

        return backtrack(0)
        


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         def backtrack(i):
#             if i == len(s):
#                 return res.append(" ".join(cur))
#             for j in range(i, len(s)):
#                 curSt = s[i:j+1]
#                 if curSt in wordDict:
#                     cur.append(curSt)
#                     backtrack(j + 1)
#                     cur.pop()
                    
#         cur = []
#         res = []
#         backtrack(0)
#         return res