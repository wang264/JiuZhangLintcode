# 395. Coins in a Line II
# 中文English
# There are n coins with different value in a line. Two players take turns to take one or two coins
# from left side until there are no more coins left. The player who take the coins with the most value wins.
#
# Could you please decide the first player will win or lose?
#
# If the first player wins, return true, otherwise return false.
#
# Example
# Example 1:
#
# Input: [1, 2, 2]
# Output: true
# Explanation: The first player takes 2 coins.
# Example 2:
#
# Input: [1, 2, 4]
# Output: false
# Explanation: Whether the first player takes 1 coin or 2, the second player will gain more value.

class Solution:
    """
   @param values: a vector of integers
   @return: a boolean which equals to true if the first player will win
   """

    # 先手的目标是让自己拿到的数字之和不比对手少。
    # 己方的数字之和为A，对方的数字之和为B -》 己方目标为A>=B -----> S_a = A - B >= 0    S_b = B - A = - S_a
    # 当X面对剩下的数字的时候，X为当前的先手，目标为最大化 S_x = X- Y
    # 当取走数字的和为m后，对手Y变先手，他要最大化S_y = Y - X

    # 假设当前轮，X为先手。取走了m。 然后在后面的轮中X 取走了 X'， Y取走了Y'. 那么X和Y得分的差为。
    # S_x = m + X' - Y'    ----> S_x = m - (Y' - X') ----> S_x = m - S_y
    # 因为S_y = Y' - X' ， 为Y在面对被拿走m后的得分（与X的得分的差）
    # dp[i] = 先手在面对 a[i.....n-1] 这些数字的时候，能得到的最大与对手的数字差。
    # 　dp[i] = max( a[i]-f[i+1],    a[i]+a[i+1] - f[i+2] )

    def firstWillWin(self, values):
        n = len(values)
        if n <= 2:
            return True
        dp = [None] * (n + 1)
        dp[n - 1] = values[n - 1]  # i=len-1时,只有一个可以拿
        dp[n - 2] = values[n - 1] + values[n - 2]  # i = len-2,有两个可拿，直接拿走
        # 当i=len-3的时候，剩下最后三个，这时候如果拿一个，对方就会拿走两个，所以这次拿两个.然后对手拿走一个
        dp[n - 3] = values[n - 2] + values[n - 3] - values[n - 1]

        for i in range(n - 4, -1, -1):
            dp[i] = max(values[i] - dp[i + 1], values[i] + values[i + 1] - dp[i + 2])

        return dp[0] >= 0


sol = Solution()
sol.firstWillWin([1, 2, 2])
sol.firstWillWin([1, 2, 4])


class Solution_2:
    """
   @param values: a vector of integers
   @return: a boolean which equals to true if the first player will win
   """

    # 算法：DP
    # len 表示硬币数组的长度，下标从0开始
    #
    # 用一个数组dp[i]表示从i到len - 1能拿到的最大值
    #
    # 一个明显的情况就是当len <= 2 时，这时候先手拿的只要全拿走就行了，所以肯定是先手赢。然后我们分析
    #
    # 当i = len的时候，dp[len]没得可拿，所以dp[len] = 0
    # 当i = len - 1 的时候，dp[len - 1] 只有一个可以拿，所以dp[len - 1] = values[len - 1];
    # 当i = len - 2 的时候，dp[len - 2] 有两个可拿，当然是直接拿走, 所以dp[len - 2] = values[len - 1] + values[len - 2];
    # 当i = len - 3 的时候，剩下最后三个，这时候如果拿一个，对方就会拿走两个，
    # 所以，这次要拿两个，所以dp[len - 3] = values[len - 2] + values[len - 3];
    # 当i = len - 4 以及以后的情况中，显然可以选择拿一个或者拿两个两种情况，我们自然是选择拿最多的那个作为dp的值，那么我们就分分析这两种情况：
    # 第一种，只拿一个, 那么对手可能拿两个或者一个，对手肯定是尽可能多拿，然后让你剩下的少，所以我们要选择尽可能小的那个，所以dp[i] = values[i] + min(dp[i + 2], dp[i + 3])
    # 第二种，拿两个，同样的情况，dp[i] = values[i] + values[i + 1] + min(dp[i + 3], dp[i + 4])
    # 然后我们取这两种情况下的最大值。
    # dp[0] 表示先手获得的最大值，sum - dp[0] 表示后手获得的最大值，比较两者即可判断先手是否必胜
    # 复杂度分析
    # 时间复杂度O(n)
    # n为硬币的数量
    # 空间复杂度O(n)
    # n为硬币的数量
    def firstWillWin(self, values):
        size = len(values)
        if size <= 2:
            return True
        dp = [0] * (size + 1)
        Sum = 0
        dp[size - 1] = values[size - 1]
        dp[size - 2] = values[size - 1] + values[size - 2]
        dp[size - 3] = values[size - 2] + values[size - 3]
        Sum += (values[size - 1] + values[size - 2] + values[size - 3])
        for i in range(size - 4, -1, -1):
            Sum += values[i]
            dp[i] = max(values[i] + min(dp[i + 2], dp[i + 3]),  # 只拿一个,那么对手可能拿两个或者一个，对手肯定是尽可能多拿，所以我们要选择尽可能小的那个
                        values[i] + values[i + 1] + min(dp[i + 3], dp[i + 4]))  # 拿两个，同样的情况
        # 由于硬币总数是确定的，我们比较一下先手的硬币dp[0]和后手的硬币数量sum-dp[0]就能得到答案
        return dp[0] > Sum - dp[0]


sol_2 = Solution_2()
sol_2.firstWillWin([1, 2, 2])
sol_2.firstWillWin([1, 2, 4])
