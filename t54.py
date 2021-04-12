class Solution:
    def spiralOrder(self, matrix) -> list:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        flag = [[False] * n for _ in range(m)]
        i = 0
        j = 0
        orient = (0, 1)  # (0, 1)=left, (1, 0)=down, (0, -1)=right, (-1, 0)=up
        while len(result) < m * n:
            result.append(matrix[i][j])
            flag[i][j] = True
            next_i, next_j = i + orient[0], j + orient[1]
            if 0 <= next_i < m and 0 <= next_j < n and not flag[next_i][next_j]:
                i, j = next_i, next_j
            else:
                if orient == (0, 1):
                    orient = (1, 0)
                elif orient == (1, 0):
                    orient = (0, -1)
                elif orient == (0, -1):
                    orient = (-1, 0)
                elif orient == (-1, 0):
                    orient = (0, 1)
                i, j = i + orient[0], j + orient[1]
        return result
