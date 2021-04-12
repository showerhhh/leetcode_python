from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        dict_1 = defaultdict(int)
        for digit in arr:
            dict_1[digit] += 1

        dict_2 = defaultdict(int)
        for key, value in dict_1.items():
            dict_2[value] += 1

        for value in dict_2.values():
            if value > 1:
                return False
        return True
