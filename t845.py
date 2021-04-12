class Solution:
    def longestMountain(self, A: list) -> int:
        def get_montain_length(i: int) -> int:
            # 获取i为中心的最长山脉长度，没有则返回0
            right = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[j - 1]:
                    right += 1
            left = 0
            for j in range(i - 1, -1, -1):
                if A[j] < A[j + 1]:
                    left += 1
            if left == 0 or right == 0:
                return 0
            else:
                return left + right + 1

        max_montain_length = 0
        for i in range(1, len(A) - 1):
            montain_length = get_montain_length(i)
            if montain_length > max_montain_length:
                max_montain_length = montain_length
        return max_montain_length

    def longestMountain_v2(self, A: list) -> int:
        left = [0] * len(A)
        for i in range(len(A)):
            if i == 0:
                left[i] = 0
            else:
                if A[i - 1] < A[i]:
                    left[i] = left[i - 1] + 1
                else:
                    left[i] = 0

        right = [0] * len(A)
        for i in range(len(A) - 1, -1, -1):
            if i == len(A) - 1:
                right[i] = 0
            else:
                if A[i] > A[i + 1]:
                    right[i] = right[i + 1] + 1
                else:
                    right[i] = 0

        max_montain_length = 0
        for i in range(1, len(A) - 1):
            montain_length = 0
            if left[i] != 0 and right[i] != 0:
                montain_length = left[i] + right[i] + 1
            if montain_length > max_montain_length:
                max_montain_length = montain_length
        return max_montain_length


if __name__ == '__main__':
    solution = Solution()
    A = [2, 1, 4, 7, 3, 2, 5]
    print(solution.longestMountain_v2(A))
