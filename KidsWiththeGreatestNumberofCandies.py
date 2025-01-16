def kidsWithCandies(candies, extraCandies):
    result = list()
    m = max(candies) - extraCandies
    for i in candies:
        result.append(i >= m)
    return result
