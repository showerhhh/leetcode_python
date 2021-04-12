class Solution:
    def findNumberOfLIS(self, nums: list) -> int:
        pass

    def LIS(self, nums: list) -> int:
        # 求最长递增子序列的长度
        dp = [1] * len(nums)  # dp[i]表示以i结尾的最长递增子序列长度。
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 2, 3, 1, 5]
    print(solution.LIS(nums))
