class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)
        def recurse(amt):
            # Base case
            if amt == 0:
                return 0
            
            if amt < 0:
                return -1
            
            if dp[amt] is not None:
                return dp[amt]
            
            least = float('inf')
            for coin in coins:
                result = recurse(amt - coin)
                if result != -1:
                    least = min(least, result + 1)

            dp[amt] = -1 if least == float('inf') else least
            return dp[amt]
        
        return recurse(amount)