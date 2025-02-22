def maxProfit(prices) -> int:
    profit = 0
    buy = prices[0]
    for sell in prices:
        if sell < buy:
            buy = sell
        else:
            profit = max(profit, sell - buy)
    return profit

def maxProfit1(prices) -> int:
    i = 0
    data = list()
    while i < len(prices) - 1:
        data.append(prices[i + 1] - prices[i])
        i += 1
    s = 0
    profit = 0
    for i in data:
        if i > 0:
            s = s + i
        else:
            profit = max(profit, s)
            s = 0 if s+i < 0 else s+i
    return max(profit, s)


print(maxProfit1([7,1,5,3,6,4]))