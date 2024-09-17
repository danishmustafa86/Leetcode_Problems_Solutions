class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(),s2.split()
        res = {}
        ans = []

        for word in s1 + s2:
            res[word] = res.get(word,0) + 1
        for key in res:
            if res[key] == 1:
                ans.append(key)
        return ans