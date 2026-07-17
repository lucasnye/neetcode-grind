class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                res = max(res, sum(nums[i:j+1]))
        
        return res