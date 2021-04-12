class Solution:
    def islandPerimeter(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])

        def check(pos_i: int, pos_j: int) -> int:
            count = 0
            offset_i = [0, 0, -1, 1]  # 左右上下
            offset_j = [-1, 1, 0, 0]  # 左右上下
            for k in range(4):
                new_i = pos_i + offset_i[k]
                new_j = pos_j + offset_j[k]
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                    continue
                else:
                    count += 1
            return count

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += check(i, j)
        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(solution.islandPerimeter(grid))
