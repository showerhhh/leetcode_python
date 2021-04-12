class Solution:
    def sumOfDistancesInTree(self, N: int, edges):
        # 建立子节点与父节点的对应关系
        child_parent = {}
        for parent, child in edges:
            child_parent[child] = parent

        def dist(i, j):
            n = j
            m = child_parent[n]
            count = 1
            while m != i:
                n = m
                m = child_parent[n]
                count += 1
            return count

        temp = 0
        for j in range(N):
            if 0 != j:
                temp += dist(0, j)
        return temp
        # answer = []
        # for i in range(N):
        #     temp = 0
        #     for j in range(N):
        #         if i != j:
        #             temp += dist(i, j)
        #     answer.append(temp)
        # return answer


if __name__ == '__main__':
    solution = Solution()
    N = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(solution.sumOfDistancesInTree(N, edges))
