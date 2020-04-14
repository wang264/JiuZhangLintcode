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

    def kSum(self, A, k, target):
        # write your code here
        # 有多少种方法让背包装满。
        # 看最后一个数A_n-1 是否选入这K个数
        # 情况一：A_n-1不选入：需要在前n-1个数中选K个数，使得它们的和是target.
        # 情况二：A_n-1选入：需要在前n-1个数中选K-1个数，使得他们的和是target - A_n-1

        # f[i][k][s] 表示有多少种方法可以在前i个数中选出k个，使得它们的和是s。

        m = len(A)
        num_numbers = k
        f = [[[None] * (target + 1) for _ in range(num_numbers + 1)] for _ in range(m + 1)]

        for i in range(0, m + 1):
            for k in range(0, num_numbers + 1):
                for s in range(0, target + 1):
                    if i == 0 and k == 0 and s == 0:
                        f[i][k][s] = 1
                        continue
                    if i == 0:
                        f[i][k][s] = 0
                        continue

                    # not chose A_n-1
                    f[i][k][s] = f[i - 1][k][s]
                    # chose A_n-1
                    if k > 0 and s >= A[i - 1]:
                        f[i][k][s] += f[i - 1][k - 1][s - A[i - 1]]

        return f[m][num_numbers][target]


A = [1, 2, 3, 4]
k = 2
target = 5
sol = Solution()
sol.kSum(A, k, target)
