class Solution:
    def sortedSquares(self, A):
        for i in range(len(A)):
            A[i] = int(pow(A[i], 2))
        return sorted(A)
