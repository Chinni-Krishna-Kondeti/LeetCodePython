def maxProfit(prices) -> int:
    i = 0
    s = 0
    while i < len(prices) - 1:
        if prices[i] < prices[i+1]:
            s += prices[i+1] - prices[i]
        i += 1
    return s

print(maxProfit([7,1,5,3,6,4]))