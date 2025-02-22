def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    temp = nums[-k::]
    for j in range(n-1-k, -1, -1):
        nums[j], nums[j+k] = nums[j+k], nums[j]
    for j in range(k):
        nums[j] = temp[j]
    print(nums)


rotate(nums = [1,2,3,4,5,6,7], k = 3)