class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        my_list = [0, 0, 0]
        for digit in nums:
            my_list[digit] += 1
        k = 0  # k指向第一个不为0的数
        while k < 3 and my_list[k] == 0:
            k += 1
        for i in range(len(nums)):
            nums[i] = k
            my_list[k] -= 1
            while k < 3 and my_list[k] == 0:
                k += 1
