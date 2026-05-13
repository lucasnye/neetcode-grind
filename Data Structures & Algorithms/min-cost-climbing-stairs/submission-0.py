class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [None] * n
        dp[n-1] = 0

        def dfs(i):
            if i >= n:
                return 0
            
            if dp[i]:
                temp = dp[i]
            
            else:
                temp = cost[i] + min(dfs(i+1), dfs(i+2))
                dp[i] = temp
            
            return temp

        return min(dfs(0), dfs(1))