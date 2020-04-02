# 149. Best Time to Buy and Sell Stock
# 中文English
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example
# Example 1
#
# Input: [3, 2, 3, 1, 2]
# Output: 1
# Explanation: You can buy at the third day and then sell it at the 4th day. The profit is 2 - 1 = 1
# Example 2
#
# Input: [1, 2, 3, 4, 5]
# Output: 4
# Explanation: You can buy at the 0th day and then sell it at the 4th day. The profit is 5 - 1 = 4
# Example 3
#
# Input: [5, 4, 3, 2, 1]
# Output: 0
# Explanation: You can do nothing and get nothing.

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0

        # min_price store the minimum price we seen so far, from day 0 to day i
        min_price = prices[0]

        # max_profit store the max_profit so far
        max_profit = 0

        # the max profit if we sell the stock at the ith day.
        for i in range(1, len(prices)):
            # if we decide to sell the stock at ith day, then to get the maximum profit is to
            # buy at the minimum among prices[0].....prices[i-1], which is stored at min_price
            max_profit = max(max_profit, prices[i] - min_price)

            min_price = min(min_price, prices[i])

        return max_profit


sol = Solution()
prices = [1, 2, 3, 4, 5]
sol.maxProfit(prices)
