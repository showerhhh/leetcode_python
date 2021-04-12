class Solution:
    def fourSum(self, nums, target: int):
        results = []
        nums.sort()  # 排序既是为了去重，也是为了使用双指针
        n = len(nums)
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                # 在同一层循环中，若发现一样的数字就跳过，从而去重
                continue
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    # 在同一层循环中，若发现一样的数字就跳过，从而去重
                    continue
                # 将后两层循环变成双指针
                third = second + 1
                fourth = n - 1
                while third < fourth:
                    if nums[first] + nums[second] + nums[third] + nums[fourth] == target:
                        results.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third += 1
                        fourth -= 1
                        while third < fourth and nums[third] == nums[third - 1]:
                            third += 1
                        while third < fourth and nums[fourth] == nums[fourth + 1]:
                            fourth -= 1
                    elif nums[first] + nums[second] + nums[third] + nums[fourth] < target:
                        third += 1
                    else:
                        fourth -= 1
        return results


if __name__ == '__main__':
    solution = Solution()
    nums = [-500, -481, -480, -469, -437, -423, -408, -403, -397, -381, -379, -377, -353, -347, -337, -327, -313, -307,
            -299, -278, -265, -258, -235, -227, -225, -193, -192, -177, -176, -173, -170, -164, -162, -157, -147, -118,
            -115, -83, -64, -46, -36, -35, -11, 0, 0, 33, 40, 51, 54, 74, 93, 101, 104, 105, 112, 112, 116, 129, 133,
            146, 152, 157, 158, 166, 177, 183, 186, 220, 263, 273, 320, 328, 332, 356, 357, 363, 372, 397, 399, 420,
            422, 429, 433, 451, 464, 484, 485, 498, 499]
    target = 2139
    print(solution.fourSum(nums, target))
