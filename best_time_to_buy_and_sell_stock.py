class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price>buy_price:
                max_profit= max(max_profit, price-buy_price)
            else:
                buy_price = price
        return max_profit