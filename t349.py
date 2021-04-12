from collections import defaultdict


class Solution:
    def intersection(self, nums1, nums2):
        result = []
        dict_num1 = defaultdict(int)
        dict_num2 = defaultdict(int)
        for num in nums1:
            dict_num1[num] += 1
        for num in nums2:
            dict_num2[num] += 1
        for key in dict_num1.keys():
            if dict_num2[key] != 0:
                result.append(key)
        return result
