class Solution:
    def shortestPalindrome(self, s: str):
        def encode(s):
            temp = ['#']
            for i in s:
                temp.append(i)
                temp.append('#')
            return ''.join(temp)

        def decode(s, j):
            s_1 = s[:j]
            s_2 = s[j:]
            return ''.join(s_1.split('#')), ''.join(s_2.split('#'))

        en_s = encode(s)
        max_len = 0
        for center in range(len(en_s)):
            i = center - 1
            j = center + 1
            while i >= 0 and j < len(en_s) and en_s[i] == en_s[j]:
                i -= 1
                j += 1
            if i == -1 and j > max_len:
                max_len = j
        s_1, s_2 = decode(en_s, max_len)
        return s_2[::-1] + s

    def shortestPalindrome_2(self, s: str):
        def my_startswith(s, r):
            if s == '':
                print('s为空！')
            elif r == '':
                print('s为空！')
            else:
                for i in range(len(r)):
                    if s[i] != r[i]:
                        return False
                return True

        if s == '':
            return ''
        reverse = s[::-1]
        for i in range(len(reverse)):
            if my_startswith(s, reverse[i:]):
                return reverse[:i] + s

    def shortestPalindrome_3(self, s: str):
        if s == '':
            return ''
        reverse = s[::-1]
        for i in range(len(reverse)):
            if s.startswith(reverse[i:]):
                return reverse[:i] + s


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPalindrome_3('bsvsd'))
