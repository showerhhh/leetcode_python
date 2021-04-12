class Solution:
    def minimumOperations(self, leaves: str) -> int:
        r, ry, ryr = 1 if leaves[0] == 'y' else 0, float('inf'), float('inf')
        for i in range(1, len(leaves)):
            if leaves[i] == 'r':
                r, ry, ryr = r, min(r, ry) + 1, min(ry, ryr)
            else:
                r, ry, ryr = r + 1, min(r, ry), min(ry, ryr) + 1
        return ryr
