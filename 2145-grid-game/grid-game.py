class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        r1_sum = sum(grid[0])
        minSum = float("inf")
        r2_sum = 0
        for i in range(len(grid[0])):
            r1_sum -= grid[0][i]
            minSum = min(minSum, max(r1_sum, r2_sum))
            r2_sum += grid[1][i]
        return minSum

