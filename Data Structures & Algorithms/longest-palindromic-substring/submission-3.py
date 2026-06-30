class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left + 1, right

        res = ""

        for i in range(n):
            l, r = expand(i, i)
            x, y = expand(i, i + 1)

            if (r-l) < (y-x):
                l, r = x, y
            
            if len(s[l:r]) > len(res):
                res = s[l:r]

        return res