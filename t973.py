class Solution:
    def kClosest(self, points: list, K: int) -> list:
        def func(point: list) -> int:
            return point[0] ** 2 + point[1] ** 2
        points.sort(key=func)
        return points[:K]
