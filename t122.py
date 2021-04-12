class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        minprice = float('inf')
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            if 1 <= i < len(prices) - 1 and prices[i] > prices[i + 1]:
                profit += prices[i] - minprice
                minprice = float('inf')
            if i == len(prices) - 1 and prices[i] > minprice:
                profit += prices[i] - minprice
        return profit
