class Solution:
    def PredictTheWinner(self, nums) -> bool:
        def score(start, end, player):
            # player == 1 表示玩家1，player == -1 表示玩家2
            # 返回当前玩家在当前状态下可以得到的最优分数（用玩家1-玩家2的差值表示）。
            if start == end:
                return nums[start] * player
            left_score = nums[start] * player + score(start + 1, end, -player)
            right_score = nums[end] * player + score(start, end - 1, -player)
            if player == 1:
                return max(left_score, right_score)
            else:
                return min(left_score, right_score)

        finally_score = score(0, len(nums) - 1, 1)
        return finally_score >= 0

    def PredictTheWinner_2(self, nums) -> bool:
        def score(start, end):
            # 返回当前玩家在当前状态下可以得到的最优分数（用当前玩家-另一玩家的差值表示）。
            if start == end:
                return nums[start]
            left_score = nums[start] - score(start + 1, end)
            right_score = nums[end] - score(start, end - 1)
            return max(left_score, right_score)

        finally_score = score(0, len(nums) - 1)
        return finally_score >= 0

    def PredictTheWinner_3(self, nums) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]  # 用列表推导建立二维数组
        for i in range(length):
            dp[i][i] = nums[i]
        for k in range(1, length):
            # k表示每一斜行
            for v in range(length - k):
                # v表示斜行长度
                # i = f(k) + v
                # j = g(k) + v
                i = 0 + v
                j = k + v
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5, 233, 7]
    print(solution.PredictTheWinner(nums))
