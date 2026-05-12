class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in nums:
            if i not in duplicate:
                duplicate[i] = 1
                
            else:
                return True
        return False
        