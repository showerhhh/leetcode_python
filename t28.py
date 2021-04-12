class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def my_startswith(haystack: str, needle: str, start: int):
            if len(needle) + start > len(haystack):
                return False
            for i in range(len(needle)):
                if haystack[start + i] != needle[i]:
                    return False
            return True

        if needle == '':
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if my_startswith(haystack, needle, i):
                return i
        return -1
