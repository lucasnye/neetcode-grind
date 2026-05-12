from collections import deque
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lookup = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b : int(a / b)
        }
        result = 0
        stack = deque()
        for char in tokens:
            if char in lookup:
                operand1, operand2 = stack.pop(), stack.pop()
                result = lookup[char](operand2, operand1)
                stack.append(result)
            else:
                stack.append(int(char))
        return stack[0]