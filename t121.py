class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0
        minprice = float('inf')
        maxprofit = float('-inf')
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            if prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit


if __name__ == '__main__':
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))
