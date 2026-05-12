class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for i in nums:
            length = 1
            start = i
            while (start - 1) in nums:
                start -= 1
            while (start + 1) in nums:
                length += 1
                start += 1
            if length > longest:
                longest = length
        return longest