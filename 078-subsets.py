# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# TODO THIS IS WRONG

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = ()
    log = []
    for n in range(len(nums)):
        result.add([n])
        for i in range(len(nums)):

            result.add([nums[n], nums[n+i]])


print(subsets([1, 2, 3]))
print(subsets([0]))
