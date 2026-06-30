class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [None] * (amount + 1)
        dp[0] = 0
        
        def dfs(amt):
            if amt < 0:
                return float('inf')

            if dp[amt] is not None:
                return dp[amt]
            
            best = float('inf')
            for coin in coins:
                best = min(best, dfs(amt - coin) + 1)
            
            dp[amt] = best
            
            return best
        
        dfs(amount)
        return dp[-1] if dp[-1] != float('inf') else -1