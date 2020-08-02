# 125. Backpack II
# 中文English
# There are n items and a backpack with size m. Given array A representing the size of each item
# and array V representing the value of each item.
#
# What's the maximum value can you put into the backpack?
#
# Example
# Example 1:
#
# Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
# Output: 9
# Explanation: Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9
# Example 2:
#
# Input: m = 10, A = [2, 3, 8], V = [2, 5, 8]
# Output: 10
# Explanation: Put A[0] and A[2] into backpack, getting the maximum value V[0] + V[2] = 10
# Challenge
# O(nm) memory is acceptable, can you do it in O(m) memory?
#
# Notice
# A[i], V[i], n, m are all integers.
# You can not split an item.
# The sum size of the items you want to put into backpack can not exceed m.
# Each item can only be picked up once

import sys


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        # f[i][w] = 用前i个物品(每个物品可以用也可以不用)拼出重量为w时的最大总价值是多少。
        # f[i][w] = -1 代表不能拼出该物品。
        # f[i][w] = 选择一：如果不用最后一个物品　选择二：用最后一个物品。
        # 选择一：　f[i][w] = f[i-1][w]
        # 选择二:   f[i][w] = f[i-1][w-A[i-1]] + V[i-1] | w-A[i-1]>=0  and f[i-1][w-A[i-1]] != -1
        # f[i-1][w-A[i-1]] + V[i-1] = 用前i-1个物品拼出重量为w-A[i-1]]的背包的最大总价值　+ 第i的物品的价值
        # f[i-1][w-A[i-1]] 意思是，我们能用前i-1个物品拼出重量为w-A[i-1]]的背包
        n = len(A)
        f = [[None] * (m + 1) for _ in range(n + 1)]

        f[0][0] = 0  # 用0个物品拼出重量为0的背包, 总价值为0
        for w in range(1, m + 1):
            f[0][w] = -1  # 用0个物品无法拼出重量不为0的背包

        for i in range(1, n + 1):
            f[i][0] = 0  # 用前i个物品拼出重量为0的背包, 最大总价值为0
            for w in range(1, m + 1):
                # 选择一：如果不用最后一个物品
                f[i][w] = f[i - 1][w]
                # 选择二：用最后一个物品。
                if w - A[i - 1] >= 0 and f[i - 1][w - A[i - 1]] != -1:
                    f[i][w] = max(f[i][w], f[i - 1][w - A[i - 1]] + V[i - 1])

        # 用前n个（所有的物品），能拼出来的所有的可能的重量的最大总价值是多少。
        return max(f[n])

sol = Solution()
assert sol.backPackII(m=10, A=[2, 3, 5, 7], V=[1, 5, 2, 4]) == 9
assert sol.backPackII(m=10, A=[2, 3, 8], V=[2, 5, 8]) == 10

