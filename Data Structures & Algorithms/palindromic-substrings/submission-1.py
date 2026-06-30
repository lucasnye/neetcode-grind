class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            
            return count
        
        for i in range(n):
            count += expand(i, i)
            count += expand(i, i + 1)
        
        return count