class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        y = 0
        while x != 0:
            y = y * 10 + x % 10
            x = int(x / 10)
        y = sign * y

        if not -pow(2, 31) <= y <= pow(2, 31) - 1:
            return 0
        else:
            return y


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(1534236469))
