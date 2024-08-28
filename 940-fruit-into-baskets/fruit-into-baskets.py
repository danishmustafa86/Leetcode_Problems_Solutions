class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hsh = {}
        j = 0
        Max = 0
        for i in range(len(fruits)):
            hsh[fruits[i]] = 1+ hsh.get(fruits[i],0)
            if len(hsh) <= 2:
                Max = max( Max, i-j+1)
            while len(hsh)>2:
                hsh[fruits[j]] -= 1
                if hsh[fruits[j]] == 0:
                    del hsh[fruits[j]]
                j += 1
        return Max