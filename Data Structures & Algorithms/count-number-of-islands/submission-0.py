from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque([])
        m = len(grid)
        n = len(grid[0])
        result = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # keep track of "1"s
        seen = set() # (r, c)

        # explore adjacent lands
        def dfs(r, c):
            if (r, c) in seen:
                return

            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if grid[r][c] == "0":
                return
            
            seen.add((r, c))
            
            for d in directions:
                dfs(r + d[0], c + d[1])

            return

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    result += 1
        
        return result