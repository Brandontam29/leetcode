# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

from functools import cache
from time import perf_counter
from typing import List


# O(n^2)
def countBits(n: int) -> List[int]:
    def countOnes(num: int) -> int:
        res = 0
        while num:
            num = num & (num-1)
            res += 1
        return res

    arr = []
    for i in range(n+1):
        arr.append(countOnes(i))

    return arr


@cache
def countBitsCache(n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i

        dp[i] = 1 + dp[i-offset]

    return dp

# O(n)


def countBits2(n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i

        dp[i] = 1 + dp[i-offset]

    return dp


# O(n)
@cache
def countBits2Cache(n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i

        dp[i] = 1 + dp[i-offset]

    return dp


print(countBits2(1))  # [0,1]
print(countBits2(2))  # [0,1,1]
print(countBits2(4))  # [0,1,1]
print(countBits2(5))  # [0,1,1,2,1,2]

# 3.269982799945865
t1_start = perf_counter()
countBits(2500000)
t1_stop = perf_counter()
print(t1_stop-t1_start)

# 0.39764560002367944
t1_start = perf_counter()
countBitsCache(2500000)
t1_stop = perf_counter()
print(t1_stop-t1_start)

# 0.3995678999926895
t1_start = perf_counter()
countBits2(2500000)
t1_stop = perf_counter()
print(t1_stop-t1_start)

# 0.3929194000083953
t1_start = perf_counter()
countBits2Cache(2500000)
t1_stop = perf_counter()
print(t1_stop-t1_start)
