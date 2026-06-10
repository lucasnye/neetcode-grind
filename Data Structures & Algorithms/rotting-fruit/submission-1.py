from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        q = deque()
        bananas = set()
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    bananas.add((r, c))
        
        if not bananas:
            return minute
        
        while q:
            cur_len = len(q)
            minute += 1
            for i in range(cur_len):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        bananas.remove((nr, nc))
            if not bananas:
                return minute
        
        return -1