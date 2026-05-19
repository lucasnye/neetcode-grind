from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        seen = set()
        
        def bfs(r, c):
            q = deque()
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            q.append((r, c))

            while q:
                curr = q.popleft()
                seen.add(curr)
                
                for dr, dc in directions:
                    nr, nc = curr[0] + dr, curr[1] + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == "1" and (nr, nc) not in seen:
                            q.append((nr, nc))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1
        
        return islands