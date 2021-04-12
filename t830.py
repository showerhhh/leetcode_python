class Solution:
    def largeGroupPositions(self, s: str) -> list:
        result = list()

        start = 0
        end = 1

        while end < len(s):
            if s[end] != s[end - 1]:
                if end - start >= 3:
                    result.append([start, end - 1])
                start = end
            end += 1

        if end - start >= 3:
            result.append([start, end - 1])

        return result
