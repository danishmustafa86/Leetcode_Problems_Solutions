class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Base cases: cost to reach the first and second steps
        if n == 1:
            return cost[0]
        elif n == 2:
            return min(cost[0], cost[1])
        
        # dp[i] will store the minimum cost to reach step i
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Fill the dp array
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # The answer will be the minimum cost to reach either of the last two steps
        return min(dp[n-1], dp[n-2])