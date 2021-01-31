# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.

from typing import List


def find_duplicate(nums: List[int]) -> int:
    total_num = set()
    for i in nums:
        if i in total_num:
            return i
        total_num.add(i)