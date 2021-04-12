class Solution:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
        # index = 0
        # result = dp[0]
        # for i in range(1, len(dp)):
        #     if dp[i] > result:
        #         index = i
        #         result = dp[i]
        # return index, result


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))
