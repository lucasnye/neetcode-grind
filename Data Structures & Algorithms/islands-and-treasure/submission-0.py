from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 0

        while q:
            dist += 1
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = dist
                        q.append((nr, nc))