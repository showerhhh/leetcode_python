class Solution:
    def getRow(self, rowIndex: int) -> list:
        pre_row = None
        for i in range(rowIndex + 1):
            row = [0 for _ in range(i + 1)]
            row[0] = 1
            row[-1] = 1

            for j in range(1, len(row) - 1):
                row[j] = pre_row[j] + pre_row[j - 1]

            pre_row = row
        return pre_row
