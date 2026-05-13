class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def rob_range(houses):
            dp = [None] * len(houses)
            def dfs(i):
                if i >= len(houses):
                    return 0 
                
                if dp[i] is not None:
                    return dp[i]
                
                dp[i] = max(houses[i] + dfs(i+2), dfs(i+1))
        
                return dp[i]
            return dfs(0)

        return max(rob_range(nums[:-1]), rob_range(nums[1:]))