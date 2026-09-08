from typing import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for remainder, count in dp.items():
                next_dp[remainder + num] += count
                next_dp[remainder - num] += count
            dp = next_dp
        
        return dp[target]