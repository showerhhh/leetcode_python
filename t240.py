class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        # 左下角开始
        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                j += 1
            else:
                i -= 1
        return False
