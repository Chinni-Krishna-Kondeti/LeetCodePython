def removeElement(self, nums, val: int) -> int:
    i = 0
    n = len(nums)
    while (i < n):
        if nums[i] == val:
            del nums[i]
            n -= 1
        else:
            i += 1
    return n