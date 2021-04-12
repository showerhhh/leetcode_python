class Solution:
    def canPartition(self, nums) -> bool:
        # 超时了
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum / 2
        count = 0
        flag = False

        def backtracking(start):
            nonlocal count, flag
            if count == target:
                flag = True
                return
            if count > target or start == len(nums):
                return
            for i in range(start, len(nums)):
                count += nums[i]
                backtracking(i + 1)
                count -= nums[i]

        backtracking(0)
        return flag

    def canPartition_v2(self, nums) -> bool:
        n = len(nums)

        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum // 2
        if max(nums) > target:
            return False

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        for j in range(target + 1):
            dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(1, target + 1):
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]
