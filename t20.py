class Solution:
    def isValid(self, s: str) -> bool:
        maps = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            if s[i] in [')', '}', ']']:
                if stack:
                    temp = stack.pop()
                else:
                    return False
                if maps[s[i]] != temp:
                    return False

        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    s = "()"
    print(solution.isValid(s))
