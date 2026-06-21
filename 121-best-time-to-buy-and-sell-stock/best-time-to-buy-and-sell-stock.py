class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        price = prices[0]

        for p in prices:
            max_profit = max(max_profit, (p-price))
            if p<price:
                price = p
        return max_profit




        '''
        max_profit = 0
        price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-price)
            if prices[i]<price:
                price = prices[i]
        return max_profit
'''