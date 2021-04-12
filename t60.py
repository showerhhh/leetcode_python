class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = range(1, n + 1)
        flag = [False] * n
        result = []
        count = 0
        result_str = None

        def factorial(t):
            sum = 1
            for i in range(1, t + 1):
                sum *= i
            return sum

        def backtracking(start):
            nonlocal count, result_str
            if count + factorial(n - start) < k:
                # 剪枝（count加上当前状态所有分支后依然没达到k），则跳过当前状态
                count += factorial(n - start)
                return
            if count >= k:
                # 剪枝（count等于k后，不再向下尝试，不断返回）
                return
            if len(result) == n:
                count += 1
                if count == k:
                    result_str = ''.join(str(i) for i in result)
                return 
            for i in range(n):
                if not flag[i]:
                    result.append(nums[i])
                    flag[i] = True
                    backtracking(start + 1)
                    flag[i] = False
                    result.pop()

        backtracking(0)
        return result_str


if __name__ == '__main__':
    solution = Solution()
    n = 3
    k = 3
    print(solution.getPermutation(n, k))

