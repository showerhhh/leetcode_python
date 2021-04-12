class Solution:
    def sortByBits(self, arr: list) -> list:
        arr.sort()

        def func(digit: int) -> int:
            # 返回digit的二进制中1的个数
            count = 0
            while digit != 0:
                count += digit % 2
                digit = digit // 2
            return count

        arr.sort(key=func)
        return arr
