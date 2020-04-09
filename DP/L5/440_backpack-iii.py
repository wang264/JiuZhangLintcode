# 440. Backpack III
# 中文English
# Given n kinds of items, and each kind of item has an infinite number available.
# The i-th item has size A[i] and value V[i].
#
# Also given a backpack with size m. What is the maximum value you can put into the backpack?
#
# Example
# Example 1:
#
# Input: A = [2, 3, 5, 7], V = [1, 5, 2, 4], m = 10
# Output: 15
# Explanation: Put three item 1 (A[1] = 3, V[1] = 5) into backpack.
# Example 2:
#
# Input: A = [1, 2, 3], V = [1, 2, 3], m = 5
# Output: 5
# Explanation: Strategy is not unique. For example, put five item 0 (A[0] = 1, V[0] = 1) into backpack.
# Notice
# You cannot divide item into small pieces.
# Total size of items you put into backpack can not exceed m.

class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    # f[i][w] = 前i种物品拼出重量w时的最大总价值(-1表示不能拼出w)
    # f[i][w] = maximum of f[i-1][w - k*A[i-1]] + k*V[i-1] , for 0<=k< np.inf, but w - k*A[i-1] need to larger than 0.
    # 用k个最后一个物品, 然后用前i-1种物品拼出重量 w - k*A[i-1],
    def backPackIII_slow(self, A, V, m):
        # write your code here
        n = len(A)
        f = [[None] * (m + 1) for _ in range(n + 1)]

        f[0][0] = 0  # 前0种物品拼出总量为0的背包时的最大总价值

        for w in range(1, m + 1):
            f[0][w] = -1  # 无法用前0个物品拼出总重量不为0的背包

        for i in range(1, n + 1):
            f[i][0] = 0  # 用前0个物品拼出总重量为0的背包, 最大总价值为0
            for w in range(1, m + 1):
                f[i][w] = -1  # 假设拼不出来
                for k in range(0, m + 1):  # 每个物品最轻为1，背包重量为m,所以你最多一种物品拿m个
                    if w - k * A[i - 1] < 0:  # 再拿下去，重量就为负了
                        break
                    if f[i - 1][w - k * A[i - 1]] != -1:
                        f[i][w] = max(f[i][w], f[i - 1][w - k * A[i - 1]] + k * V[i - 1])

        return max(f[n])

    def backPackIII(self, A, V, m):
        # write your code here
        n = len(A)
        f = [[None] * (m + 1) for _ in range(n + 1)]

        f[0][0] = 0  # 前0种物品拼出总量为0的背包时的最大总价值

        for w in range(1, m + 1):
            f[0][w] = -1  # 无法用前0个物品拼出总重量不为0的背包

        for i in range(1, n + 1):
            f[i][0] = 0  # 用前0个物品拼出总重量为0的背包, 最大总价值为0
            for w in range(1, m + 1):
                f[i][w] = f[i - 1][w]  # 假设拼不出来
                if w - A[i - 1] >= 0 and f[i][w - A[i - 1]] != -1:
                    f[i][w] = max(f[i][w], f[i][w - A[i - 1]] + V[i - 1])

        return max(f[n])


A = [88, 85, 59, 100, 94, 64, 79, 75, 18, 38, 47, 11, 56, 12, 96, 54, 23, 6, 19, 31, 30, 32, 21, 31, 4, 30, 3, 12, 21,
     60, 42, 42, 78, 6, 72, 25, 96, 21, 77, 36, 42, 20, 7, 46, 19, 24, 95, 3, 93, 73, 62, 91, 100, 58, 57, 3, 32, 5, 57,
     50, 3, 88, 67, 97, 24, 37, 41, 36, 98, 52, 75, 7, 57, 23, 55, 93, 4, 17, 5, 13, 46, 48, 28, 24, 70, 85, 48, 48, 55,
     93, 6, 8, 12, 50, 95, 66, 92, 25, 80, 16]
V = [53, 70, 20, 41, 12, 71, 37, 87, 51, 64, 63, 50, 73, 83, 75, 60, 96, 70, 76, 25, 27, 89, 93, 40, 41, 89, 93, 46, 16,
     4, 41, 29, 99, 82, 42, 14, 69, 75, 20, 20, 56, 23, 92, 71, 70, 1, 63, 18, 11, 68, 33, 6, 82, 69, 78, 48, 95, 42,
     53, 99, 15, 76, 64, 39, 48, 83, 21, 75, 49, 73, 85, 28, 31, 86, 63, 12, 71, 35, 21, 17, 73, 18, 7, 51, 94, 88, 46,
     77, 80, 95, 31, 80, 32, 45, 5, 30, 51, 63, 43, 9]
m = 965
sol = Solution()
sol.backPackIII(A, V, m)
# Output: 15
# Explanation: Put three item 1 (A[1] = 3, V[1] = 5) into backpack.
# Example 2:
