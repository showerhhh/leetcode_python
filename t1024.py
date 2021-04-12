class Solution:
    def videoStitching(self, clips, T: int) -> int:
        def func(start: int) -> int:
            # 从列表中选取所有第一位小于等于start的项，从这些项中找出第二位最大的，并返回该值。
            end = -1
            for clip in clips:
                if clip[0] <= start:
                    if clip[1] > end:
                        end = clip[1]
            return end

        count = 0
        old = 0
        while old < T:
            new = func(old)
            if new == old:
                return -1
            else:
                count += 1
                old = new
        return count
