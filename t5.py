class Solution:
    def f(self, s: str, i: int, j: int) -> int:
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        if i > j:
            self.dp[i][j] = 0
            return 0
        elif i == j:
            self.dp[i][j] = 1
            return 1
        elif j == i + 1:
            if s[i] == s[j]:
                self.dp[i][j] = 1
                return 1
            else:
                self.dp[i][j] = 0
                return 0
        else:
            if self.f(s, i + 1, j - 1) == 1 and s[i] == s[j]:
                self.dp[i][j] = 1
                return 1
            else:
                self.dp[i][j] = 0
                return 0

    def longestPalindrome(self, s: str) -> str:
        self.dp = [[-1] * len(s) for _ in range(len(s))]
        for x in range(len(s)):
            for y in range(x + 1):
                i = y
                j = len(s) - 1 - x + y
                if self.f(s, i, j) == 1:
                    return s[i:j + 1]


if __name__ == '__main__':
    solution = Solution()
    s = "twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqqlrcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"
    print(solution.longestPalindrome(s))
