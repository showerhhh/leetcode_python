class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划状态转移方程：f(n) = f(n-2) + f(n-1)，f(0) = 1，f(1) = 1
        x = 1
        y = 1
        for i in range(2, n + 1):
            z = x + y
            x = y
            y = z
        return y
