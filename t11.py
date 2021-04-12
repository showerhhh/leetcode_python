class Solution:
    def maxArea(self, height: list) -> int:
        max_cheng = 0
        i = 0
        j = len(height) - 1
        while i < j:
            cheng = min(height[i], height[j]) * (j - i)
            max_cheng = max(max_cheng, cheng)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_cheng
