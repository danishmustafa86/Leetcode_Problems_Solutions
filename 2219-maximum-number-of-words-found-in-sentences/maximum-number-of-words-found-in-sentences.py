class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n = 0
        Max = 0
        for i in sentences:
            lst = list(i)
            n = 0
            for j in i:
                if j == " ":
                    n += 1
            Max = max(n,Max)
        return Max+1