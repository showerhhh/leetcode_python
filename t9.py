class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        m = x
        y = 0
        while x != 0:
            y = y * 10 + x % 10
            x = int(x / 10)
        if y == m:
            return True
        else:
            return False
