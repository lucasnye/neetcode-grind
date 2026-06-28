class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]

        ans = nums[0]
        
        for num in nums[1:]:
            old_min, old_max = cur_min, cur_max

            cur_max = max(num, old_min * num, old_max * num)
            cur_min = min(num, old_min * num, old_max * num)

            ans = max(ans, cur_max)
        
        return ans