class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(i, pars):
            if len(pars) == 2*n:
                if isValid(pars):
                    result.append(pars)
                return
            if i < n:
                backtrack(i, pars + '(')
            backtrack(i, pars + ')')

        def isValid(parantheses):
            stack = []
            for char in parantheses:
                if char == '(':
                    stack.append('(')
                else:
                    if not stack:
                        return False
                    stack.pop()
            return True if not stack else False
        
        backtrack(0, "")
        return result