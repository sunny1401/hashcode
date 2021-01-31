# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
# of all the elements of nums except nums[i].


from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    output = [0 for i in nums]

    output[0] = 1
    for i in range(1, len(nums)):
        output[i] = output[i - 1] * nums[i - 1]

    multiply = 1
    for i in reversed(range(len(nums))):
        output[i] = output[i] * multiply
        multiply *= nums[i]

    return output
