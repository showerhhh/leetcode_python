class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        i = len(a)
        j = len(b)
        while i < j:
            a.insert(0, '0')
            i += 1
        while i > j:
            b.insert(0, '0')
            j += 1
        c = []
        carry = 0
        for i in range(len(a)-1, -1, -1):
            temp = int(a[i]) + int(b[i]) + carry
            c.insert(0, str(temp % 2))
            carry = int(temp / 2)
        if carry == 1:
            c.insert(0, '1')
        return ''.join(c)


if __name__ == '__main__':
    solution = Solution()
    a = '11'
    b = '1'
    print(solution.addBinary(a, b))
