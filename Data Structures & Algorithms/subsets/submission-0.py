class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):
            # Base case
            if i >= len(nums):
                result.append(subset[:])
                return
            
            # Decision 1: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Decision 2: exclude nums[i]
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return result