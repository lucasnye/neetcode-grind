class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        if len(s) < 2:
            return False

        for i in range(len(s)):
            if not stack:
                if s[i] not in lookup:
                    return False
                stack.append(s[i])
                continue
            if lookup[stack[-1]] == s[i]:
                stack.pop()
            else:
                if s[i] in lookup:
                    stack.append(s[i])
                else:
                    return False
        
        return False if stack else True