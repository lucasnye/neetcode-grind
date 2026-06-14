from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(heights), len(heights[0])
        result = []
        pacific = deque()
        pac_seen = set()
        atlantic = deque()
        atl_seen = set()
        
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    pacific.append((r, c))
                    pac_seen.add((r, c))
                if r == m - 1 or c == n - 1:
                    atlantic.append((r, c))
                    atl_seen.add((r, c))
        
        def bfs(q, seen):
            while q:
                cur = q.popleft()
                seen.add(cur)
                for dr, dc in directions:
                    nr, nc = cur[0] + dr, cur[1] + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if (nr, nc) not in seen:
                            if heights[nr][nc] >= heights[cur[0]][cur[1]]:
                                q.append((nr, nc))
            
        bfs(pacific, pac_seen)
        bfs(atlantic, atl_seen)

        return [[r, c] for r in range(m) for c in range(n) if (r, c) in pac_seen and (r, c) in atl_seen]
                    