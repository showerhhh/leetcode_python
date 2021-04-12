class Solution:
    def sortString(self, s: str) -> str:
        result_list = []
        s_list = list(s)

        def pick_small(previous) -> chr:
            # 从s_list中选出最小字符，从s_list中删除，并返回该字符
            pass

        while s_list:
            letter = pick_small()
            result_list.append(letter)
