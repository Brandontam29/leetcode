# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# O(n^2)
def maxProfit(prices) -> int:
    mem = set()
    for i1, p in enumerate(prices):
        for i2 in range(i1, len(prices)):
            mem.add(prices[i2]-p)

    return max(mem)


# O(n)
def maxProfit2(prices) -> int:
    length = len(prices)
    dp = [0] * length

    for i in range(length-2, -1, -1):
        dp[i] = max(prices[i+1] - prices[i] + dp[i+1], 0)

    return max(dp)


print(maxProfit([1, 2]))
print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))

print(maxProfit2([1, 2]))
print(maxProfit2([7, 1, 5, 3, 6, 4]))
print(maxProfit2([7, 6, 4, 3, 1]))
