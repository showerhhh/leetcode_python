class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        def func(k: int) -> int:
            count = 0
            for i in range(len(nums)):
                if i != k and nums[i] < nums[k]:
                    count += 1
            return count

        result = []
        for k in range(len(nums)):
            result.append(func(k))
        return result
