# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if nums == []:
        return 0

    s = sorted(list(set(nums)))
    dp = [1] * len(nums)
    for n in range(len(s) - 2, -1, -1):
        if s[n] + 1 == s[n + 1]:
            dp[n] += dp[n+1]

    return max(dp)


print(longestConsecutive([0, 0, 1, 2, 3, 9, 10]))  # 4
print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
