# 516. Paint House II
# 中文English
# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each
# house with a certain color is different. You have to paint all the houses such that no two adjacent
# houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x k cost matrix.
# For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the
# cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
#
# Example 1
#
# Input:
# costs = [[14,2,11],[11,14,5],[14,3,10]]
# Output: 10
# Explanation:
# The three house use color [1,2,1] for each house. The total cost is 10.
# Example 2
#
# Input:
# costs = [[5]]
# Output: 5
# Explanation:
# There is only one color and one house.
# Challenge
# Could you solve it in O(nk)?
#
# Notice
# All costs are positive integers.

import sys


class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """

    def minCostII(self, costs):
        # write your code here
        # there are n house, with house number #0, #1,......#(n-1)
        # dp[i][0] minimum cost to paint the first ith houses(0,1,2,3....i-1) and the #(i-1) is painted.RED
        # dp[i][1] minimum cost to paint the first ith houses(0,1,2,3....i-1) and the #(i-1), is painted.BLUE
        # dp[i][2] minimum cost to paint the first ith houses(0,1,2,3....i-1) and the #(i-1), is painted.GREEN
        number_of_houses = len(costs)
        if number_of_houses == 0:
            return 0
        num_colors = len(costs[0])
        dp = [[0] * num_colors for _ in range(number_of_houses + 1)]

        # the cost to not paint any houses are zero
        for j in range(num_colors):
            dp[0][j] = 0

        for i in range(1, number_of_houses + 1):
            # find minimum and 2nd minimum color, among dp[i-1][0], dp[i-1][1].....dp[i-1][num_colors - 1]
            minimum = minimum_2nd = -1
            for k in range(num_colors):
                # smaller than the current minimum
                if minimum == -1 or dp[i - 1][k] < dp[i - 1][minimum]:
                    minimum_2nd = minimum  # old minimum become the 2nd minimum now
                    minimum = k  # new minimum is now dp[i-1][k]
                # larger than minimum but smaller than 2nd minimum, only updare second minimum
                elif minimum_2nd == -1 or dp[i - 1][k] < dp[i - 1][minimum_2nd]:
                    minimum_2nd = k

            # house #(i-1)'s color is j   !!!!! the i'th house will be index i-1
            for j in range(num_colors):
                if j != minimum:
                    # if we remove an element from a list which its value is NOT the minimum value.
                    # then the minimum value is the minimum value of that list
                    dp[i][j] = dp[i-1][minimum] + costs[i-1][j]
                else:
                    # if we remove an element from a list which its value is the minimum value.
                    # then the minimum value is the 2ND MINIMUM value of that list
                    dp[i][j] = dp[i - 1][minimum_2nd] + costs[i - 1][j]

        min_cost = sys.maxsize
        for j in range(num_colors):
            min_cost = min(min_cost, dp[number_of_houses][j])
        return min_cost

    def minCostII_time_limit_exceed(self, costs):
        # write your code here
        # there are n house, with house number #0, #1,......#(n-1)
        # dp[i][0] minimum cost to paint the first ith houses(0,1,2,3....i-1) and the #(i-1) is painted.RED
        # dp[i][1] minimum cost to paint the first ith houses(0,1,2,3....i-1) and the #(i-1), is painted.BLUE
        # dp[i][2] minimum cost to paint the first ith houses(0,1,2,3....i-1) and the #(i-1), is painted.GREEN
        number_of_houses = len(costs)
        if number_of_houses == 0:
            return 0
        num_colors = len(costs[0])
        dp = [[0] * num_colors for _ in range(number_of_houses + 1)]

        # the cost to not paint any houses are zero
        for j in range(num_colors):
            dp[0][j] = 0

        for i in range(1, number_of_houses + 1):
            # house #(i-1)'s color is j   !!!!! the i'th house will be index i-1
            for j in range(num_colors):
                dp[i][j] = sys.maxsize
                # house #(i-2)'s color is k
                for k in range(num_colors):
                    if j == k:
                        continue
                    # dp[i][j] = the minimum cost to paint the first i houses, and the House #(i-1) is paint with color j
                    # dp[i - 1][k] = the minimum cost to paint the first i-1 houses, and the House #(i-2) is paint with color k
                    # costs[i - 1][j] = the cost of paint the House #(i-1) with color j
                    # noted that k not equal to j since adjacent houses can not paint with same color
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])

        min_cost = sys.maxsize
        for j in range(num_colors):
            min_cost = min(min_cost, dp[number_of_houses][j])
        return min_cost
