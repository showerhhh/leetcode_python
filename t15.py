class Solution:
    def threeSum(self, nums):
        # 仅实现了去重，未降低时间复杂度
        # 目标和为0
        results = []
        nums.sort()  # 排序为了去重
        n = len(nums)
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                # 在同一层循环中，若发现一样的数字就跳过，从而去重
                continue
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    # 在同一层循环中，若发现一样的数字就跳过，从而去重
                    continue
                for third in range(second + 1, n):
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        # 在同一层循环中，若发现一样的数字就跳过，从而去重
                        continue
                    if nums[first] + nums[second] + nums[third] == 0:
                        results.append([nums[first], nums[second], nums[third]])
        return results

    def threeSum_v2(self, nums):
        # 实现了去重，降低了时间复杂度
        # 目标和为0
        results = []
        nums.sort()  # 排序既是为了去重，也是为了使用双指针
        n = len(nums)
        for first in range(n):
            # if nums[first] > 0:
            #     # 当第一个数大于目标值时，直接退出循环，降低时间消耗
            #     break
            if first > 0 and nums[first] == nums[first - 1]:
                # 在同一层循环中，若发现一样的数字就跳过，从而去重
                continue
            # 将后两层循环变成双指针
            second = first + 1
            third = n - 1
            while second < third:
                if nums[first] + nums[second] + nums[third] == 0:
                    results.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
                elif nums[first] + nums[second] + nums[third] < 0:
                    second += 1
                else:
                    third -= 1
        return results


if __name__ == '__main__':
    solution = Solution()
    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    print(solution.threeSum_v2(nums))
