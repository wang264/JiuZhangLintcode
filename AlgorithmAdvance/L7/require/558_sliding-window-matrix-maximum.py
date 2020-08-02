# 滑动窗口矩阵的最大值 · Sliding Window Matrix Maximum
# 描述
# Given an array of n * m matrix, and a moving matrix window (size k * k), move the window from top left to
# bottom right at each iteration, find the maximum sum inside the window at each moving.
# Return 0 if the answer does not exist.
#
# 样例
# Example 1:
#
# Input：[[1,5,3],[3,2,1],[4,1,9]]，k=2
# Output：13
# Explanation：
# At first the window is at the start of the matrix like this
#
# 	[
# 	  [|1, 5|, 3],
# 	  [|3, 2|, 1],
# 	  [4, 1, 9],
# 	]
# ,get the sum 11;
# then the window move one step forward.
#
# 	[
# 	  [1, |5, 3|],
# 	  [3, |2, 1|],
# 	  [4, 1, 9],
# 	]
# ,get the sum 11;
# then the window move one step forward again.
#
# 	[
# 	  [1, 5, 3],
# 	  [|3, 2|, 1],
# 	  [|4, 1|, 9],
# 	]
# ,get the sum 10;
# then the window move one step forward again.
#
# 	[
# 	  [1, 5, 3],
# 	  [3, |2, 1|],
# 	  [4, |1, 9|],
# 	]
# ,get the sum 13;
# SO finally, get the maximum from all the sum which is 13.
# Example 2:
#
# Input：[[10]，k=1
# Output：10
# Explanation：
# sliding window size is 1*1，and return 10.

import sys


class Solution:
    """
    @param matrix: an integer array of n * m matrix
    @param k: An integer
    @return: the maximum number
    """

    def maxSlidingMatrix(self, matrix, k):
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        prefix_sum = [[0] * (num_cols + 1) for _ in range(num_rows + 1)]

        # prefix_sum[0][0] = matrix[0][0]
        for i in range(1, num_rows + 1):
            for j in range(1, num_cols + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + \
                                   matrix[i - 1][j - 1]

        max_value = -1 * sys.maxsize
        for i in range(k, num_rows + 1):
            for j in range(k, num_cols + 1):
                value = prefix_sum[i][j] - prefix_sum[i - k][j] - prefix_sum[i][j - k] + prefix_sum[i - k][j - k]

                if value > max_value:
                    max_value = value

        return max_value


sol = Solution()
sol.maxSlidingMatrix(matrix=[[1, 5, 3], [3, 2, 1], [4, 1, 9]], k=2)
