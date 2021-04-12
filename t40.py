import copy


class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()  # 排序必不可少，排序后才能用下面的方法去重
        results = []
        result = []
        sum = 0

        def backtracking(i):
            nonlocal sum
            if sum == target:
                results.append(copy.deepcopy(result))
                return
            if sum > target or i == len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    # 在同一层循环中，若发现一样的数字就跳过，从而去重
                    continue
                result.append(candidates[j])
                sum += candidates[j]
                backtracking(j + 1)
                sum -= candidates[j]
                result.pop()

        backtracking(0)
        return results


if __name__ == '__main__':
    solution = Solution()
    # candidates = [10, 1, 2, 7, 6, 1, 5]
    # target = 8
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(solution.combinationSum2(candidates, target))
