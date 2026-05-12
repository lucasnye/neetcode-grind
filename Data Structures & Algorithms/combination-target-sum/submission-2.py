class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(i):
            # Base case
            if sum(combination) == target:
                result.append(combination[:])
                return
            
            if i >= len(nums) or sum(combination) > target:
                return

            # Decision 1: include the same element
            combination.append(nums[i])
            backtrack(i)

            # Decision 2: include the new element
            combination.pop()
            backtrack(i+1)

            # Decision 3: Neither include the same element nor the new element
            # combination.pop()
        
        backtrack(0)
        return result