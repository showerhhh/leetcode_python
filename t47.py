import copy


class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        results = []
        one_result = []
        n = len(nums)
        flag = [False] * n

        def backtracking():
            if len(one_result) == n:
                results.append(copy.deepcopy(one_result))
                return
            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1] and not flag[i - 1]:
                    continue
                if not flag[i]:
                    one_result.append(nums[i])
                    flag[i] = True
                    backtracking()
                    flag[i] = False
                    one_result.pop()

        backtracking()
        return results


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    print(solution.permuteUnique(nums))
