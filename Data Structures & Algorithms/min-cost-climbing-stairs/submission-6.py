class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n

        def dfs(i):
            if i <= 1:
                return cost[i]
            
            if dp[i] != 0:
                return dp[i]
            
            res = min(dfs(i - 1), dfs(i - 2))
            dp[i] = res + cost[i]

            return dp[i]
        
        return min(dfs(n-1), dfs(n-2))