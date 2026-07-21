class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i], -1, -1):
                if i + j < len(nums):
                    dp[i] = min(dp[i + j] + 1, dp[i])

        return dp[0]