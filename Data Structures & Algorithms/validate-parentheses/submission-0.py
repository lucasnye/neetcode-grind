class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_to_opening = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in closing_to_opening:
                # It's a closing bracket
                if not stack or stack[-1] != closing_to_opening[char]:
                    return False
                stack.pop()
            else:
                # It's an opening bracket
                stack.append(char)
        
        # Valid only if stack is empty (all brackets matched)
        return len(stack) == 0