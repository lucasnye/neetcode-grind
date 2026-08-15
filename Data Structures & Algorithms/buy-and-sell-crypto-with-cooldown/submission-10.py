class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        cool = 0
        sold = 0

        for i in range(1, len(prices)):
            prev_hold, prev_cool, prev_sold = hold, cool, sold
            hold = max(prev_hold, prev_cool - prices[i])
            cool = max(prev_cool, prev_sold)
            sold = prev_hold + prices[i]
        
        return max(cool, sold)