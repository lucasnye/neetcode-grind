class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        intermediate = nums[0]
        
        for num in nums[1:]:
            intermediate = max(num, intermediate + num)
            largest = max(largest, intermediate)
        
        return largest