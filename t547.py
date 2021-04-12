class Solution:
    def findCircleNum(self, isConnected: list) -> int:
        n = len(isConnected)
        visited = set()
        count = 0

        def dfs(i: int):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.update([j])
                    dfs(j)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count
