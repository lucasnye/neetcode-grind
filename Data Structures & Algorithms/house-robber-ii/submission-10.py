class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]

        def rob_range(houses):
            if len(houses) == 1:
                return houses[0]

            prev = houses[0]
            cur = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                prev, cur = cur, max(cur, prev + houses[i])
            
            return cur
        
        return max(rob_range(nums[1:]), rob_range(nums[:-1]))