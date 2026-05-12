class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        candidates.sort()
        def backtrack(i):
            # Base case
            if sum(combination) == target:
                result.append(combination[:])
                return

            if i >= len(candidates) or sum(combination) > target:
                return
            
            # Decision 1: include elememt
            combination.append(candidates[i])
            backtrack(i+1)
            # Decision 2: exclude element
            curr = combination.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return result