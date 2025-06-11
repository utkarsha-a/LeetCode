class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cost = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < cost:
                cost = prices[i]
            else:
                max_profit = max(max_profit, prices[i]-cost)
        return max_profit
