class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # if sum is odd, straightaway impossible
        if total % 2 != 0:
            return False
        
        target = sum(nums) // 2
        # dp[s]: is it possible to partition sum s from the num we've seen so far
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
        
        return dp[target]