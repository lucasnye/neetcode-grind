class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            next_dp = {}

            for curr_sum, count in dp.items():
                plus = curr_sum + num
                minus = curr_sum - num

                next_dp[plus] = next_dp.get(plus, 0) + count
                next_dp[minus] = next_dp.get(minus, 0) + count
                
            dp = next_dp
        
        return dp.get(target, 0)