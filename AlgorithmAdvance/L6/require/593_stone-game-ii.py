# 石头游戏 II · Stone Game II
# 动态规划
# There is a stone game.At the beginning of the game the player picks n piles of stones in a CIRCLE.
#
# The goal is to merge the stones in one pile observing the following rules:
#
# At each step of the game,the player can merge two adjacent piles to a new pile.
# The score is the number of stones in the new pile.
# You are to determine the minimum of the total score.
#
# 样例
# Example 1:
#
# Input:
# [1,1,4,4]
# Output:18
# Explanation:
# 1. Merge second and third piles => [2, 4, 4], score +2
# 2. Merge the first two piles => [6, 4]，score +6
# 3. Merge the last two piles => [10], score +10
# Example 2:
#
# Input:
# [1, 1, 1, 1]
# Output:8
# Explanation:
# 1. Merge first and second piles => [2, 1, 1], score +2
# 2. Merge the last two piles => [2, 2]，score +2
# 3. Merge the last two piles => [4], score +4

# 因为这道题要求石子堆是环形的，所以A[n-1],A[0]也是一段可以合并的连续区间，因此我们可以把给定的石子堆按原顺序延长一倍。
# 这样就避免了计算区间“左端点在尾部，右端点在头部”情况的麻烦。比如1，2，1可以扩张至1，2，1，1，2，1。这样原区间的所有
# 集合都可以在新的数组中以连续下标的形式表示。

# 我们最后得到的dp[i][i+n-1]即为以第i堆石子堆作为起点的n堆石子堆合并的最小代价。最后比较每一种可能得到的最小值就是答案。


import sys


class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def stoneGame2(self, A):
        n = len(A)
        if n == 0:
            return 0
        prefix_sum = [0] * (2 * n + 1)
        dp = [[None]*(2 * n + 1) for _ in range(2 * n + 1)]
        for i in range(1, 2 * n + 1):
            # 做一次前缀和，减少时间复杂度
            prefix_sum[i] = prefix_sum[i - 1] + A[(i - 1) % n]
            dp[i][i] = 0
        # 枚举长度
        for length in range(2, n + 1):
            # 枚举起点
            i = 1
            while i + length - 1 <= 2 * n:
                # j为i为起点时的石子堆终点
                j = i + length - 1
                dp[i][j] = sys.maxsize
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + prefix_sum[j] - prefix_sum[i - 1])
                i += 1
        ans = sys.maxsize
        for i in range(1, n + 1):
            # 取最小的 以第i堆石子堆作为起点的n堆石子堆合并的最小代价
            ans = min(ans, dp[i][i + n - 1])
        return ans
