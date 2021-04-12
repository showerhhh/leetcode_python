class Solution:
    def sortArrayByParityII(self, A: list) -> list:
        result = []
        i = 0
        j = 0
        while len(result) != len(A):
            # i指向下一个偶数，j指向下一个奇数
            while i < len(A) and A[i] % 2 != 0:
                i += 1
            while j < len(A) and A[j] % 2 == 0:
                j += 1
            result.append(A[i])
            result.append(A[j])
            i += 1
            j += 1
        return result
