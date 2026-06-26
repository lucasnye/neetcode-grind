class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n < 2:
            return nums[0]
        
        # dp = [0] * n
        prev1, prev2 = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            prev1, prev2 = prev2, max(nums[i] + prev1, prev2)
        
        return prev2