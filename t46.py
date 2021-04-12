import copy


class Solution:
    def permute(self, nums):
        # 使用标记数组
        results = []
        one_result = []
        n = len(nums)
        flag = [False] * n

        def backtracking():
            if len(one_result) == n:
                results.append(copy.deepcopy(one_result))
                return
            for i in range(n):
                if not flag[i]:
                    one_result.append(nums[i])
                    flag[i] = True
                    backtracking()
                    flag[i] = False
                    one_result.pop()

        backtracking()
        return results

    def permute_2(self, nums):
        # 未使用标记数组
        results = []
        one_result = []
        n = len(nums)

        def backtracking(start):
            if len(one_result) == n:
                results.append(copy.deepcopy(one_result))
                return
            for i in range(start, n):
                one_result.append(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtracking(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
                one_result.pop()

        backtracking(0)
        return results


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute_2(nums))
