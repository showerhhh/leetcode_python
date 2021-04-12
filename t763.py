class Solution:
    def partitionLabels(self, S: str) -> list:
        last = [-1] * 26
        for i in range(len(S)):
            last[ord(S[i]) - ord('a')] = i
        start = 0
        end = 0
        results = []
        for i in range(len(S)):
            if last[ord(S[i]) - ord('a')] > end:
                end = last[ord(S[i]) - ord('a')]
            if i == end:
                results.append(end - start + 1)
                start = end + 1
        return results
