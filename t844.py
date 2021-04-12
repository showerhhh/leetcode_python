class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def transform(string: str) -> str:
            temp = []
            for s in string:
                if s == "#":
                    if temp:
                        temp.pop()
                else:
                    temp.append(s)
            return ''.join(temp)

        return transform(S) == transform(T)


if __name__ == '__main__':
    solution = Solution()
    S = "ab#c"
    T = "ad#c"
    print(solution.backspaceCompare(S, T))
