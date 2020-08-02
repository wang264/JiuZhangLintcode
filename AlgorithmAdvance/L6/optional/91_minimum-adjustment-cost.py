# 91. Minimum Adjustment Cost
# 中文English
# Given an integer array, adjust each integers so that the difference of every adjacent integers are not greater
# than a given number target.
#
# If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of | A[i] - B[i] |
#
#
# Example 1:
# Input: [1, 4, 2, 3], target = 1
# Output: 2
#
# Example 2:
# Input: [3, 5, 4, 7], target = 2
# Output: 1
#
# Notice You can assume each number in the array is a positive integer and not greater than 100.

# 91. 最小调整代价
# 中文English
# 给一个整数数组，调整每个数的大小，使得相邻的两个数的差不大于一个给定的整数target，调整每个数的代价为调整前后的
# 差的绝对值，求调整代价之和最小是多少。
#
# Example
# 样例
# 1:
# 输入: [1, 4, 2, 3], target = 1
# 输出: 2
#
# 样例
# 2:
# 输入: [3, 5, 4, 7], target = 2
# 输出: 1
#
# Notice
# 你可以假设数组中每个整数都是正整数，且小于等于100。

import sys


class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """

    def MinAdjustmentCost(self, A, target):
        # write your code here
        n = len(A)
        # dp[i][j] the minimum adjustment cost to get valid A[0].....A[i] when A[i]=j
        dp = [[sys.maxsize] * 101 for _ in range(n)]
        for i in range(n):
            for j in range(1, 101):
                if i == 0:
                    # the total cost will be the cost to adjust A[0] to j
                    dp[0][j] = abs(j - A[0])
                    continue
                # given A[i] = j, the minimum and maximum value for valid A[i-1] so that abs(A[i]-A[i-1])<=target
                # left: min(1,j - target)
                # right: max(j + target,100)
                left = max(1, j - target)
                right = min(j + target, 100)
                for k in range(left, right + 1):
                    # when A[i-1] = k, total cost is dp[i-1][k] and the cost to adjust A[i] to j
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(j - A[i]))

        return min(dp[n - 1])

sol = Solution()
sol.MinAdjustmentCost(A=[1,4,2,3], target=1)