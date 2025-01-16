# def maxProfit(k, prices):
#     buy = 999999
#     is_buy = True
#     sell = 0
#     prices += [-1]
#     profits = []
#     for price in prices:
#         if is_buy:
#             if buy > price:
#                 buy = price
#             else:
#                 sell = price
#                 is_buy = False
#         else:
#             if sell < price:
#                 sell = price
#             elif sell > price:
#                 profits += [sell - buy]
#                 buy = price
#                 is_buy = True
#                 sell = 0
#     profits.sort()
#     print(profits)
#     return sum(profits[:k])

def maxProfit(k, prices):
    buy = 999999
    is_buy = True
    sell = 0
    prices += [-1]
    profits = []
    for price in prices:
        if is_buy:
            if buy > price:
                buy = price
            else:
                sell = price
                is_buy = False
        else:
            if sell < price:
                sell = price
            elif sell > price:
                profits += [sell - buy]
                buy = price
                is_buy = True
                sell = 0
    profits.sort()
    print(profits)
    return sum(profits[:k])
print(maxProfit( k = 2, prices = [1,2,4,2,5,7,2,4,9,0]))