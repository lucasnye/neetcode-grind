import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        n = len(s)
        p1 = 0
        p2 = n - 1
        for i in range(n // 2):
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True