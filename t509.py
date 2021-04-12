class Solution:
    def fib(self, n: int) -> int:
        fn_2 = 0
        fn_1 = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(1, n):
                fn = fn_2 + fn_1
                fn_2 = fn_1
                fn_1 = fn
            return fn


if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(4))
