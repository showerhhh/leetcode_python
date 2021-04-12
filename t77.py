import copy


class Solution:
    def combine(self, n: int, k: int):
        nums = range(1, n + 1)
        results = []
        result = []

        def backtracking(start):
            if len(result) == k:
                results.append(copy.deepcopy(result))
                return
            for i in range(start, n):
                result.append(nums[i])
                backtracking(i + 1)
                result.pop()

        backtracking(0)
        return results


if __name__ == '__main__':
    solution = Solution()
    n = 4
    k = 2
    print(solution.combine(n, k))
