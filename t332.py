import collections


class Solution:
    def findItinerary(self, tickets):
        # 按depart将arrive组成列表，字典中键值对为depart: arrive列表
        # 其实建立了图的邻接表
        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)

        def find(start_place):
            """
            按start_place找到target_place
            将target_place从vec[start_place]中删除
            """
            target_place = 'ZZZ'
            for i in vec[start_place]:
                if i < target_place:
                    target_place = i
            vec[start_place].remove(target_place)
            return target_place

        def DFS(current_place):
            while vec[current_place]:
                target_place = find(current_place)
                DFS(target_place)
            travel.insert(0, current_place)

        travel = []
        DFS('JFK')
        return travel


if __name__ == '__main__':
    solution = Solution()
    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    print(solution.findItinerary(tickets))
    # print('LGA' < 'LGB')
