from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s == t:
            return True
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for alpha in s:
            count_s[alpha] += 1
        for alpha in t:
            count_t[alpha] += 1
        for key, value in count_s.items():
            if count_t[key] != value:
                return False
        for key, value in count_t.items():
            if count_s[key] != value:
                return False
        return True
