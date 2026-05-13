class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [None] * n

        def dfs(i):
            if i >= n:
                return 0
            
            if dp[i] is not None:
                return dp[i]
            
            else:
                dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            
            return dp[i]

        return min(dfs(0), dfs(1))