# 476. Stone Game
# 中文English
# There is a stone game.At the beginning of the game the player picks n piles of stones in a line.
#
# The goal is to merge the stones in one pile observing the following rules:
#
# 1.At each step of the game,the player can merge two adjacent piles to a new pile.
# 2.The score is the number of stones in the new pile.
# You are to determine the minimum of the total score.
#
# 样例
# Example 1:
#
# Input: [3, 4, 3]
# Output: 17
# Example 2:
#
# Input: [4, 1, 1, 4]
# Output: 18
# Explanation:
#   1. Merge second and third piles => [4, 2, 4], score = 2
#   2. Merge the first two piles => [6, 4]，score = 8
#   3. Merge the last two piles => [10], score = 18


# use prefix sum to store the sum of the stones weight.
# dp[i][j]  = the minimum energy/score the merge from stone A[i] to stone A[j] into one pile.
# we iterate over the last step before stone A[i]~~A[j] become one single pile.
# if the last step is to merge pile A[i] and pile A[i+1].....A[j](this pile already merge into one single pile)
# the total energy/score is A[i]+dp[i+1][j] +sum(A[i]......A[j])
# the first term is the cost of merge the first pile(just stone A[i] in this case) and dp[i+1][j] is the energy needed
# to merge A[i+1]....A[j],    sum(A[i]......A[j]) is the cost of this specific merge.

# if the last step is to merge pile (A[i],A[i+1) and pile (A[i+2].....A[j])(these stones already merge into two big piles)
# the total energy/score is dp[i][i+1]+dp[i+2][j] +sum(A[i]......A[j])
# the first term dp[i][i+1]is the cost of merge the first pile  A[i]....A[i+1],
# and dp[i+1][j] is the energy needed to merge A[i+2]....A[j],
# sum(A[i]......A[j]) is the cost of this specific merge.

# so the formular is the following
# dp[i][j] = min(dp[i][k] + dp[k+1][j] + sum(A[i].....A[j])  | for all i<k<j)

import sys


class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def stoneGame(self, A):
        n = len(A)
        if n == 0:
            return 0
        if n == 0:
            return A[0]

        prefix_sum = [0] * (n + 1)
        prefix_sum[0] = 0
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

        dp = [[None] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for length in range(2, len(A)+1):
            for i in range(0, n - 1 - length+2):
                j = i + length-1
                dp[i][j] = sys.maxsize
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j]+self.get_sum(prefix_sum, i, j))

        return dp[0][n-1]

    def get_sum(self, prefix_sum_arr, i, j):
        return prefix_sum_arr[j + 1] - prefix_sum_arr[i]


sol = Solution()
assert sol.stoneGame(A=[4,1,5,10]) == 35
assert sol.stoneGame(A=[4, 1, 1, 4]) ==18
assert sol.stoneGame(A=[3,4,3]) == 17