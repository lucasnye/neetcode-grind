class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left = 0
        # n = len(s)
        # tracker = {}
        # longest = 0
        # for right in range(n):
        #     if s[right] in tracker and tracker[s[right]] >= left:
        #         left = tracker[s[right]] + 1
            
        #     tracker[s[right]] = right
        #     longest = max(longest, right - left + 1)
        # return longest







    






















        longest = 0
        left = 0
        tracker = {}
        for right in range(len(s)):
            if s[right] in tracker and tracker[s[right]] >= left:
                left = tracker[s[right]] + 1
            tracker[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest