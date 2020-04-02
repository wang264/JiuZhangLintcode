# 669. Coin Change
# 中文English
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the
# fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example
# Example1
#
# Input:
# [1, 2, 5]
# 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example2
#
# Input:
# [2]
# 3
# Output: -1
# Notice
# You may assume that you have an infinite number of each kind of coin.
import sys


class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """

    def coinChange(self, coins, amount):
        # write your code here
        # dp[i] = the minimum number of coins could combine with money amount i
        # for example, if coins are [1,2,5].
        # then dp[27] = min( dp[27-1]+1, dp[27-2]+1, dp[27-5]+1)
        # for example dp[27-5]+1 means that we use minimum number of coins to get to amount '22' then use an
        # additional '5' cent coins to get to 27=22+5

        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0  # do not need to use any coins to get to amount 0.
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            for k in coins:
                if i - k >= 0:
                    dp[i] = min(dp[i], dp[i - k] + 1)

        if dp[amount] == sys.maxsize:
            return -1
        else:
            return dp[amount]


coins = [9, 9]
amount = 0
