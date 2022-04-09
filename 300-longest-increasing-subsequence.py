# brute force
def lengthOfLIS(nums: list[int]) -> int:
    dp = [1] * len(nums)

    for n in range(len(nums) - 1, -1, -1):

        for x in range(n + 1, len(nums)):
            if nums[n] < nums[x]:
                dp[n] = max(dp[n], 1 + dp[x])

    return max(dp)


print(lengthOfLIS([1, 2, 4, 3]))  # 3
print(lengthOfLIS([1, 9, 2, 10]))  # 3
print(lengthOfLIS([0, 3, 1, 6, 2, 2, 7]))  # 4
print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
