class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1D approach (most space efficient)
        dp = [1] * n

        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c-1]
        
        return dp[n-1]