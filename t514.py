class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # 错误解法，原因在于ring中有重复字符，选择时即便不是当前最优，但却有利于下一步，有可能整体最优。

        n = len(ring)
        i = 0
        step = 0

        def find(target: chr) -> int:
            # 以i位置为起点，向左右两侧找target，要更新i，返回最小要找的步数
            nonlocal i
            # 向右查找
            right_step = 0
            right_i = i
            while ring[right_i] != target:
                right_step += 1
                right_i = (right_i + 1) % n
            # 向左查找
            left_step = 0
            left_i = i
            while ring[left_i] != target:
                left_step += 1
                left_i = (left_i - 1 + n) % n
            # 比较
            if right_step < left_step:
                i = right_i
                return right_step
            else:
                i = left_i
                return left_step

        for target in key:
            step += find(target) + 1

        return step


if __name__ == '__main__':
    solution = Solution()
    ring = "iotfo"
    key = "fioot"
    print(solution.findRotateSteps(ring, key))
