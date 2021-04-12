class Solution:
    def validMountainArray(self, A: list) -> bool:
        i = 1
        while i < len(A) and A[i] > A[i - 1]:
            i += 1
        if i == len(A):
            return False
        else:
            i -= 1

        j = len(A) - 2
        while j >= 0 and A[j] > A[j + 1]:
            j -= 1
        if j == -1:
            return False
        else:
            j += 1

        return i == j
