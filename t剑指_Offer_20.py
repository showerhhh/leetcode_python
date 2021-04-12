import re

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except:
            return False
        return True

    def isNumber_2(self, s: str) -> bool:
        matchObj = re.match('^\s*[+-]{0,1}((\d)+((\.)(\d)+){0,1}|((\.)(\d)+)|((\d)+(\.)))([eE][+-]{0,1}[\d]+){0,1}\s*$', s)
        if matchObj:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    solution.isNumber_2('-123')
