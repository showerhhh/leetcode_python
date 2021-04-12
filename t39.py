import copy


class Solution:
    def combinationSum(self, candidates, target: int):
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
            # 不选i位置元素
            backtracking(i + 1)
            # 选i位置元素
            result.append(candidates[i])
            sum += candidates[i]
            backtracking(i)
            sum -= candidates[i]
            result.pop()

        backtracking(0)
        return results

    def combinationSum_2(self, candidates, target: int):
        # candidates.sort()  # 非必须
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
                result.append(candidates[j])
                sum += candidates[j]
                backtracking(j)
                sum -= candidates[j]
                result.pop()

        backtracking(0)
        return results


if __name__ == '__main__':
    solution = Solution()
    candidates = [6, 3, 2, 7]
    target = 7
    print(solution.combinationSum_2(candidates, target))
