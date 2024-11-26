class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        hsh = defaultdict(int)
        for f, s in trust:
            hsh[f] -= 1
            hsh[s] += 1
        for i in range(1, n+1):
            if hsh[i] == n - 1:
                return i
        return -1


