def canJump(nums):
    i = len(nums) - 2
    n = 1
    while i>=0:
        if i == 0:
            return nums[0] >= n
        if nums[i] >= n:
            n = 1
        else:
            n += 1
        i -= 1
    return True

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))