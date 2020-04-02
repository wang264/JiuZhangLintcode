# 515. Paint House
# 中文English
# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
# The cost of painting each house with a certain color is different. You have to paint all the houses such that no
#  two adjacent houses have the same color, and you need to cost the least. Return the minimum cost.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example,
# costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with
# color green, and so on... Find the minimum cost to paint all houses.
#
# Example
# Example 1:
#
# Input: [[14,2,11],[11,14,5],[14,3,10]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.
# Example 2:
#
# Input: [[1,2,3],[1,4,6]]
# Output: 3
# Notice
# All costs are positive integers.

import sys


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        # write your code here
        # there are n house, with house number #0, #1,......#(n-1)
        # dp[i][0] minimum cost to paint the first ith houses(0,1,2,3....i-1) and the #(i-1) is painted.RED
        # dp[i][1] minimum cost to paint the first ith houses(0,1,2,3....i-1) and the #(i-1), is painted.BLUE
        # dp[i][2] minimum cost to paint the first ith houses(0,1,2,3....i-1) and the #(i-1), is painted.GREEN
        number_of_houses = len(costs)
        if number_of_houses == 0:
            return 0
        dp = [[0] * 3 for _ in range(number_of_houses + 1)]

        # the cost to not paint any houses are zero
        dp[0][0] = dp[0][1] = dp[0][2] = 0

        for i in range(1, number_of_houses + 1):
            # house #(i-1)'s color is j   !!!!! the i'th house will be index i-1
            for j in range(3):
                dp[i][j] = sys.maxsize
                # house #(i-2)'s color is k
                for k in range(3):
                    if j == k:
                        continue
                    # dp[i][j] = the minimum cost to paint the first i houses, and the House #(i-1) is paint with color j
                    # dp[i - 1][k] = the minimum cost to paint the first i-1 houses, and the House #(i-2) is paint with color k
                    # costs[i - 1][j] = the cost of paint the House #(i-1) with color j
                    # noted that k not equal to j since adjacent houses can not paint with same color
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])

        return min(dp[number_of_houses][0], dp[number_of_houses][1], dp[number_of_houses][2])
