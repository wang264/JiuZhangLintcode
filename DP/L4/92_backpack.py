# 92.Backpack
# 中文English
# Given n items with size Ai, an integer m denotes the size of a backpack.How full you can fill this backpack?
#
# Example
# 1:
# Input: [3, 4, 8, 5],
# backpack size = 10
# Output: 9
#
# Example
# 2:
# Input: [2, 3, 5, 7],
# backpack size = 12
# Output: 12
#
# ChallengeO(nxm) time and O(m) memory.
# O(n x m) memory is also acceptable if you do not know how to optimize memory.
# Notice You can not divide any item into small pieces.

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    # f[i][w]= 能否用前i个物品拼出重量w  True/False

    # f[i][w] = f[i-1][w] or f[i-1][w - A[i-1]]
    # 前i个物品能否拼出重量w = 前i-1拼出重量w OR 前i-1拼出重量w-A[i-1] 再加上第i个物品。
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        f = [[False] * (m + 1) for _ in range(n + 1)]

        # initial condition
        f[0][0] = True  # 前0 个物品能拼出重量0
        for w in range(1, m + 1):
            f[0][w] = False  # 前0个物品不能拼出重量w

        for i in range(1, n + 1):
            for w in range(0, m + 1):
                f[i][w] = f[i - 1][w]  # 不用第i个物品

                if w - A[i - 1] >= 0:
                    # 用第i个物品
                    f[i][w] = True

        # 用所有的物品，能拼出来的重量的最大的那个
        weights = [w for w in range(0, m + 1) if f[n][w] is True]
        return max(weights)


sol = Solution()
m = 10
A = [3, 4, 8, 5]
sol.backPack(m, A)

import numpy as np


class Solution2:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        # dp[i][j] can you use the first i element to sum to weight m
        n = len(A)
        dp = np.array([[False] * (m + 1) for _ in range(n + 1)])

        dp[0][0] = True

        for i in range(1, n + 1):
            weight = A[i - 1]
            for j in range(0, m + 1):
                dp[i][j] = dp[i - 1][j]  # do not use the ith element
                if j - weight >= 0:
                    if dp[i - 1][j - weight]:
                        # use the ith element
                        dp[i][j] = True

        weights = [w for w in range(0, m + 1) if dp[n][w]]
        return max(weights)


sol = Solution2()
m = 10
A = [3, 4, 8, 5]
sol.backPack(m, A)
