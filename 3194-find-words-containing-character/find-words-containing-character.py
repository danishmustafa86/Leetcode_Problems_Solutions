class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ind = []
        for i in range(len(words)):
            if x in words[i]:
                ind.append(i)
        return ind












        # index = []
        # for i in range(len(words)):
        #     lst = list(words[i])
        #     for j in lst:
        #         if j == x:
        #             index.append(i)
        #             break
        # return index