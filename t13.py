class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        x = 0
        for i in range(len(s)):
            x += maps[s[i]]
            if (i - 1) >= 0 and s[i] in ['V', 'X'] and s[i - 1] == 'I':
                x -= 2 * maps[s[i - 1]]
            if (i - 1) >= 0 and s[i] in ['L', 'C'] and s[i - 1] == 'X':
                x -= 2 * maps[s[i - 1]]
            if (i - 1) >= 0 and s[i] in ['D', 'M'] and s[i - 1] == 'C':
                x -= 2 * maps[s[i - 1]]
        return x
