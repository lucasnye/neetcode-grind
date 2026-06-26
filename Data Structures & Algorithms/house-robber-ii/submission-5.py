class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        def rob_range(houses):
            n = len(houses)
            if n < 2:
                return houses[0]
            
            prev1, prev2 = houses[0], max(houses[0], houses[1])

            for i in range(2, n):
                prev1, prev2 = prev2, max(houses[i] + prev1, prev2)
            
            return prev2
        
        return max(rob_range(nums[1:]), rob_range(nums[:-1]))