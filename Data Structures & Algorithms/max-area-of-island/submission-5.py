from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        q = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(r, c):
            area = 0
            q.append((r, c))
            seen.add((r, c))

            while q:
                curr = q.popleft()
                area += 1
                
                for dr, dc in directions:
                    nr, nc = curr[0] + dr, curr[1] + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        seen.add((nr, nc))
                        
            return area
        
        max_area = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in seen and grid[r][c] == 1:
                    area = bfs(r, c)
                    max_area = max(area, max_area)
        
        return max_area