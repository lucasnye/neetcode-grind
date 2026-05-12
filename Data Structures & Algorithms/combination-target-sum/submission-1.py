class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(i):
            total = sum(combination)

            if i >= len(nums) or total > target:
                return
            
            if total == target:
                result.append(combination[:])
                return

            combination.append(nums[i])
            backtrack(i)

            combination.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return result