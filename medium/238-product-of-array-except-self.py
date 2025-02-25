import math


def productExceptSelf(nums):
    prod = 1
    index = -1
    n = len(nums)
    for i in range(n):
        if nums[i] != 0:
            prod *= nums[i]
        else:
            if index == -1:
                index = i
            else:
                return [0] * n
    if index == -1:
        for i in range(n):
            nums[i] = prod // nums[i]
        return nums
    else:
        output = [0] * n
        output[index] = prod
        return output


def productExceptSelf1(nums):
    n = len(nums)
    output = [1] * n
    for i in range(1, n):
        output[i] = output[i-1] * nums[i-1]
    prd = 1
    for i in range(n-2, -1, -1):
        prd *= nums[i+1]
        output[i] *= prd
    return output
print(productExceptSelf1([1,2,3,4]))
print(productExceptSelf1([-1,1,0,-3,3]))