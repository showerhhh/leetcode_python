from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k: int):
        result = []
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        my_list = list(count.items())
        my_list.sort(key=lambda x: x[1], reverse=True)
        for item in my_list[:k]:
            result.append(item[0])
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solution.topKFrequent(nums, k))
