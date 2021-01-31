# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    number_idx = dict()
    for i in range(len(nums)):
        value = target - nums[i]
        if value in number_idx:
            return [number_idx[value], i]
        number_idx[nums[i]] = i