from typing import List

p = [7,1,5,3,6,4]


def maxProfit(prices: List[int]) -> int:
    buy = prices[0]
    profit = 0
    for price in prices[1:]:
        sell = price
        real_profit = sell - buy
        if real_profit > profit:
            profit = real_profit
        if price < buy:
            buy = price
    return profit


print(maxProfit(p))
