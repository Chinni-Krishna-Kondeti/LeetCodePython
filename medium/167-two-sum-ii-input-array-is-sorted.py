def twoSum1(numbers, target):
    data = dict()
    output = []
    for i in range(len(numbers)):
        res = target - numbers[i]
        if res not in data:
            data[numbers[i]] = i
        else:
            output = [data[res]+1, i+1]
            break
    return output
def twoSum(numbers, target):
    i = 0
    j = len(numbers)-1
    s = numbers[i] + numbers[j]
    while s!= target:
        if s > target:
            j -= 1
        else:
            i += 1
        s = numbers[i] + numbers[j]
    return i+1, j+1
print(twoSum([2,7,11,15], 9))
print(twoSum([5,25,75], 100))
print(twoSum([3,24,50,79,88,150,345], 200))
