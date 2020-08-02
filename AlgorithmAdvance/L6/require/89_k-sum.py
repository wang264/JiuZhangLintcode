# 89. k Sum
# 中文English
# Given n distinct positive integers, integer k (k <= n) and a number target.
#
# Find k numbers where sum is target. Calculate how many solutions there are?
#
# 样例
# Example 1
#
# Input:
# List = [1,2,3,4]
# k = 2
# target = 5
# Output: 2
# Explanation: 1 + 4 = 2 + 3 = 5
# Example 2
#
# Input:
# List = [1,2,3,4,5]
# k = 3
# target = 6
# Output: 1
# Explanation: There is only one method. 1 + 2 + 3 = 6


class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """

    # write your code here
    # 有多少种方法让背包装满。
    # 看最后一个数A_n-1 是否选入这K个数
    # 情况一：A_n-1不选入：需要在前n-1个数中选K个数，使得它们的和是target.
    # 情况二：A_n-1选入：需要在前n-1个数中选K-1个数，使得他们的和是target - A_n-1

    # f[i][k][s] 表示有多少种方法可以在前i个数中选出k个，使得它们的和是s。
    # dp[i][k][s] = number of ways to use the first 'i' numbers in A, select 'k' of them, to sum to target 's'

    def kSum(self, A, k, target):
        n = len(A)
        num_numbs = k
        dp = [[[None] * (target + 1) for _ in range(k + 1)] for _ in range(n + 1)]

        for i in range(0, n + 1):
            for k in range(num_numbs + 1):
                for s in range(0, target + 1):
                    if i == 0 and k == 0 and s == 0:
                        dp[i][k][s] = 1
                        continue
                    if i == 0:
                        dp[i][k][s] = 0
                        continue

                    # not use the ith number A[i-1]
                    dp[i][k][s] = dp[i - 1][k][s]
                    # use the ith number A[i-1]
                    if k > 0 and s - A[i - 1] >= 0:
                        dp[i][k][s] += dp[i - 1][k - 1][s - A[i - 1]]

        return dp[n][num_numbs][target]


A = [1, 2, 3, 4]
k = 2
target = 5
sol = Solution()
sol.kSum(A, k, target)
