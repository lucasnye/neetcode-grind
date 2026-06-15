class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(board), len(board[0])
        q = deque()

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                    q.append((r, c))
                    board[r][c] = "S"  # safe

        while q:
            cur = q.popleft()
            for dr, dc in directions:
                nr, nc = cur[0] + dr, cur[1] + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    q.append((nr, nc))

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"