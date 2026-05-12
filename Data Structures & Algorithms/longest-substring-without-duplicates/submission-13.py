class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        tracker = {}
        longest = 0
        # if n <= 1:
        #     return n
        for right in range(n):
            if s[right] in tracker and tracker[s[right]] >= left:
                left = tracker[s[right]] + 1
            
            tracker[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest