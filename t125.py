class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(s: str) -> bool:
            n = len(s)
            for i in range(n // 2):
                if s[i] != s[n - 1 - i]:
                    return False
            return True

        new_s = ''
        for alpha in s:
            if alpha.isalnum():
                new_s += alpha.lower()
        return check(new_s)
