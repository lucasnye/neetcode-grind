class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = []
        n = len(s)

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                palindromes.append(s[left:right+1])
                left -= 1
                right += 1
        
        for i in range(n):
            expand(i, i)
            expand(i, i+1)
        
        return len(palindromes)