def twoSum(nums, target: int):
    data = dict()
    output = []
    for i in range(len(nums)):
        res = target - nums[i]
        if res not in data:
            data[nums[i]] = i
        else:
            output = [data[res], i]
            break
    return output
