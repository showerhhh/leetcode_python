class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        digit_list = [int(digit) for digit in num]

        i = 0
        while i < len(digit_list) - 1 and k > 0:
            if digit_list[i] <= digit_list[i + 1]:
                i += 1
            else:
                digit_list.pop(i)
                k -= 1
                # 删掉后i退一位（当i不是第一位时）
                if i > 0:
                    i -= 1
        # 如果k不是0，则会删掉最后k个
        while k > 0:
            digit_list.pop()
            k -= 1
        # 删掉digit_list中的前导0
        while digit_list and digit_list[0] == 0:
            digit_list.pop(0)
        # 如果删空了，加个0进去
        if not digit_list:
            digit_list.append(0)

        digit_str = ''.join([str(digit) for digit in digit_list])
        return digit_str


if __name__ == '__main__':
    solution = Solution()
    num = "1432219"
    k = 3
    print(solution.removeKdigits(num, k))
