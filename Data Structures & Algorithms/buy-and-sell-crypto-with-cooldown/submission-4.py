class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        hold = float('-inf')
        sold = 0
        cool = 0

        for i in range(n):
            old_hold, old_sold, old_cool = hold, sold, cool

            hold = max(old_hold, old_cool - prices[i])
            sold = old_hold + prices[i]
            cool = max(old_sold, old_cool)
        
        return max(sold, cool)