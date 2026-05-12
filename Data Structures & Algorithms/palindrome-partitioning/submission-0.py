class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)
        # Define a helper function to check palindromic validity
        def isValid(s):
            return s == s[::-1]
        
        def backtrack(i, curr):
            if i == len(s):
                result.append(curr[:])
                return
            
            for j in range(i, n):
                temp = s[i:j+1]
                if isValid(temp):
                    curr.append(temp)
                    backtrack(j+1, curr)
                    curr.pop()

        backtrack(0, [])
        return result