def majorityElement( nums) -> int:
    nums.sort()
    return nums[int(len(nums) // 2)]

print(majorityElement([3,2,2,3,3]))