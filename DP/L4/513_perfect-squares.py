# 513. Perfect Squares
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example
# Example 1:
#
# Input: 12
# Output: 3
# Explanation: 4 + 4 + 4
# Example 2:
#
# Input: 13
# Output: 2
# Explanation: 4 + 9

import sys


class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        # write your code here
        # f[i] = the minimum numbers of perfect square sum that equals to i.

        # f[i] = min(f[i-j*j] +1, for all 1<=j*j<=i)

        f = [0] * (n + 1)

        # initialization
        f[0] = 0  # the minimum numbers of perfect square sum that equals to 0 is 0.
        for i in range(1, n + 1):
            # for all j from 1<=j*j<=i:
            f[i] = sys.maxsize
            for j in range(1, int(i ** 0.5) + 1):
                f[i] = min(f[i], f[i - j * j] + 1)

        return f[n]


sol = Solution()
sol.numSquares(1000)
