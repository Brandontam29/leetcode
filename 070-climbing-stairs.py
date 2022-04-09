import time


# recursion
def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    return climbStairs(n-1) + climbStairs(n-2)

# recursion with memo


def climbStairs2(n: int) -> int:
    memo = [-1 for x in range(n+1)]
    if memo[n] >= 0:
        return memo[n]

    if n <= 2:
        return n

    memo[n] = climbStairs(n-1) + climbStairs(n-2)

    return memo[n]


# recursion with memo
def climbStairs2(n: int) -> int:
    memo = [-1 for x in range(n+1)]

    def recur(memo, num):

        if num == 2 or num == 1:
            return num

        if memo[num] >= 0:
            return memo[num]

        memo[num] = recur(memo, num - 1) + recur(memo, num - 2)
        return memo[num]

    return recur(memo, n)


# O(n)
def climbStairs3(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


# start = time.time()
# print(climbStairs(36))
# end = time.time()
# print(end - start)

start = time.time()
print(climbStairs2(500))
end = time.time()
print(end - start)

start = time.time()
print(climbStairs3(500))
end = time.time()
print(end - start)

# Stairs|  Ways
# 1     |   1
# 2     |   2
# 3     |   3
# 4     |   5
# 5     |   8
# 6     |   13
