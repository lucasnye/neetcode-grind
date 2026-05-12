from collections import Counter
class Solution:
    """
    Rules
    1. Each row has to have 1-9, without duplicates
    2. Each column has to have 1-9, without duplicates
    3. Each square has to have 1-9, without duplicates
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                box = (r // 3) * 3 + (c // 3)
                if num == ".":
                    continue
                if num in row[c] or num in column[r] or num in boxes[box]:
                    return False
                else:
                    row[c].add(num)
                    column[r].add(num)
                    boxes[box].add(num)
        return True
        # seen = {}
        # for i in range(1, 10):
        #     seen[i] = 1
        # for row in range(9):
        #     for column in range(9):
        #         cell = board[row][column]
        #         if cell not in seen:
        #             return False
        #         elif seen[cell] == 0:
        #             return False
        #         elif 