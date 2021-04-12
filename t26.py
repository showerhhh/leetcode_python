class Solution:
    def removeDuplicates(self, nums) -> int:
        # 双指针法
        nums.sort()  # 要先排序，使得相同元素相邻
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1
