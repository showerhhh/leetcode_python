class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        flag = [False] * len(rooms)

        def DFS(v):
            flag[v] = True
            for i in rooms[v]:
                if not flag[i]:
                    DFS(i)

        DFS(0)
        for i in range(len(flag)):
            if not flag[i]:
                return False
        return True

    def canVisitAllRooms_2(self, rooms) -> bool:
        flag = [False] * len(rooms)

        def BFS():
            queue = [0]
            while queue:
                w = queue.pop()
                flag[w] = True
                for i in rooms[w]:
                    if not flag[i]:
                        queue.append(i)

        BFS()
        for i in range(len(flag)):
            if not flag[i]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(solution.canVisitAllRooms(rooms))
