class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start: int, n: int):
            for i in range(n // 2):
                nums[i + start], nums[n - 1 - i + start] = nums[n - 1 - i + start], nums[i + start]

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i < 0:
            reverse(0, len(nums))
            return

        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        # 反转nums[i+1, n-1]
        reverse(i + 1, len(nums) - i - 1)
        return
