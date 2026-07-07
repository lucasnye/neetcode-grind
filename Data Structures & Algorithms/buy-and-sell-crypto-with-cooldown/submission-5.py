class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. currently holding a stock
        # hold -> hold, cool -> hold
        # 2. just sold a stock
        # hold -> sold
        # 3. rest/cool down
        # cool -> cool, sold -> cool

        # max profit while holding current stock
        hold = -prices[0]
        # max profit when just sold stock
        sold = 0
        # max profit when cooling down or resting
        cool = 0

        for price in prices[1:]:
            old_hold, old_sold, old_cool = hold, sold, cool
            hold = max(old_hold, old_cool - price)
            sold = old_hold + price
            cool = max(old_cool, old_sold)
        
        return max(sold, cool)