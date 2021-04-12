class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s):
            n = len(s)
            for i in range(int(n / 2)):
                temp = s[i]
                s[i] = s[n - i - 1]
                s[n - i - 1] = temp

        words = s.split(' ')
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return ' '.join(words)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("Let's take LeetCode contest"))
