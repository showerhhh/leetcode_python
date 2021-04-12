import copy


class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(row, column, n):
            # 不用检查行

            # 检查列
            for i in range(n):
                if queen[i][column] == 'Q':
                    return False

            # 检查主对角线（左上），主对角线（右下）还没有，不用检查
            for i, j in zip(range(row - 1, -1, -1), range(column - 1, -1, -1)):
                if queen[i][j] == 'Q':
                    return False

            # 检查副对角线（右上），副对角线（左下）还没有，不用检查
            for i, j in zip(range(row - 1, -1, -1), range(column + 1, n)):
                if queen[i][j] == 'Q':
                    return False

            return True

        def generate(queen):
            temp = []
            copy_queen = copy.deepcopy(queen)  # 保证深复制
            for i in range(len(copy_queen)):
                temp.append(''.join(copy_queen[i]))
            return temp

        def print_queen(queen):
            print('count = ' + str(count))
            for i in range(n):
                for j in range(n):
                    if queen[i][j] == 'Q':
                        print('.' * j + 'Q' + '.' * (n - 1 - j))
            print("\n")

        # result = []
        queen = [['.'] * n for _ in range(n)]
        count = 0

        def func(row):
            nonlocal count
            if row == n:
                count += 1
                # print_queen(queen)
                # result.append(generate(queen))
                return
            for column in range(n):
                if check(row, column, n):
                    queen[row][column] = 'Q'
                    func(row + 1)
                    queen[row][column] = '.'

        func(0)
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(8))
