class Solution:
    def searchInsert(self, nums, target: int) -> int:
        """
        二分法查找，若目标不存在，则返回它将会被按顺序插入的位置。
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    print(solution.searchInsert(nums, target))
