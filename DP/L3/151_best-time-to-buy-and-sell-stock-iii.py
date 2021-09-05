# 151. Best Time to Buy and Sell Stock III
# 中文English
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Example
# Example 1
#
# Input : [4,4,6,1,1,4,2,5]
# Output : 6
# Notice
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# 五个阶段
# 阶段1：第一次买之前
#   ---第一次买
# 阶段2：持有股票
#   ---第一次卖
# 阶段3：第一次卖之后，第二次买之前
#   ---第二次买
# 阶段4：持有股票
#   ---第二次卖
# 阶段5：第二次卖之后

# 阶段可以保持：在阶段2，4，手里有股票的话。当天获利当天结算。获利为当天价格减去昨天价格。
# 阶段可以变化： 在阶段2，卖了一股后，进入阶段3

# 最优策略一定是前N天（第N-1天）结束后，处于：
# ---阶段1：没买卖过， 阶段3：买卖过一次， 阶段5：买卖过两次

# 状态： f[i][j] = 表示前i天（第i-1天）结束后，在阶段j的最大获利。

# 阶段5，看状态转移，求前N天（第N-1天）在阶段5的最大获利，设为f[N][5]:
# --情况1： 在前N-1天就在阶段5， f[N][5] = f[N-1][5]
# --情况2： 在前N-1天还在阶段4， 第N天卖掉 则f[N-1][4] + [P(n-1) - P(n-2)]
# 阶段1，3，5都同理为手中无股票的状态

# 阶段4， 看状态转移，求前N天（第N-1天）在阶段5的最大获利，设为f[N][4]:
# --情况1： 在前N-1天就在阶段4， f[N][4] = f[N-1][4] + [P(n-1) - P(n-2)]
# --情况2： 在前N-1天还在阶段3， 前N天（今天）买了股票 则f[N-1][3]
# 阶段2，4都同理为。。。手中有股票

import sys


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        if n == 0:
            return 0

        f = [[0] * (5 + 1) for _ in range(n + 1)]

        for k in range(1, 6):
            f[0][k] = -sys.maxsize  # impossible to reach, except f[0][1]

        f[0][1] = 0

        for i in range(1, n + 1):
            # 阶段1，3，5
            for j in range(1, 5 + 1, 2):
                # f[i][j] = max(f[i-1][j], f[i - 1][j - 1] + (prices[i - 1] - prices[i - 2]))
                f[i][j] = f[i - 1][j]  # keep state
                if j > 1 and i >= 2 and f[i - 1][j - 1] != -sys.maxsize:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + (prices[i - 1] - prices[i - 2]))  # sell
            # 阶段2，4
            for j in range(2, 4 + 1, 2):
                # f[i][j] = max(f[i-1][j] + (prices[i - 1] - prices[i - 2]), f[i-1][j-1])
                f[i][j] = f[i - 1][j - 1]  #just bought the stock on ith date.
                if i > 1 and f[i - 1][j] != -sys.maxsize:
                    f[i][j] = max(f[i][j], f[i - 1][j] + (prices[i - 1] - prices[i - 2]))  #keep state

        rslt = 0
        for j in range(1, 5 + 1, 2):
            rslt = max(rslt, f[n][j])
        return rslt


sol = Solution()
prices = [4, 4, 6, 1, 1, 4, 2, 5]
sol.maxProfit(prices)
