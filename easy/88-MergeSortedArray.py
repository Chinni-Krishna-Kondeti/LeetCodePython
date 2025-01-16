from typing import List


def merge( nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    while (i != m and j != n):
        if (nums1[i] > nums2[j]):
            nums1 = nums1[:i] + [nums2[j]] + nums1[i:]
            j += 1
        i +=1
    if i==m:
        nums1 = nums1[:-n] + nums2[j:]
    return nums1

print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

