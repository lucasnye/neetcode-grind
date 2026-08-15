class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            sell (0) | resting (1) | hold (2)
        1      0            0          -1
        2      1            0             
        4
        """
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]

        dp[0][2] = -prices[0]

        for r in range(1, n):
            dp[r][0] = dp[r-1][2] + prices[r]
            dp[r][1] = max(dp[r-1][0], dp[r-1][1])
            dp[r][2] = max(dp[r-1][2], dp[r-1][1] - prices[r])

        return max(dp[n-1][0], dp[n-1][1])