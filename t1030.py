class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> list:
        point_pos = []
        for i in range(R):
            for j in range(C):
                point_pos.append([i, j])

        def func(x):
            return abs(x[0] - r0) + abs(x[1] - c0)

        return sorted(point_pos, key=func)
