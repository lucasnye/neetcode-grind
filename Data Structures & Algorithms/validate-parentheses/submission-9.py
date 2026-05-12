class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in lookup:
                stack.append(char)
            elif stack and lookup[stack[-1]] == char:
                stack.pop()
            else:
                return False
            # if lookup[stack[-1]] == s[i]:
            #     stack.pop()
            # else:
            #     if s[i] in lookup:
            #         stack.append(s[i])
            #     else:
            #         return False
        
        return not stack