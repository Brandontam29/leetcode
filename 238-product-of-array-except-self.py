# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    arr = [1] * len(nums)
    post = nums[-1]

    for n in range(1, len(nums)):
        arr[n] = arr[n - 1] * nums[n-1]

    for n in range(len(nums) - 2, -1, -1):
        arr[n] *= post
        post *= nums[n]

    return arr


print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(productExceptSelf([2, 0, 2]))  # [0, 4, 0]
print(productExceptSelf([1, 2, 3, 4, -1, -1, 0]))  # [0, 0, 0, 0, 0, 0, 24]
