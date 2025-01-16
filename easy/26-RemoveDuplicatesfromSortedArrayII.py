def removeDuplicates(nums):
    i=0
    pe = -99999
    d = -99999
    while i<len(nums):
        if nums[i] == pe:
            d = pe
            pe = -99999
            i += 1
        elif nums[i] == d:
            nums.pop(i)
        else:
            pe = nums[i]
            i += 1
    return len(nums)




print(removeDuplicates([0,0,1,1,1,1,2,3,3]))