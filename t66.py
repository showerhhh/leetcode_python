class Solution:
    def plusOne(self, digits: list):
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += flag
            flag = int(digits[i] / 10)
            digits[i] = digits[i] % 10
        if flag == 1:
            digits.insert(0, 1)
        return digits
