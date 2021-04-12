class Solution:
    def commonChars(self, A):
        def alpha_in_str(alpha, string):
            count_in_str = 0
            for s in string:
                if s == alpha:
                    count_in_str += 1
            return count_in_str

        def alpha_in_list(alpha, A):
            count_in_list = alpha_in_str(alpha, A[0])
            for i in range(1, len(A)):
                temp = alpha_in_str(alpha, A[i])
                if temp < count_in_list:
                    count_in_list = temp
            return count_in_list

        result = []
        for i in range(26):  # 26个英文字母
            alpha = chr(97 + i)  # a的ASCII码为97
            count_in_list = alpha_in_list(alpha, A)
            while count_in_list != 0:
                result.append(alpha)
                count_in_list -= 1
        return result
