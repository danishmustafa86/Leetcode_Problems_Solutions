class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hsh = { trust[i][0]:trust[i][1] for i in range(len(trust))}
        temp = 0



        for i in range(1, n+1):
            if i not in hsh:
                for j in range(len(trust)):
                    if i == trust[j][1]:
                        temp += 1
                if temp == n - 1:
                    return i
            temp = 0

        return -1


