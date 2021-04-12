class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in S:
            if J.find(i) != -1:
                count += 1
        return count
