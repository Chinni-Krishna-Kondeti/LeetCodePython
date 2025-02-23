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

# print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))