# 396. Coins in a Line III
# 中文English
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

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    # f[i][j] = 先手在面对a[i....j]这些数字时，能得到的最大的与对手的数字差。
    # f[i][j] = max(a[i] - f[i+1][j], a[j] - f[i][j-1])
    # 取头或者取尾巴， 减号是因为，取完后对方先手。变成对方和你的数字差，所以要反过来。
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        if n == 0:
            return True

        f = [[None] * n for _ in range(n)]

        for i in range(n):
            f[i][i] = values[i]

        # 每一段的长度
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                f[i][j] = max(values[i] - f[i + 1][j], values[j] - f[i][j - 1])

        if f[0][n - 1] > 0:
            return True
        else:
            return False


values = [3, 2, 2]
sol=Solution()
sol.firstWillWin(values)
import sys


class Solution2:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    # dp[i][j] the maximum score difference(A-B) when A is first to act and facing number
    # values[i].....values[j]  i<=j
    def firstWillWin(self, values):
        n = len(values)
        dp = [[-1 * sys.maxsize] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = values[i]

        for length in range(2, n + 1):  # iterate for each length
            for j in range(length - 1, n):  # end_index
                i = j - length + 1  # start_index
                # facing nums[i].....nums[j]
                # you can take nums[i] ---->another player get dp[i+1][j]
                dp[i][j] = max(dp[i][j], values[i] - dp[i + 1][j])
                # you can take nums[j[ ---->another player get dp[i][j-1]
                dp[i][j] = max(dp[i][j], values[j] - dp[i][j - 1])

        return dp[0][n - 1] > 0

sol = Solution2()
sol.firstWillWin(values = [3, 2, 2])