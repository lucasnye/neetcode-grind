from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        seen = set()
        max_area = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            seen.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            area = 0
            
            while q:
                curr = q.popleft()
                area += 1

                for dr, dc in directions:
                    nr = curr[0] + dr
                    nc = curr[1] + dc

                    if 0 <= nr < rows and 0 <= nc < columns:
                        if grid[nr][nc] == 1 and (nr, nc) not in seen:
                            q.append((nr, nc))
                            seen.add((nr, nc))
                            
            return area

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area