import copy


class Solution:
    def subsets(self, nums):
        results = []
        result = []

        def backtracking(start, k):
            if len(result) == k:
                results.append(copy.deepcopy(result))
                return
            for i in range(start, len(nums)):
                result.append(nums[i])
                backtracking(i + 1, k)
                result.pop()

        for k in range(len(nums) + 1):
            backtracking(0, k)
        return results


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))
