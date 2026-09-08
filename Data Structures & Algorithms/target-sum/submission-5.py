from typing import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (num, running_sum): no. of ways
        def dp(i, running_sum):
            if i == len(nums):
                return 1 if running_sum == target else 0
            if (i, running_sum) in memo:
                return memo[(i, running_sum)]
            
            memo[(i, running_sum)] = dp(i + 1, running_sum + nums[i]) + dp(i + 1, running_sum - nums[i])
            return memo[(i, running_sum)]

        return dp(0, 0)