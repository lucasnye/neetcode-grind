class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        paths = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i] or (r, c) in paths:
                return False
            
            paths.add((r, c))
            result = dfs(r-1, c, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
            paths.remove((r, c))

            return result

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        
        return False