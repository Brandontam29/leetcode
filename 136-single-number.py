# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

from functools import reduce
from typing import List


# O(n) time and O(1) memory
def singleNumber(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res ^= n
    return res


# O(n) time and O(1) memory
def singleNumber2(nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)


# O(n) time and O(n) memory
def singleNumberBad(nums: List[int]) -> int:
    s = set()
    for n in nums:
        if n in s:
            s.remove(n)
        else:
            s.add(n)

    return list(s)[0]


print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1]))
