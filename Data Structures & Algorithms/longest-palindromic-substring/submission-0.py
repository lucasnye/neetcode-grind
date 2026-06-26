class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                left -= 1
                right += 1
            
            return left + 1, right - 1
        
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            
            if len(s[l1:r1+1]) > len(res):
                res = s[l1:r1+1]

            
            l2, r2 = expand(i, i+1)

            if len(s[l2:r2+1]) > len(res):
                res = s[l2:r2+1]
            
        return res