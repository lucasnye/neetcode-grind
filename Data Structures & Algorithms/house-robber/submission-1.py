class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        
        def dfs(i):
            if i >= len(nums):
                return 0 
            
            if dp[i] is not None:
                return dp[i]
            
            dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))
    
            return dp[i]

        return dfs(0)