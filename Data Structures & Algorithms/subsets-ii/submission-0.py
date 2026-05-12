class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        n = len(nums)
        
        def backtrack(i):
            if i >= len(nums):
                result.append(subset[:])
                return
        
            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return result