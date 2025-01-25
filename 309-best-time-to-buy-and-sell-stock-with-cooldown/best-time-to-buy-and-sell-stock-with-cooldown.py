class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        sell, buy, pbuy, psell = 0, -prices[0], 0, 0
        for price in prices:
            pbuy = buy
            buy = max(psell - price, pbuy)
            psell = sell
            sell = max(pbuy + price, psell)
        return sell

     
        