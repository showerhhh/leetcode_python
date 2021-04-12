import copy


class Solution:
    def combinationSum3(self, k: int, n: int):
        nums = range(1, 10)
        results = []
        result = []
        sum = 0

        def backtracking(start):
            nonlocal sum
            if sum == n and len(result) == k:
                results.append(copy.deepcopy(result))
                return
            if sum > n or len(result) > k:
                return
            for i in range(start, 9):
                result.append(nums[i])
                sum += nums[i]
                backtracking(i + 1)
                sum -= nums[i]
                result.pop()

        backtracking(0)
        return results


if __name__ == '__main__':
    solution = Solution()
    # k = 3
    # n = 7
    k = 3
    n = 9
    print(solution.combinationSum3(k, n))
