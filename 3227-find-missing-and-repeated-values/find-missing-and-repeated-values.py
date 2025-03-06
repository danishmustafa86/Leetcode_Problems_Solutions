class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        hsh = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in hsh:
                    ans.append(grid[i][j])
                else:
                    hsh[grid[i][j]] = 1
        
        n = 1
        while n <= len(grid) * len(grid):
            if n not in hsh:
                ans.append(n)
            n += 1


        return ans