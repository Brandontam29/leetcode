# recursive
def rob(nums: list[int]):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    return max(nums[0] + rob(nums[2:]), rob(nums[1:]))


def rob2(nums):
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n + 1, ...]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


print(rob2([1, 2, 3]))  # 4

print(rob2([1, 2, 3, 2, 2]))  # 6

print(rob2([5, 1, 9, 9, 1, 9]))  # 23

print(rob([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238,
      168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]))  # 23
