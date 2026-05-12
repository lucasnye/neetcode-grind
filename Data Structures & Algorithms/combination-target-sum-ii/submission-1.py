class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, subset, total):
            if total == target:
                result.append(subset[:])
                return

            if i >= n or total > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])

            subset.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, subset, total)


        dfs(0, [], 0)
        return result