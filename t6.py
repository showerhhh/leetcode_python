class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lists = [[] for _ in range(numRows)]
        row = 0
        orient = 0  # 0表示down，1表示up
        for i in range(len(s)):
            lists[row].append(s[i])
            if orient == 0:
                row += 1
            else:
                row -= 1

            if row == numRows - 1:
                orient = 1
            elif row == 0:
                orient = 0
        result = ''
        for i in range(numRows):
            result += ''.join(lists[i])
        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'AB'
    numRows = 1
    print(solution.convert(s, numRows))
