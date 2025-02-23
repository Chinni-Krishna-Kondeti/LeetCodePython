def hIndex(citations) -> int:
    output = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            output = i + 1
        else:
            break
    return output

print(hIndex([3,0,6,1,5]))
print(hIndex([1]))