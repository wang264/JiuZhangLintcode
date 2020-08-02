# 硬币排成线 III · Coins in a Line III
# 博弈论
# LintCode 版权所有
# 动态规划
# 数组
# 描述
# There are n coins in a line, and value of i-th coin is values[i].
#
# Two players take turns to take a coin from one of the ends of the line until there are no more coins left.
# The player with the larger amount of money wins.
#
# Could you please decide the first player will win or lose?
#
# 样例
# Example 1:
#
# Input: [3, 2, 2]
# Output: true
# Explanation: The first player takes 3 at first. Then they both take 2.
# Example 2:
#
# Input: [1, 20, 4]
# Output: false
# Explanation: The second player will take 20 whether the first player take 1 or 4.
# 挑战
# O(1) memory and O(n) time when n is even.

# 算法：区间DP ， 博弈
# 这道题目的限制条件说在偶数个数字下做到O(n)时间复杂度内得到先手必胜的结果。因为先手者可以计算编号是奇数的堆的和以及编号是偶数
# 的堆的和，然后比较，如果奇数堆和大的话，那就先选择第一个，然后保持选择奇数堆即可,保持选择奇数编号的数。如果是偶数堆和较大的
# 话，那么先选择最后一个堆，然后保持选择偶数堆即可,那就保持选择偶数编号的数，偶数个数可以保证选择的数的下标奇偶性保持一致，
# 所以先手必胜。
#
# 但是奇数或更一般的情况来说，我们需要用动态规划来解决这个问题，用dp[i][j]表示values[i ... j]之间取第i或第j枚硬币的玩家可以
# 赢得的最大分数差。先手可以赢后手的分数，并且此时先手取的是i或者j。
#
# 对于某个范围dp[i][j]来说
#
# 如果先手取i，那么dp[i][j] = values[i]-dp[i+1][j]，因为values[i+1]~values[j]是后手赢先手的分数，所以此时先手选择values[i]
# 和它做差；
# 如果先手取j，那么同理dp[i][j] = values[j]-dp[i][j-1]。
# 最后就是取这两者的极大值，即 dp[i][j] = max(values[i]-dp[i+1][j], values[j]-dp[i][j-1])。可以看出是一个区间DP。
# 那么最后的结果就是看dp[0][n-1](n是values的长度)，因为0和n-1就是先手可以进行选择的目标。

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        n = len(values)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):  # 初始化
            dp[i][i] = values[i]
        for length in range(1, n):
            for i in range(n - length):
                # 如果先手取i，那么dp[i][j] = values[i]-dp[i+length][j]，因为values[i+length]~values[j]是后手赢先手的分数，
                # 所以此时先手选择values[i]和它做差
                # 如果先手取j=i+length，那么dp[i][j] = values[j]-dp[i][j-length]
                dp[i][i + length] = max(values[i] - dp[i + 1][i + length], values[i + length] - dp[i][i + length - 1])
        # 判断差值是否大于零便能知道赢了输了
        return dp[0][n - 1] > 0

sol = Solution()
sol.firstWillWin([3, 2, 2])
sol.firstWillWin([1,20,4])