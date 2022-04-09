# bottom approach to dynamic problem
# calculate every smaller subproblem until the answer
def coinChange(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)

    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c < 0:
                continue

            if dp[a - c] < 0:
                continue

            dp[a] = min(1 + dp[a - c], dp[a])

    # found answer
    if dp[amount] != (amount + 1):
        return dp[amount]

    # did not find answer
    return -1


print(coinChange([12, 1, 2, 5], 11))  # 3
print(coinChange([9, 4, 2], 12))  # 3
print(coinChange([12, 25], 11))  # -1
print(coinChange([], 0))  # 0
print(coinChange([5, 4, 3, 1], 7))  # 2
