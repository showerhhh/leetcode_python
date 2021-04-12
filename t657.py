import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # 计数
        count = collections.defaultdict(int)
        for i in moves:
            count[i] += 1

        if count['R'] == count['L'] and count['U'] == count['D']:
            return True
        else:
            return False
