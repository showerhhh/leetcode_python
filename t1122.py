class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        digits_not_in_arr2 = []
        i = 0
        while i < len(arr1):
            if arr1[i] not in arr2:
                digits_not_in_arr2.append(arr1[i])
                arr1.pop(i)
            else:
                i += 1

        def func(x):
            return arr2.index(x)

        arr1.sort(key=func)
        arr1 += sorted(digits_not_in_arr2)
        return arr1
