class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[int(i / 3)][int(j / 3)][digit] = True

        def backtracking(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[int(i / 3)][int(j / 3)][digit] == False:
                    line[i][digit] = column[j][digit] = block[int(i / 3)][int(j / 3)][digit] = True
                    board[i][j] = str(digit + 1)
                    backtracking(pos + 1)
                    line[i][digit] = column[j][digit] = block[int(i / 3)][int(j / 3)][digit] = False
                if valid:
                    return

        backtracking(0)
