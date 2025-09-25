class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        repeated = -1
        length = len(grid) * (len(grid))
        seen = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in seen:
                    repeated = grid[i][j]
                    break
                else:
                    seen[grid[i][j]] = grid[j]
            if repeated != -1:
                break
        curSum = sum(sum(grid[i]) for i in range(len(grid)))
        totalSum = length * (length + 1) // 2
        missing = totalSum - (curSum - repeated)
        print(curSum, missing)

        return [repeated, missing]