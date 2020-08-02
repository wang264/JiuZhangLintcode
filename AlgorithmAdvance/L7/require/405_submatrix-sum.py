# 405. Submatrix Sum
# 中文English
# Given an integer matrix, find a submatrix where the sum of numbers is zero. Your code should return the
# coordinate of the left-up and right-down number.
#
# If there are multiple answers, you can return any of them.
#
# Example
# Example 1:
#
# Input:
# [
#   [1, 5, 7],
#   [3, 7, -8],
#   [4, -8 ,9]
# ]
# Output: [[1, 1], [2, 2]]
# Example 2:
#
# Input:
# [
#   [0, 1],
#   [1, 0]
# ]
# Output: [[0, 0], [0, 0]]
# Challenge
# O(n3) time.

class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        # write your code here
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        prefix_sum = [[0] * (num_cols + 1) for _ in range(num_rows + 1)]

        # prefix_sum[0][0] = matrix[0][0]
        for i in range(1, num_rows + 1):
            for j in range(1, num_cols + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + \
                                   matrix[i - 1][j - 1]

        # iterate all upper-left point (x1,y1) and lower right point(x2,y2)
        for x1 in range(1, num_rows+1):
            for y1 in range(1, num_cols+1):
                for x2 in range(x1, num_rows+1):
                    for y2 in range(y1, num_cols+1):
                        if prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1]+prefix_sum[x1-1][y1-1]==0:
                            rslt = []
                            rslt.append([x1 - 1, y1 - 1])
                            rslt.append([x2 - 1, y2 - 1])
                            return rslt

sol= Solution()
matrix = [
  [1, 5, 7],
  [3, 7, -8],
  [4, -8 ,9]
]
sol.submatrixSum(matrix)