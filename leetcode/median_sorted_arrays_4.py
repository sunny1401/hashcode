# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums1.extend(nums2)
    nums1 = sorted(nums1)
    num_elements = len(nums1)

    if all(n == 0 for n in nums1):
        return round(0.0, 5)

    if num_elements % 2:
        return round(float(nums1[int(num_elements / 2)]), 5)

    else:
        num1 = nums1[int(num_elements / 2) - 1]
        num2 = nums1[int((num_elements) / 2)]
        return round(float((num1 + num2) / 2), 5)