class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        def check(i):
            temp = strs[0][i]
            for k in range(1, len(strs)):
                if strs[k][i] != temp:
                    return False
            return True

        min_len = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])

        i = 0
        while i < min_len and check(i):
            i += 1

        return strs[0][0:i]


if __name__ == '__main__':
    solution = Solution()
    strs = ["","dog","racecar","car",]
    print(solution.longestCommonPrefix(strs))
