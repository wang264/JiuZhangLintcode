# 109. Triangle
# 中文English
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# 样例
# Example 1:
#
# Input the following triangle:
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# Output: 11
# Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# Example 2:
#
# Input the following triangle:
# [
#      [2],
#     [3,2],
#    [6,5,7],
#   [4,4,8,1]
# ]
# Output: 12
# Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).
# 注意事项
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


################################################
# DP,
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        # dp[i][j] means the minimum path sum from (0, 0) to (i, j)
        dp = [[0] * n for _ in range(n)]

        dp[0][0] = triangle[0][0]

        # fill the boundary, if j=0 or j=i, then that path must from upper right and upper left respectively.
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        for i in range(1, n):
            for j in range(1, i):
                # upper right path ----> dp[i - 1][j]
                # upper left path -----> p[i - 1][j - 1]
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        # answer will be the min of the last layer.
        return min(dp[n - 1])


################################################
# use memorization search, and divide_conquer
class Solution2:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        return self.divide_conquer(triangle, 0, 0, {})

    # memo[(i,j)] = the minimum path sum from (i,j) to bottom.
    def divide_conquer(self, triangle, i, j, memo):
        # we are reach the bottom
        if i >= len(triangle):
            return 0

        # if we solve this problem before, just return it
        if (i, j) in memo.keys():
            return memo[(i, j)]

        left = self.divide_conquer(triangle, i + 1, j, memo)
        right = self.divide_conquer(triangle, i + 1, j + 1, memo)

        rslt = min(left, right) + triangle[i][j]
        memo[(i, j)] = rslt
        return rslt


l = [
    [2],
    [3, 2],
    [6, 5, 7],
    [4, 4, 8, 1]
]

sol = Solution()
sol.minimumTotal(triangle=l)
