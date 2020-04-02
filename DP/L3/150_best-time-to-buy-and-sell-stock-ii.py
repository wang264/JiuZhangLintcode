# 150. Best Time to Buy and Sell Stock II
# 中文English
# Given an array prices, which represents the price of a stock in each day.
#
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, if you already have the stock, you must sell it before you buy again).
#
# Design an algorithm to find the maximum profit.
#
# Example
# Example 1:
#
# Input: [2, 1, 2, 0, 1]
# Output: 2
# Explanation:
#     1. Buy the stock on the second day at 1, and sell the stock on the third day at 2. Profit is 1.
#     2. Buy the stock on the 4th day at 0, and sell the stock on the 5th day at 1. Profit is 1.
#     Total profit is 2.
# Example 2:
#
# Input: [4, 3, 2, 1]
# Output: 0
# Explanation: No transaction, profit is 0.

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        # if we can buy/sell unlimited time, but may not engage in multiple transactions at the same time
        # then we can capture every uptick
        if not prices:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            # buy at [i-1] sell at [i]
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]

        return profit