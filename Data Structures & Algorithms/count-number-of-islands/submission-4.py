from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        seen = set()
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = 0

        def bfs(r, c):
            q.append((r, c))
            
            while q:
                curr = q.popleft()
                seen.add(curr)

                for dr, dc in directions:
                    nr, nc = dr + curr[0], dc + curr[1]
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    result += 1
        
        return result