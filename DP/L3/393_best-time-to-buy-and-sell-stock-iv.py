# 393. Best Time to Buy and Sell Stock IV
# 中文English
# Given an array prices and the i-th element of it represents the price of a stock on the i-th day.
#
# You may complete at most k transactions. What's the maximum profit?
#
# Example
# Example 1:
#
# Input: k = 2, prices = [4, 4, 6, 1, 1, 4, 2 ,5]
# Output: 6
# Explanation: Buy at 4 and sell at 6. Then buy at 1 and sell at 5. Your profit is 2 + 4 = 6.
# Example 2:
#
# Input: k = 1, prices = [3, 2, 1]
# Output: 0
# Explanation: No transaction.
# Challenge
# O(nk) time. n is the size of prices.
#
# Notice
# You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
import sys


class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """

    def maxProfit(self, K, prices):
        # write your code here
        # write your code here
        n = len(prices)
        if n == 0:
            return 0

        if K > n / 2:  # it means unlimited buy/sell
            ans = 0
            for i in range(1, n):
                if (prices[i] - prices[i - 1]) > 0:
                    ans += prices[i] - prices[i - 1]
            return ans

        # have 2*K+1 states, but we count from state 1,2,3,...so need to add another one.
        f = [[0] * (2 * K + 1 + 1) for _ in range(n + 1)]

        for k in range(1, 2 * K + 1 + 1):
            f[0][k] = -sys.maxsize  # impossible to reach, except f[0][1]

        f[0][1] = 0

        for i in range(1, n + 1):
            # 阶段1，3，5,....2K+1
            for j in range(1, 2 * K + 1 + 1, 2):
                # f[i][j] = max(f[i-1][j], f[i - 1][j - 1] + (prices[i - 1] - prices[i - 2]))
                f[i][j] = f[i - 1][j]  # keep state
                if j > 1 and i >= 2 and f[i - 1][j - 1] != -sys.maxsize:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + (prices[i - 1] - prices[i - 2]))  # sell
            # 阶段2，4,....2K
            for j in range(2, 2 * K + 1, 2):
                # f[i][j] = max(f[i-1][j] + (prices[i - 1] - prices[i - 2]), f[i-1][j-1])
                f[i][j] = f[i - 1][j - 1]  # buy
                if i > 1 and f[i - 1][j] != -sys.maxsize:
                    f[i][j] = max(f[i][j], f[i - 1][j] + (prices[i - 1] - prices[i - 2]))  # keep state

        rslt = 0
        for j in range(1, 2 * K + 1 + 1, 2):
            rslt = max(rslt, f[n][j])
        return rslt


K = 2
prices = [4, 4, 6, 1, 1, 4, 2, 5]
sol = Solution()
sol.maxProfit(K, prices)
