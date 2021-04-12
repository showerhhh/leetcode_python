class Solution:
    def countAndSay(self, n: int) -> str:
        def generate(old_str: str) -> str:
            new_str = ''
            i = 0
            j = 1
            count = 1
            while j < len(old_str):
                if old_str[i] == old_str[j]:
                    count += 1
                else:
                    new_str += str(count) + str(old_str[i])
                    i = j
                    count = 1
                j += 1
            new_str += str(count) + str(old_str[i])
            return new_str

        now_str = '1'
        for i in range(n - 1):
            now_str = generate(now_str)
        return now_str


if __name__ == '__main__':
    solution = Solution()
    n = 5
    print(solution.countAndSay(n))
