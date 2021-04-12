class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        if not s:
            return 0
        unique = set(s[start])
        longest = 1
        while start < len(s):
            if end < start:
                end = start
                unique.update(s[start])
            while end + 1 < len(s) and s[end + 1] not in unique:
                unique.update(s[end + 1])
                end += 1
            longest = max(longest, end - start + 1)
            if end + 1 == len(s):
                break  # 加速
            unique.remove(s[start])
            start += 1
        return longest


if __name__ == '__main__':
    solution = Solution()
    s = 'abcabcbb'
    print(solution.lengthOfLongestSubstring(s))
