# 668. Ones and Zeroes
# 中文English
# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
#
# For now, suppose you are a dominator of m 0s and n 1s respectively.
# On the other hand, there is an array with strings consisting of only 0s and 1s.
#
# Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s.
# Each 0 and 1 can be used at most once.
#
# 样例

# Example1
# Input:
# ["10", "0001", "111001", "1", "0"]
# 5
# 3
# Output: 4
# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10", "0001", "1", "0"

# Example2
# Input:
# ["10", "0001", "111001", "1", "0"]
# 7
# 7
# Output: 5
# Explanation: All strings can be formed by the using of 7 0s and 7 1s.

# 注意事项
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.

class Solution:
    """
    @param strs: an array with strings include only 0 and 1
    @param m: An integer
    @param n: An integer
    @return: find the maximum number of strings
    """

    # 双背包问题。问最多能装多少个物品，你有两个背包一个包装1一个包装0.
    # 最后一步：最优策略组成了最多的01串，其中有没有最后一个字符串S_t-1.
    # 情况一：没有S_t-1
    # 需要知道前T-1 个01串中，用m个0和n个1最多能组成多少个01串。
    # 情况二：有S_t-1
    # 假设第T-1个01串中有a_t-1个0， b_t-1个1
    # 需要知道前T-1个01串中，用m - a_t-1 个 0 和 n - b_t-1个1最多能组成多少01串

    # f[i][j][k] = 前i个01串最多能有多少个被j个0和k个1组成。

    def findMaxForm(self, strs, m, n):
        # write your code here
        if len(strs) == 0:
            return 0

        T = len(strs)
        count_0 = [s.count('0') for s in strs]
        count_1 = [s.count('1') for s in strs]

        f = [[[None] * (n + 1) for _ in range(m + 1)] for _ in range(T + 1)]

        # 前0个01串无法被组成。
        for j in range(m + 1):
            for k in range(n + 1):
                f[0][j][k] = 0

        for i in range(1, T + 1):
            for j in range(m + 1):
                for k in range(n + 1):
                    # j 0's and k 1's

                    # 情况一, do not take strs[i-1]
                    f[i][j][k] = f[i - 1][j][k]

                    # 情况二, take strs[i-1]
                    if j >= count_0[i - 1] and k >= count_1[i - 1]:
                        f[i][j][k] = max(f[i][j][k], f[i-1][j - count_0[i - 1]][k - count_1[i - 1]] + 1)

        rslt = 0
        for j in range(0, m + 1):
            for k in range(0, n + 1):
                rslt = max(rslt, f[T][j][k])

        return rslt


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
sol = Solution()
sol.findMaxForm(strs, m, n)
