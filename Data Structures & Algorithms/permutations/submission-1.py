class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(path):
            # Base case: if the current path is the same length as nums, we found a permutation
            if len(path) == len(nums):
                result.append(path[:]) # Append a copy of the path
                return

            for i in range(len(nums)):
                # Skip if the number is already in the current path
                if used[i]:
                    continue
                
                # Make a choice
                used[i] = True
                path.append(nums[i])
                
                # Explore further
                backtrack(path)
                
                # Undo the choice (backtrack)
                path.pop()
                used[i] = False

        result = []
        used = [False] * len(nums)
        backtrack([])
        return result
            