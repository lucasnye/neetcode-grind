class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        n = len(nums)

        used = [False] * n

        def backtrack():
            if len(permutation) == n:
                result.append(permutation[:])
                return
            
            for i in range(n):
                if not used[i]:
                    permutation.append(nums[i])
                    used[i] = True
                    backtrack()
                    permutation.pop()
                    used[i] = False
        
        backtrack()
        return result