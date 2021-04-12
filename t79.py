class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            for offset_i, offset_j in positions:
                new_i = i + offset_i
                new_j = j + offset_j
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited and check(new_i, new_j, k + 1):
                    return True
            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False
