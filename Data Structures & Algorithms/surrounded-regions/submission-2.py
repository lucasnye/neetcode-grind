from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(board), len(board[0])
        edges = deque()
        seen = set()

        # for r in range(m):
        #     for c in range(n):
        #         if board[r][c] == "O" and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
        #             edges.append((r, c))
        #             seen.add((r, c))
        
        for r in range(m):
            for c in [0, n-1]:
                if board[r][c] == "O":
                    edges.append((r, c))
                    seen.add((r, c))
        
        for c in range(n):
            for r in [0, m-1]:
                if board[r][c] == "O":
                    edges.append((r, c))
                    seen.add((r, c))
        
        while edges:
            cur = edges.popleft()
            for dr, dc in directions:
                nr, nc = cur[0] + dr, cur[1] + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and board[nr][nc] == "O":
                    edges.append((nr, nc))
                    seen.add((nr, nc))

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r, c) not in seen:
                    board[r][c] = "X"