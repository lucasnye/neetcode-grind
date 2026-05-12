class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr):
            total = sum(curr)
            if i >= len(nums) or total > target:
                return
            
            if total == target:
                result.append(curr[:])
                return
            
            curr.append(nums[i])
            dfs(i, curr)

            curr.pop()
            dfs(i + 1, curr)
        
        dfs(0, [])
        return result