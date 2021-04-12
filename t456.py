class Solution:
    def find132pattern(self, nums: list) -> bool:
        self.nums = nums
        self.dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j >= i + 2:
                    self.dp[i][j] = -1
        return bool(self.f(0, len(nums) - 1))

    def f(self, i, j) -> int:
        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if self.f(i + 1, j) or self.f(i, j - 1) or self.f(i + 1, j - 1):
            self.dp[i][j] = 1
            return 1
        else:
            if self.nums[i] < self.nums[j] < max(self.nums[i + 1:j]):
                self.dp[i][j] = 1
                return 1
            else:
                self.dp[i][j] = 0
                return 0


class Solution_2:
    def find132pattern(self, nums: list) -> bool:
        self.stack = [nums[-1]]
        max_k = float('-inf')
        for i in range(len(nums) - 2, -1, -1):  # [)区间，步长为负数时，前大于后
            if nums[i] < max_k:
                return True
            while self.stack and nums[i] > self.stack[-1]:
                max_k = self.stack.pop(-1)
            self.stack.append(nums[i])
        return False

    def push(self, x: int) -> set:
        tmp = set()
        while self.stack and x >= self.stack[-1]:
            top = self.stack.pop(-1)
            tmp.update([top])
        self.stack.insert(-1, x)
        return tmp


if __name__ == '__main__':
    solution = Solution_2()
    nums = [3, 5, 0, 3, 4]
    print(solution.find132pattern(nums))
